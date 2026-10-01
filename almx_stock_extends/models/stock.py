# -*- coding: utf-8 -*-
import base64
from odoo import api, fields, models, SUPERUSER_ID
from odoo import models, fields, api, _
from odoo.exceptions import Warning, ValidationError, UserError
from datetime import date
from datetime import datetime
from io import StringIO, BytesIO
import logging
import json
import requests
from odoo.tools.populate import compute


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    not_validate = fields.Boolean(string='No se puede validar', help='Muestra si la condición de pagado aplica para la orden de venta relacionada al movimiento de almacén actual')#, compute='compute_spare_sale_order')
    detect_move_type = fields.Boolean(string='Tipo de movimiento', compute='compute_picking_type_move')
    pick_move = fields.Boolean(string='Es un PICK')
    out_move = fields.Boolean(string='Es un OUT')
    in_move = fields.Boolean(string='Es un IN')

    @api.depends('picking_type_id.sequence_code')
    def compute_picking_type_move(self):
        for rec in self:
            sequence_code = rec.picking_type_id.sequence_code
            move_flags = {
                'PICK': 'pick_move',
                'OUT': 'out_move',
                'IN': 'in_move',
            }

            rec.pick_move = rec.out_move = rec.in_move = False

            move_attr = move_flags.get(sequence_code)
            if move_attr:
                setattr(rec, move_attr, True)
                rec.detect_move_type = True
            else:
                rec.detect_move_type = False

    def compute_spare_sale_order(self):
        op_type = self.picking_type_id.id
        sale_type = self.x_studio_tipo_de_venta
        comp_paid = self.x_studio_completamente_pagado
        if sale_type == 'spare' and comp_paid != True and op_type == 2: #Aplica solo para movimientos que son OUT
            self.not_validate = True
        else:
            self.not_validate = False

    def action_set_to_draft(self):
        if self.state not in ('draft', 'done'):
            self.action_clear_quantities_to_zero()
            self.do_unreserve()
            move = self.env['stock.move'].search([('picking_id', '=', self.id)])
            for each in move:
                each.state = 'draft'
            self.state = 'draft'

    def action_create_related_out(self):
        self.ensure_one()

        if self.state != 'done':
            raise UserError(_('Solo puedes crear un OUT desde un PICK ya validado.'))

        # Buscar tipo de operación OUT del mismo almacén
        picking_type_out = self.env['stock.picking.type'].sudo().search([
            ('code', '=', 'outgoing'),
            ('warehouse_id', '=', self.picking_type_id.warehouse_id.id)
        ], limit=1)

        if not picking_type_out:
            raise UserError(_('No se encontró un tipo de operación de salida (OUT) para este almacén.'))

        # Clonar el picking actual con todos sus movimientos
        picking_out = self.sudo().copy({
            'picking_type_id': picking_type_out.id,
            # El OUT normalmente sale desde donde terminó el PICK
            'location_id': self.location_dest_id.id,
            'location_dest_id': picking_type_out.default_location_dest_id.id or self.location_dest_id.id,
            'state': 'draft',
            # Para que sepas de dónde viene
            'origin': (self.origin or self.name or '') + ' - OUT',
        })

        return {
            'type': 'ir.actions.act_window',
            'name': _('Salida Generada'),
            'res_model': 'stock.picking',
            'res_id': picking_out.id,
            'view_mode': 'form',
            'target': 'current',
        }

    def action_create_related_int(self):
        self.ensure_one()

        if self.state != 'done':
            raise UserError(_('Solo puedes crear un INT desde un PICK ya validado.'))

        # Buscar tipo de operación INTERNAL del mismo almacén
        picking_type_int = self.env['stock.picking.type'].sudo().search([
            ('code', '=', 'internal'),
            ('warehouse_id', '=', self.picking_type_id.warehouse_id.id)
        ], limit=1)

        if not picking_type_int:
            raise UserError(_('No se encontró un tipo de operación interna (INT) para este almacén.'))

        # Clonar el picking actual con todos sus movimientos
        picking_int = self.sudo().copy({
            'picking_type_id': picking_type_int.id,
            'location_id': self.location_dest_id.id,
            'location_dest_id': picking_type_int.default_location_dest_id.id or self.location_dest_id.id,
            'state': 'draft',
            'origin': (self.origin or self.name or '') + ' - INT',
        })

        return {
            'type': 'ir.actions.act_window',
            'name': _('Transferencia Generada'),
            'res_model': 'stock.picking',
            'res_id': picking_int.id,
            'view_mode': 'form',
            'target': 'current',
        }

