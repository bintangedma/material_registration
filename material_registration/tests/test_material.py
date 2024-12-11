from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError, ValidationError

class TestMaterial(TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.supplier = self.env['material.supplier'].create({'name': 'Supplier 1'})
        self.material = self.env['material.material'].create({
            'material_code': 'MAT001',
            'name': 'Test Material',
            'material_type': 'fabric',
            'buy_price': 150,
            'supplier_id': self.supplier.id,
        })

    def test_create_material(self):
        material = self.env['material.material'].create({
            'material_code': 'MAT002',
            'name': 'New Material',
            'material_type': 'jeans',
            'buy_price': 200,
            'supplier_id': self.supplier.id,
        })
        self.assertEqual(material.name, 'New Material')

    def test_buy_price_constraint(self):
        with self.assertRaises(ValidationError):
            self.env['material.material'].create({
                'material_code': 'MAT003',
                'name': 'Invalid Material',
                'material_type': 'cotton',
                'buy_price': 50,
                'supplier_id': self.supplier.id,
            })