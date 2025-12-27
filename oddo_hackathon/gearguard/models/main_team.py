from odoo import models, fields

class GearGuardTeam(models.Model):
    _name = 'gearguard.team'
    _description = 'Maintenance Team'

    name = fields.Char(required=True)
    member_ids = fields.Many2many('res.users', string="Team Members")
