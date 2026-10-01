
<h1> Guia completa: Odoo 16 + Docker en macOS </h1>

### Entorno de desarrollo con Docker Compose para Odoo 16 y PostgreSQL 15 en macOS.

---

### Contenido

- Arquitectura del entorno
- Instalacion y requisitos
- Configuracion de Docker Compose y Odoo
- Activar Odoo Enterprise
- Gestion de modulos y addons
- Git y repositorios
- Bases de datos y PostgreSQL
- PyCharm
- Python local para otros proyectos
- Comandos frecuentes y troubleshooting

---

### Arquitectura

Este entorno utiliza macOS como sistema anfitrion y Docker para ejecutar Odoo y PostgreSQL.

```text
~/odoo16/
├── addons/                 # modulos propios y repositorios Git
├── enterprise/             # addons de Odoo Enterprise
├── config/
│   └── odoo.conf          # configuracion de Odoo
└── docker-compose.yml
```

Dentro de Docker:

- Servicio `odoo` → imagen `odoo:16.0`
- Servicio `db` → imagen `postgres:15`
- `./addons` del Mac → `/mnt/extra-addons` dentro de Odoo
- `./config` del Mac → `/etc/odoo` dentro de Odoo
- Puerto del Mac `8016` → puerto Odoo `8069`

---

### Requisitos

Instalar:

- Docker Desktop
- Git
- Homebrew (recomendado)
- PyCharm

Python local es opcional. Para Odoo no es necesario si Odoo se ejecuta dentro de Docker.

Comprobar Git:

```bash
git --version
```

---

### Crear la carpeta del proyecto

```bash
mkdir -p ~/odoo16
cd ~/odoo16
mkdir -p addons
mkdir -p config
```

---

### docker-compose.yml

Ejemplo base:

```yaml
services:
  db:
    image: postgres:15
    container_name: odoo16-db
    environment:
      POSTGRES_DB: postgres
      POSTGRES_USER: odoo
      POSTGRES_PASSWORD: odoo
    volumes:
      - odoo16-db-data:/var/lib/postgresql/data

  odoo:
    image: odoo:16.0
    container_name: odoo16
    depends_on:
      - db
    ports:
      - "8016:8069"
    volumes:
      - ./config:/etc/odoo
      - ./addons:/mnt/extra-addons
    command: odoo -c /etc/odoo/odoo.conf

volumes:
  odoo16-db-data:
```

> **Nota:** Si Docker Compose muestra que `version` es obsolete, no es un error. En Compose moderno se puede eliminar la propiedad `version:`.

---

### odoo.conf

Crear el archivo:

```text
~/odoo16/config/odoo.conf
```

Contenido base:

```ini
[options]
data_dir = /var/lib/odoo
db_host = db
db_port = 5432
db_user = odoo
db_password = odoo
log_level = info
workers = 0
limit_time_real = 0
addons_path = /mnt/extra-addons
```

> **Muy importante:** El formato debe ser `clave = valor`.

Incorrecto:

```text
addons_path /mnt/extra-addons
```

Correcto:

```text
addons_path = /mnt/extra-addons
```

---

### Levantar Odoo

```bash
cd ~/odoo16
docker compose up -d
docker compose ps
```

Ver logs:

```bash
docker compose logs -f odoo
```

Acceder a Odoo:

```text
http://localhost:8016
```

---

### Activar Odoo Enterprise

Una vez que Odoo Community esta corriendo correctamente en `http://localhost:8016`, se puede activar la version Enterprise.

1. Apagar el contenedor:

```bash
cd ~/odoo16
docker compose down
```

2. Descargar Odoo Enterprise desde el portal de Odoo usando tu licencia. En macOS el archivo se descarga como `.tar.gz`.

3. Descomprimir el archivo descargado. Dentro encontraras una estructura similar a:

```text
odoo-16.0+eXXXX/
└── odoo/
    └── addons/        # addons enterprise
```

4. Crear la carpeta `enterprise` dentro del proyecto:

```bash
mkdir -p ~/odoo16/enterprise
```

5. Copiar todos los addons enterprise desde la ruta descomprimida a la carpeta del proyecto:

```bash
cp -r /ruta/a/odoo-16.0+eXXXX/odoo/addons/* ~/odoo16/enterprise/
```

6. Agregar el volumen de enterprise en `docker-compose.yml`:

```yaml
    volumes:
      - ./config:/etc/odoo
      - ./addons:/mnt/extra-addons
      - ./enterprise:/mnt/enterprise
```

7. Agregar la ruta de enterprise en `odoo.conf`:

```ini
addons_path = /mnt/extra-addons,/mnt/enterprise
```

8. Levantar el contenedor nuevamente:

```bash
docker compose up -d
```

9. Ir a `http://localhost:8016`, entrar a **Aplicaciones**, buscar `web_enterprise` e instalarla.

Una vez instalado `web_enterprise`, Odoo cambiara a la interfaz Enterprise.

---

### Comprobar addons dentro del contenedor

```bash
docker compose exec odoo bash
ls -la /mnt/extra-addons
```

Tambien:

```bash
docker compose exec odoo bash -lc 'nl -ba /etc/odoo/odoo.conf'
```

---

### Crear un modulo de prueba

```bash
mkdir -p addons/hello_world
cat > addons/hello_world/__manifest__.py <<'PY'
{
    "name": "Hello World",
    "version": "16.0.1.0.0",
    "depends": ["base"],
    "installable": True,
    "application": False,
}
PY
touch addons/hello_world/__init__.py
```

Comprobar:

```bash
docker compose exec odoo bash -lc 'ls -la /mnt/extra-addons'
```

---

### Bases de datos

Administrador de bases de datos:

```text
http://localhost:8016/web/database/manager
```

PostgreSQL:

```bash
docker compose exec db psql -U odoo -d postgres
```

Dentro de `psql`:

```sql
\l
```

Salir:

```sql
\q
```

El volumen `odoo16-db-data` conserva los datos.

```bash
docker compose down
```

no elimina normalmente el volumen.

> **Advertencia:** Este comando si elimina los volumenes:

```bash
docker compose down -v
```

No usarlo si quieres conservar las bases.

---

### Actualizar modulos

```bash
docker compose exec odoo odoo   -c /etc/odoo/odoo.conf   -u NOMBRE_MODULO   -d NOMBRE_BASE
```

Ejemplo:

```bash
docker compose exec odoo odoo   -c /etc/odoo/odoo.conf   -u almx_pricelock   -d mi_base
```

---

### PyCharm

Con PyCharm Professional y Docker Compose disponible, se puede utilizar un interprete remoto basado en el servicio `odoo`.

Configuracion utilizada anteriormente:

```text
Script: /usr/bin/odoo

-c /etc/odoo/odoo.conf
--addons-path=/usr/lib/python3/dist-packages/odoo/addons,/mnt/extra-addons
--dev=all
--limit-time-real=0
--workers=0
```

> **Nota:** Si PyCharm intenta ejecutar:

```text
/usr/bin/python3 /usr/bin/odoo
```

en macOS y aparece `can't open file '/usr/bin/odoo'`, esta ejecutando el Python local y no el Odoo del contenedor.

---

### Python local para otros proyectos

No afecta al Odoo de Docker.

Crear un proyecto independiente:

```bash
mkdir ~/proyectos/mi_proyecto
cd ~/proyectos/mi_proyecto
python3 -m venv .venv
source .venv/bin/activate
python --version
pip --version
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Salir:

```bash
deactivate
```

---

### Comandos frecuentes

```bash
docker compose up -d
docker compose down
docker compose restart odoo
docker compose ps
docker compose logs -f odoo
docker compose exec odoo bash
docker compose exec db psql -U odoo -d postgres
docker compose down --remove-orphans
```

Actualizar modulo:

```bash
docker compose exec odoo odoo -c /etc/odoo/odoo.conf -u modulo -d base
```

---

### Problemas frecuentes

#### `configparser.ParsingError`

Revisar:

```bash
docker compose exec odoo bash -lc 'nl -ba /etc/odoo/odoo.conf'
```

Buscar lineas sin `=`.

#### `service odoo is not running`

```bash
docker compose ps
docker compose logs odoo
```

#### `/usr/bin/odoo` no existe

PyCharm esta intentando ejecutar Odoo localmente. Usar Docker Compose interpreter o ejecutar Odoo desde Docker.

#### El addon no aparece

```bash
docker compose exec odoo bash -lc 'ls -la /mnt/extra-addons'
```

Revisar `addons_path`, actualizar la lista de aplicaciones y actualizar el modulo.

#### `version is obsolete`

Es un aviso de Docker Compose moderno. Se puede quitar `version:` del YAML.

---

### Checklist para otra Mac

- [ ] Docker Desktop
- [ ] Homebrew
- [ ] Git
- [ ] Autenticacion GitHub
- [ ] `~/odoo16`
- [ ] `addons/`
- [ ] `config/`
- [ ] `docker-compose.yml`
- [ ] `odoo.conf`
- [ ] Repositorios clonados en `addons/`
- [ ] `docker compose up -d`
- [ ] `docker compose ps`
- [ ] Logs correctos
- [ ] `/mnt/extra-addons` visible
- [ ] Odoo en `http://localhost:8016`
- [ ] PyCharm configurado
- [ ] Base de datos restaurada/creada si corresponde

---

### Flujo diario recomendado

1. Abrir Docker Desktop.
2. `cd ~/odoo16`
3. `docker compose up -d`
4. Abrir el proyecto en PyCharm.
5. Editar modulos dentro de `addons/`.
6. Actualizar el modulo.
7. Revisar logs.
8. Probar en `http://localhost:8016`.
9. Hacer commit/push.
10. Al terminar, opcionalmente `docker compose down`.

---

### Tecnologias utilizadas

- Docker / Docker Compose
- Odoo 16.0
- PostgreSQL 15
- Python (ORM de Odoo, logica backend)
- XML / QWeb (vistas, reportes y PDFs)
- macOS (sistema anfitrion)
- Git / GitHub (control de versiones)
- PyCharm (IDE)
