from odoo import api, fields, models 

class Supplier(models.Model):
    _name = 'fashionstore.supplier'
    _description = 'new description'

    name = fields.Char(string='Nama Perusahaan')    
    alamat = fields.Char(string='Alamat')
    cp = fields.Char(string='Contact Person')
    telp = fields.Char(string='Nomor Telepon')
    produk_ids = fields.One2many(comodel_name='fashionstore.produk', 
                 inverse_name='supplier', 
                 string='Barangnya')
    

                    