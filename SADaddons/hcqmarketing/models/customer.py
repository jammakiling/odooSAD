from odoo import models, fields, api

class Customer(models.Model):
    _name = "hcqinventory.customer"
    _description = "HCQ Inventory Customer"
    
    #fieldnames
    name = fields.Char(string='Customer Name')
    address = fields.Char(string='Customer Address')
    contactname = fields.Char(string='Contact Person')
    owner = fields.Char(string='Owner Name')
    contact1= fields.Char(string='Contact A')
    contact2= fields.Char(string='Contact B')
    contact3= fields.Char(string='Contact C')
    TIN= fields.Char(string='TIN number')
    