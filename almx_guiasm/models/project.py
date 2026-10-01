from odoo import models, fields, api, _


class ProjectTask(models.Model):
    _inherit = "project.task"

    # operations_firmed = fields.Char(string="GMD Firma de operaciones", tracking=True)
    # approved_by_client = fields.Binary(string="Aprobado por el cliente", tracking=True)
    format_finally = fields.Binary(string="Formatos Acabados")
    # Campo tecnico OCULTO: Odoo solo puede capturar el nombre real del
    # archivo a traves de un campo compañero del Binary. No se muestra en
    # la vista; el usuario solo interactua con 'format_finally'.
    format_finally_filename = fields.Char()

    def _log_format_finally(self, action, filename):
        """Registra en el chatter la accion realizada sobre el archivo."""
        name = filename or _("archivo")
        for task in self:
            task.message_post(
                body=_('<b>Formatos Acabados</b>: archivo %s "%s".') % (action, name)
            )

    @api.model_create_multi
    def create(self, vals_list):
        tasks = super().create(vals_list)
        for task in tasks:
            if task.format_finally:
                task._log_format_finally(_("subido"), task.format_finally_filename)
        return tasks

    def write(self, vals):
        logs = []
        if "format_finally" in vals:
            new = vals.get("format_finally")
            for task in self:
                old = task.format_finally
                old_name = task.format_finally_filename
                new_name = vals.get("format_finally_filename") or old_name
                if new and not old:
                    logs.append((task.id, _("subido"), new_name))
                elif new and old:
                    logs.append((task.id, _("modificado"), new_name))
                elif old and not new:
                    logs.append((task.id, _("eliminado"), old_name))

        res = super().write(vals)

        for task_id, action, name in logs:
            self.browse(task_id)._log_format_finally(action, name)
        return res
