import logging
import requests
from odoo import models

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super().action_confirm()
        for order in self:
            try:
                order._send_whapi_test_message()
            except Exception as e:
                _logger.exception("Error WHAPI para %s: %s", order.name, e)
        return res

    def _send_whapi_test_message(self):
        self.ensure_one()

        token = "e3j5T58xrmMCsdgo0aRjvtBYo74RCgGW"      
        base_url = "https://gate.whapi.cloud/"

        phone = "5215650881182"  # formato internacional SIN '+'
        message = f"Hola! Prueba WHAPI desde Odoo. Orden: {self.name}"

        url = f"{base_url}/messages/text"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        payload = {
            "to": phone,
            "body": message,
        }

        resp = requests.post(url, json=payload, headers=headers, timeout=30)

        if resp.status_code not in (200, 201):
            _logger.error("WHAPI ERROR %s: %s", resp.status_code, resp.text)
        else:
            _logger.info("WHAPI OK: %s", resp.text)
