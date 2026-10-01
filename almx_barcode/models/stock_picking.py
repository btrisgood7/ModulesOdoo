from odoo import models

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def _get_stock_barcode_data(self):
        data = super(StockPicking, self)._get_stock_barcode_data()
        if 'config' not in data:
            data['config'] = {}

        data['config']['user_can_validate_barcode'] = self.env.user.has_group(
            'almx_barcode.group_barcode_allow_validate')

        return data

    #def _get_stock_barcode_data(self):
    #    data = super(StockPicking, self)._get_stock_barcode_data()
    #    data['user_can_validate_barcode'] = self.env.user.has_group('almx_barcode.group_barcode_allow_validate')

    #    return data