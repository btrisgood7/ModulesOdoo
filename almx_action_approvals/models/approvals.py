from odoo import models, api, _

class ApprovalsRequest(models.Model):
    _inherit = 'approval.request'

    def approve(self):
        #===LOCALIZA A LOS USUARIOS===
        #CAMBIAR EN PRODUCCIÓN
        userApproval = self.env['res.users'].search([('id', '=', 6)], limit=1) #USUARIO DE: MARC DEMO
        userFollower = self.env['res.users'].search([('id', '=', 8)], limit=1) #USUARIO DE: DUVALIN EKCO
        
        for req in records:
            if req.create_uid == userApproval and userFollower and userFollower.partner_id:
                req.message_subscribe(partner_ids=[userFollower.partner_id.id])

            #create_approval = (req.create_uid.id == userApproval.id)
            #if hasattr(req, 'request_owner_id') and req.request_owner_id:


