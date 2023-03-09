from odoo import api, fields, models 

class Pembayaran(models.Model):
    _name = 'fashionstore.pembayaran'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    metode = fields.Selection(string='Metode', selection=[('transfer', 'Transfer'), ('cash', 'Cash'),('rekening','Rekening'),('debet','Debet'),])

    
