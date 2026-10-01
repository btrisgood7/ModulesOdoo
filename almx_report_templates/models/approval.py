from odoo import models, fields, api

#Aquí estoy creando mi one2many llamado approval.loan
class ApprovalLoan(models.Model):
    _name = 'approval.loan'
    _description = 'Loan Approval'

    # inverso al one2many
    request_id = fields.Many2one('approval.request', string='Solicitud de prestamo', ondelete='cascade', index=True)
    category_id = fields.Char(string="Categoria del equipo")
    model_id = fields.Char(string="Modelo del equipo")
    serial_number = fields.Char(string="Número de serie del equipo")

