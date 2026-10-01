from odoo import models, fields, api

class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    start_date = fields.Datetime(string='Fecha de inicio programada', tracking=True)
    effective_date = fields.Datetime(string='Fecha de efectiva de termino', tracking=True)
    end_date = fields.Datetime(string='Fecha de fin', tracking=True)