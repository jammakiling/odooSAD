from odoo import models, fields, api

class Category(models.Model):
    _name = "hcqinventory.category"
    _description = "HCQ Inventory Category"
    
    #fieldnames
    name = fields.Char(string='Item Category')
    description = fields.Char(string=' Category Description')
    