from odoo import models, fields, api

class Sale(models.Model):
    _name = "hcqinventory.sale"
    _description = "HCQ Inventory Sale"
    
    #fieldnames
    name = fields.Char(string='Sale Code')
    saleorder_line_ids=fields.One2many('hcqinventory.saleorder', 'item_id' , string = "Sale Order Lines")
    
    
class SaleOrder(models.Model):
    _name = 'hcqinventory.saleorder'
    _description = 'HCQ Inventory Sale Order'
    
    item_id= fields.Many2one('hcqinventory.item', string="Item")
    itemcode=fields.Char(related='item_id.code')
    itemprice=fields.Float(related='item_id.price1')
    quantity=fields.Integer(string="Quantity")
    