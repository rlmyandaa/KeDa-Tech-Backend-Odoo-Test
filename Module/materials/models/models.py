from odoo import models, fields, api
from odoo.exceptions import ValidationError


class materials(models.Model):
    _name = 'materials.materials'
    _description = 'materials.materials'

    material_code = fields.Char()
    material_name = fields.Char()
    material_type = fields.Selection(
        [('Fabric', 'Fabric'), ('Jeans', 'Jeans'), ('Cotton', 'Cotton')], string="Material Type", )
    material_buy_price = fields.Integer()
    material_supplier = fields.Many2one(
        'materials.supplier', string="Supplier List", )

    # Constrains
    @api.constrains('material_buy_price')
    def constrain_buy_price(self):
        if self and self.material_buy_price < 100:
            raise ValidationError('Material Buy Price should at least 100.')

    @api.constrains('material_code')
    def constrain_material_code(self):
        if not (self.material_code):
            raise ValidationError('Material Code should not empty.')

    @api.constrains('material_name')
    def constrain_material_name(self):
        if not (self.material_name):
            raise ValidationError('Material Name should not empty.')

    @api.constrains('material_type')
    def constrain_material_type(self):
        if not (self.material_type):
            raise ValidationError('Material Type should not empty.')

    @api.constrains('material_supplier')
    def constrain_material_supplier(self):
        if not (self.material_supplier):
            raise ValidationError('Material Supplier should not empty.')


class supplier(models.Model):
    _name = 'materials.supplier'
    _description = 'materials.supplier'

    supplier_name = fields.Char()
    _rec_name = 'supplier_name'

    @api.constrains('supplier_name')
    def constrain_supplier_name(self):
        if not (self.supplier_name):
            raise ValidationError('Supplier Name should not empty.')
