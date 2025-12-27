from odoo import models, fields

class GearGuardRequest(models.Model):
    _name = 'gearguard.request'
    _description = 'Maintenance Request'

    name = fields.Char(string="Issue", required=True)
    equipment_id = fields.Many2one('gearguard.equipment', required=True)
    team_id = fields.Many2one('gearguard.team')
    technician_id = fields.Many2one('res.users')

    request_type = fields.Selection([
        ('corrective', 'Corrective'),
        ('preventive', 'Preventive')
    ], default='corrective')

    stage = fields.Selection([
        ('new', 'New'),
        ('progress', 'In Progress'),
        ('done', 'Done')
    ], default='new')

    scheduled_date = fields.Date()
