from odoo import api, fields, models
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    entry_number = fields.Char(
        string="Número de pedimento",
        copy=False,
        help="Captura el número de pedimento. Solo permitido en recepciones directas de Orden de Compra.",
        tracking=True,
    )

    @api.constrains("entry_number", "picking_type_id", "purchase_id")
    def _check_entry_number_po_context(self):
        """
        Valida que el pedimento solo se capture si:
        1. Es una operación de Entrada (Incoming).
        2. Proviene directamente de una Orden de Compra (purchase_id).
        """
        for rec in self:
            # Si el campo está vacío, permitimos el flujo normal (no bloqueamos devoluciones ni otros movimientos)
            if not rec.entry_number:
                continue

            # 1. Validamos que sea físicamente una entrada (code='incoming' es más seguro que sequence_code)
            is_incoming = rec.picking_type_id.code == 'incoming'

            # 2. Validamos que exista un vínculo con una Orden de Compra
            # Las devoluciones de clientes o ajustes de inventario NO tienen este campo set.
            is_from_po = bool(rec.purchase_id)

            if not is_incoming:
                raise ValidationError("El número de pedimento solo aplica para movimientos de entrada (IN).")

            if not is_from_po:
                raise ValidationError(
                    "El número de pedimento solo puede asignarse a recepciones ligadas directamente a una Orden de Compra.\n"
                    "Este movimiento parece ser una devolución, ajuste o transferencia sin PO asociada."
                )
