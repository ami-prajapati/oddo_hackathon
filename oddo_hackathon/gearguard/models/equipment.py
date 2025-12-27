from odoo import models, fields

class GearGuardEquipment(models.Model):
    _name = 'gearguard.equipment'
    _description = 'Equipment'

    name = fields.Char(string="Equipment Name", required=True)
    serial_number = fields.Char(string="Serial Number")
    department = fields.Char(string="Department")
    location = fields.Char(string="Location")

    purchase_date = fields.Date(string="Purchase Date")
    warranty_end = fields.Date(string="Warranty End Date")

    is_scrap = fields.Boolean(string="Is Scrap", default=False)
