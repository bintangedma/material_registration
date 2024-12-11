This application uses Odoo 14.

ERD of the application is in the following :

Material
--------
- id (PK)
- material_code (Unique)
- name
- material_type (Enum: Fabric, Jeans, Cotton)
- buy_price (>= 100)
- supplier_id (FK -> res.partner)

Material entity has 6 attributes which are id, material_code, name, material_type, buy_price, and supplier_id.

material_code is designed uniquely to define the code of the material and can't be created if the same code exists in the database.
material_type only limited to 3 choices, which are Fabric, Jeans, and Cotton.
buy_price can not be less than 100.
supplier_id is related to res.partner, an odoo module which often used for suppliers.
