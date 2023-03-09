from odoo import api, fields, models 

class Produk(models.Model):
    _name = 'fashionstore.produk'
    _description = 'new description'

    name = fields.Char(string='Nama Barang')
    deskripsi = fields.Text(string='Deskripsi')
    jenis = fields.Selection(string='Jenis barang', selection=[('atasan', 'Atasan'), ('bawahan', 'Bawahan'), ('dress', 'Dress'), ('hijab','Hijab'),('gaun', 'Gaun'),
                                                               ('setelan','Setelan'),('hoddie','Hoddie'),('sweater','Sweater'), ('jaket','Jaket')])
    img = fields.Binary(string='Image')
    ukuran = fields.Selection(string='Ukuran', selection=[('s', 'S'), ('m', 'M'),('l','L'),('xl','XL'),('xxl','XXL'),('all size','All Size')])
    varian = fields.Selection(string='Varian Warna', selection=[('black','Black'), ('white','White'), ('light blue','Light Blue'),('daisy','Daisy'),
                                                                ('light pink','Light Pink'), ('maroon','Maroon'),('navy','Navy'), ('sport grey','Sport Grey'),
                                                                ('dark grey','Dark Grey'), ('silver','Silver'), ('coffe','Coffe'), ('browen','Browen'), ('green','Green'),
                                                                ('tosca','Tosca'), ('lavender','Lavender'),('purple','Purple'), ('nude','Nude'), ('avocado','Avocado'),
                                                                ('mint','Mint'), ('smoke','Smoke'), ('millo','Millo'), ('coksu','Coksu'), ('mocca','Mocca'), ('mustard','Mustard'),
                                                                ('all color','All Color')])
    bahan = fields.Char(string='Bahan')
    harga = fields.Integer(string='Harga')
    stok = fields.Integer(string='Stok')
    
    supplier = fields.Many2one(comodel_name='fashionstore.supplier', string='Supplier')

    penjualan_id = fields.Many2one(comodel_name='fashionstore.penjualandetail', string='Penjualan')