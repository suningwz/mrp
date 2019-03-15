# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)


class ProcurementRule(models.Model):
    _inherit = 'procurement.rule'

    @api.multi
    def _run_manufacture(self, product_id, product_qty, product_uom, location_id, name, origin, values):
        result = super(ProcurementRule, self)._run_manufacture(product_id, product_qty, product_uom, location_id, name, origin, values)
        self.env['procurement.group'].run_scheduler()
        if not result:
            raise exceptions.UserError("Error creating Manufacturing Order")
        return result
