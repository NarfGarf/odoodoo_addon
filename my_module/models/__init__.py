from . import my_model


file: models/my_model.py

from odoo import models, fields

class MyModel(models.Model):
 _name = 'my.model'
 _description = 'My Custom Model'

 name = fields.Char(string='Name', required=True)
 description = fields.Text(string='Description')
