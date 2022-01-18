from odoo.tests import TransactionCase
from odoo.exceptions import ValidationError


class ConstrainTest(TransactionCase):
    def setUp(self):
        super(ConstrainTest, self).setUp()
        self.material_obj = self.env['materials.materials']
        self.supplier_obj = self.env['materials.supplier']

    # test required field with null field
    def test_throws_exception_for_null_required_fields(self):
        with self.assertRaises(ValidationError):
            self.material_obj.create({
                'material_name': 'testname',
                'material_type': 'Cotton',
                'material_buy_price': 10
            })

    # test buy price that doesn't meet constrain (<100)
    def test_throws_exception_for_buyprice_constrain(self):
        with self.assertRaises(ValidationError):
            supplier = self.supplier_obj.create({
                'supplier_name': 'Supplier1',
            })
            self.material_obj.create({
                'material_code': 'dassda',
                'material_name': 'testname',
                'material_type': 'Cotton',
                'material_buy_price': 10,
                'material_supplier': supplier.id
            })
