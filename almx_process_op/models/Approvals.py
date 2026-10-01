from odoo import models, fields, api
from odoo.exceptions import UserError

class ProcessApproval(models.Model):
    _inherit = "approval.request"

    in_process_request = fields.Boolean(string='Solicitud dentro del proceso', tracking=True)
    out_process_request = fields.Boolean(string='Solicitud fuera del proceso', tracking=True)
    process_reason = fields.Text(string='Motivo si salió de proceso', tracking=True)