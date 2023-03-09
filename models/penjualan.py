from odoo import api, fields, models 

class Penjualan(models.Model):
    _name = 'fashionstore.penjualan'
    _description = 'New Description'

    pelanggan_id = fields.Many2one(comodel_name='fashionstore.pelanggan', string='Pelanggan')
    tanggal = fields.Datetime(string='Tanggal Pesan', default=fields.Datetime.now)

    produk_ids = fields.One2many (comodel_name = 'fashionstore.penjualandetail' , 
                                  inverse_name = 'penjualan_id' , 
                                  string='produk')

    ttl_bayar = fields.Integer(compute= '_compute_ttl_bayar', string='Total Bayar', store=True)

    metode = fields.Selection(string='Metode', selection=[('e-wallet', 'E-wallet'), ('cash', 'Cash'),('rekening','Rekening'),('debet','Debet')])

    @api.depends('produk_ids')
    def _compute_ttl_bayar(self):
        for record in self:
            a = sum(self.env['fashionstore.penjualandetail'].search([('penjualan_id','=', record.id)]).mapped('harga'))
            b = sum(self.env['fashionstore.produk'].search([('penjualan_id', '=', record.id)]).mapped('harga'))
            record.ttl_bayar = a + b

    sudah_bayar = fields.Boolean(string='Sudah Bayar', default=False)
    

class Penjualan_detail(models.Model):
    _name = 'fashionstore.penjualandetail'
    _description = 'New Description'

    produk_id = fields.Many2one(comodel_name='fashionstore.produk', string='Produknya')
    penjualan_id = fields.Many2one(comodel_name='fashionstore.penjualan', string='Penjualan')
    
    name = fields.Char(string='Nama Barang')
    harga = fields.Integer(compute='_compute_harga', string='Harga')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga Satuan')

    @api.depends('produk_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.produk_id.harga

    qty = fields.Integer(string='Quantity')

    @api.depends('qty','harga_satuan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.harga_satuan * record.qty

    @api.model
    def create(self,vals):
        record = super(Penjualan_detail, self).create(vals) 
        if record.qty:
            self.env['fashionstore.produk'].search([('id','=',record.produk_id.id)]).write({'stok':record.produk_id.stok-record.qty})
            return record

    