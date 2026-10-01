from odoo import models, fields, api
from odoo.exceptions import AccessError


class HrLeave(models.Model):
    _inherit = 'hr.leave'

    # Campo computado para controlar si la descripción es editable
    description_readonly = fields.Boolean(
        string='Descripción bloqueada',
        compute='_compute_description_readonly',
    )

    @api.depends('state')
    def _compute_description_readonly(self):
        """
        La descripción es editable si:
          1. El registro es nuevo (state == 'draft' o 'confirm') Y
             el usuario NO tiene el grupo 'Puede editar descripción'.
          2. El usuario SÍ tiene el grupo 'Puede editar descripción',
             siempre puede editar.
        """
        can_edit_group = self.env.ref(
            'hr_leave_description_lock.group_leave_description_editor',
            raise_if_not_found=False,
        )
        user_can_edit = can_edit_group and (can_edit_group in self.env.user.groups_id)

        for leave in self:
            if user_can_edit:
                leave.description_readonly = False
            else:
                # Bloqueado si ya no está en borrador/confirmado
                leave.description_readonly = leave.state not in ('draft', 'confirm')
#Validación adicional cuando alguien quiera editar después de haberla confirmado.
    def write(self, vals):
        if 'private_note' in vals or 'notes' in vals:
            can_edit_group = self.env.ref(
                'hr_leave_description_lock.group_leave_description_editor',
                raise_if_not_found=False,
            )
            user_can_edit = can_edit_group and (can_edit_group in self.env.user.groups_id)

            if not user_can_edit:
                locked = self.filtered(lambda l: l.state not in ('draft', 'confirm'))
                if locked:
                    raise AccessError(
                        'No tienes permiso para editar la descripción de una '
                        'ausencia que ya ha sido confirmada o validada.'
                    )
        return super().write(vals)