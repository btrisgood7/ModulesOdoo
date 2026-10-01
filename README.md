<h1> Módulos personalizados para la versión de 16 de Odoo. </h1>

### Rama v16
Este rama contiene la instalación de odoo 16 para Windows y Macos con Pycharm, al igual que módulos personalizados para esta versión de odoo.

## Instalación
1. Clonar el repositorio:
```bash
   git clone https://github.com/btrisgood7/ModulesOdoo.git
   git checkout v16
```
2. Instalar las dependencias de Python:
```bash
   pip install -r requirements.txt
```

3. Agregar la carpeta de módulos personalizados al `addons_path` en el archivo de configuración de Odoo.

4. Reiniciar el servidor de Odoo y activar los módulos desde el menú de Aplicaciones.

### Estructura de los modulos
```text
ModulesOdoo/
|
|-- module_name_1/
|   |-- __manifest__.py
|   |-- __init__.py
|   |-- models/
|   |-- views/
|   |-- security/
|   |-- data/
|   `-- static/
|
|-- module_name_2/
|   `-- ...

```
📧 celiahdza0709@gmail.com | 
🔗 [LinkedIn](https://www.linkedin.com/in/celia-hernández-501b2a30a?utm_source=share_via&utm_content=profile&utm_medium=member_ios) 

