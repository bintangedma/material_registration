from odoo import http
from odoo.http import request, json

class MaterialController(http.Controller):
    
    @http.route('/api/materials', type='json', auth='user', methods=['GET'])
    def get_materials(self):
        material_type = json.loads(request.httprequest.data.decode('utf-8')).get('material_type')
        domain = []
        if material_type:
            domain.append(('material_type', '=', material_type))
        materials = request.env['material.material'].search(domain)
        return materials.read(['material_code', 'name', 'material_type', 'buy_price', 'supplier_id'])
    
    @http.route('/api/materials', type='json', auth='user', methods=['POST'])
    def create_material(self, **kwargs):
        request_data = json.loads(request.httprequest.data.decode('utf-8'))
        data = request.env['material.material'].search([('material_code', '=', request_data.get('material_code'))])
        if data : 
            return {"error" : f"Code : {request_data.get('material_code')} is already exist!"}
        required_fields = ['material_code', 'name', 'material_type', 'buy_price', 'supplier_id']
        missing_fields = [field for field in required_fields if field not in request_data]
        if missing_fields:
            return {"error": f"Missing fields: {', '.join(missing_fields)}"}
    
        if request_data.get('buy_price', 0) < 100:
            return {"error": "Buy price must be 100 or higher"}
        material = request.env['material.material'].create(request_data)
        return {"message": "Material created successfully", "id": material.id}

    @http.route('/api/materials/<int:material_id>', type='json', auth='user', methods=['PUT'])
    def update_material(self, material_id, **kwargs):
        request_data = json.loads(request.httprequest.data.decode('utf-8'))
        material = request.env['material.material'].browse(material_id)
        if not material.exists():
            return {"error": "Material not found"}
        material.write(request_data)
        return {"message": "Material updated successfully"}
    
    @http.route('/api/materials/<int:material_id>', type='json', auth='user', methods=['DELETE'])
    def delete_material(self, material_id):
        material = request.env['material.material'].browse(material_id)
        if not material.exists():
            return {"error": "Material not found"}
        material.unlink()
        return {"message": "Material deleted successfully"}