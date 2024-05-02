from odoo import models, fields, api

class Item(models.Model):
    _name = "hcqinventory.item"
    _description = "HCQ Inventory Item"
    
    #fieldnames
    name = fields.Char(string='Item Name')
    code =fields.Char(string='Item Code')
    category_id= fields.Many2one('hcqinventory.category', string="Category")
    brand_id= fields.Many2one('hcqinventory.brand', string="Brand")
    price1= fields.Float(string='Price A')
    price2= fields.Float(string='Price B')
    price3= fields.Float(string='Price C')
    price4= fields.Float(string='Price D')
    quantity=fields.Integer(string="Quantity")