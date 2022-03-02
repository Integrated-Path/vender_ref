from email.policy import default
from fnmatch import translate
from odoo import models, fields, api


class sales(models.Model):
  _inherit = "sales.model"
  _description ="test the inherited properity "
  sale_description = fields.Char(string="sales desc" )

  

  
