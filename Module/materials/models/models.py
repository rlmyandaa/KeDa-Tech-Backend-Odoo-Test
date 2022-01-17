from odoo import models, fields, api


class materials(models.Model):
    _name = 'materials.materials'
    _description = 'materials.materials'

    material_code = fields.Char()
    material_name = fields.Char()
    material_type = fields.Selection([('Fabric','Fabric'),('Jeans','Jeans'),('Cotton','Cotton')],string="Material Type")
    material_buy_price = fields.Integer()
    material_supplier = fields.Many2one('materials.supplier', string="Supplier List")

    @api.onchange('material_buy_price')
    def _onchange_buy_price(self):
        if ((self.material_buy_price < 100 and self.material_buy_price > 0) or self.material_buy_price < 0) :
            self.material_buy_price = 100
            return {
                'warning': {'title': "Error", 'message': "Material Buy Price should at least 100"},
            }
        if (self.material_buy_price == 0) :
            self.material_buy_price = 100
            return {
                'warning': {'title': "Warning", 'message': "Material Buy Price can't be zero", 'type': 'notification'},
            }

class supplier(models.Model):
    _name = 'materials.supplier'
    _description = 'materials.supplier'

    supplier_name = fields.Char()
    _rec_name = 'supplier_name'