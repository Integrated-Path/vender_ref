
from odoo import models, fields

# TODO: It is recommended that the each file has an indetation of at least  4 spaces for ease of read (tabs are recommended 🙂)
class PurchaseOrder(models.Model):
  _inherit = "purchase.order"
  partner_ref = fields.Char('Vendor Reference', required=True)
  _sql_constraints = [
        ('partner_ref_uniq', 'unique(partner_ref)', "Vendor Reference duplicated !"),
    ]
     