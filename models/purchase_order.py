
from odoo import models, fields

class PurchaseOrder(models.Model):
  _inherit = "purchase.order"
  partner_ref = fields.Char('Vendor Reference', required=True)
  _sql_constraints = [
        ('partner_ref_uniq', 'unique(partner_ref)', "Vendor Reference duplicated !"),
    ]
     