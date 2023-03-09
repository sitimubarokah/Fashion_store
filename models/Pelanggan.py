from odoo import api, fields, models 

class Pelanggan(models.Model):
    _name = 'fashionstore.pelanggan'
    _description = 'New Description'

    name = fields.Char(string='Nama Pelanggan')
    jenkel = fields.Selection(string='Jenis Kelamin', selection=[('laki-laki', 'Laki-laki'), ('perempuan', 'Perempuan')])
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='Telephone')
    pelanggan_ids = fields.One2many(
        comodel_name='fashionstore.penjualan', 
        inverse_name='pelanggan_id', 
        string='Pelanggan')
    

    