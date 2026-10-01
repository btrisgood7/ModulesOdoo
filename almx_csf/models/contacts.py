from odoo import models, fields, api, _


class Contacts(models.Model):
    _inherit = 'res.partner'

    csf_document = fields.Binary(string='Constancia de situación fiscal')
    csf_document_filename = fields.Char(string='Nombre del archivo CSF')

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for record in records:
            if record.csf_document:
                record._log_csf_change(_("agregó"))
        return records

    def write(self, vals):
        if 'csf_document' not in vals:
            return super().write(vals)

        # Estado previo por registro
        previous = {rec.id: bool(rec.csf_document) for rec in self}
        res = super().write(vals)

        for rec in self:
            had_doc = previous.get(rec.id)
            has_doc = bool(rec.csf_document)
            if not had_doc and has_doc:
                rec._log_csf_change(_("agregó"))
            elif had_doc and not has_doc:
                rec._log_csf_change(_("eliminó"))
            elif had_doc and has_doc:
                rec._log_csf_change(_("modificó"))
        return res

    def _log_csf_change(self, action):
        filename = self.csf_document_filename or _("Constancia de situación fiscal")
        body = _("Se %s el documento CSF: %s") % (action, filename)
        self.message_post(body=body)
