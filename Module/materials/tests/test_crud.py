from odoo.tests import TransactionCase
from odoo.exceptions import ValidationError


class CrudTest(TransactionCase):
    def setUp(self):
        super(CrudTest, self).setUp()
        self.material_obj = self.env['materials.materials']
        self.supplier_obj = self.env['materials.supplier']

    # test if model exist
    def test_material_model_exist(self):
        self.assertTrue(self.material_obj._name in self.env)
        self.assertTrue(self.supplier_obj._name in self.env)

    def test_create_read_data(self):
        supplier = self.supplier_obj.create({
            'supplier_name': 'Supplier1',
        })
        material = self.material_obj.create({
            'material_code': '23sdaasd12',
            'material_name': 'testname',
            'material_type': 'Cotton',
            'material_buy_price': 120,
            'material_supplier': supplier.id
        })
        self.assertTrue(bool(self.material_obj.search(
            [('id', '=', material.id)], limit=1)))

    def test_edit_data(self):
        supplier = self.supplier_obj.create({
            'supplier_name': 'Supplier1',
        })
        material = self.material_obj.create({
            'material_code': '23sdaasd12',
            'material_name': 'testname',
            'material_type': 'Cotton',
            'material_buy_price': 120,
            'material_supplier': supplier.id
        })
        material.material_name = 'changedname'
        get = self.material_obj.browse(material.id)
        self.assertEqual(get.material_name, material.material_name)

    def test_delete_data(self):
        supplier = self.supplier_obj.create({
            'supplier_name': 'Supplier1',
        })
        material = self.material_obj.create({
            'material_code': '23sdaasd12',
            'material_name': 'testname',
            'material_type': 'Cotton',
            'material_buy_price': 120,
            'material_supplier': supplier.id
        })
        material_id = material.id
        material.unlink()
        self.assertFalse(bool(self.material_obj.search(
                    [('id', '=', material_id)], limit=1)))

