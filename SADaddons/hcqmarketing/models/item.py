from odoo import models, fields, api

class Item(models.Model):
    _name = "hcqinventory.item"
    _description = "HCQ Inventory Item"
    
    #fieldnames
    name = fields.Char(string='Item Name')
    description = fields.Char(string=' Item Description')
    size= fields.Integer(string='Size')
    price= fields.Integer(string='Price')
    color = fields.Char(string='Color')