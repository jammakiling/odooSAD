from odoo import models, fields, api

class Brand(models.Model):
    _name = "hcqinventory.brand"
    _description = "HCQ Inventory Brand"
    
    #fieldnames
    name = fields.Char(string='Item Brand')
    description = fields.Char(string=' Brand Description')
    