from odoo import api, fields, models 

class Partner(models.Model):
    _name = 'fashionstore.partner'
    _description = 'human description'

    name = fields.Char(string='Name')
    alamat = fields.Char(string='Alamat')

class Pegawai(models.Model):
    _inherit = 'fashionstore.partner'
    _name = 'fashionstore.pegawai'
    
    name = fields.Char(string='Nama')
    jabatan = fields.Char(string='Jabatan')
    jenkel = fields.Selection(string='Jenis Kelamin', selection=[('perempuan', 'Perempuan'), ('laki-laki', 'Laki-laki')])
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    status = fields.Boolean(string='Sudah Menikah', default=False)
    no_telp = fields.Char(string='Nomor Telepon')
    alamat = fields.Char(string='Alamat')
    gaji = fields.Integer(string='Gaji Pokok')
    
    
    