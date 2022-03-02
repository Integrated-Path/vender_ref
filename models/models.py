from email.policy import default
from fnmatch import translate
from odoo import models, fields, api


class expensess(models.Model):
  _name = "expensess.model"
  _description ="calculate the store expensess "
  employee_name = fields.Char(default="jun",string='name' )
  new_expensses = fields.Integer(default="0")
  month = fields.Selection([
    ('jan','January'  ),
     ('feb','Febreuary'  ),
      ('mar','March'  ),
      ('mar','March'  ),
      ('mar','March'  ),
  ] , reqirued=True , default='jan'  )


  
