{
    'name': 'GearGuard - Maintenance Management',
    'version': '1.0',
    'summary': 'Equipment and Maintenance Tracking System',
    'description': """
GearGuard is an Odoo module built for hackathon purposes.
It helps organizations manage equipment, maintenance teams,
and corrective/preventive maintenance requests using
a simple workflow and clean UI.
    """,

    'author': 'Odoo Hackathon Team',
    'category': 'Operations/Maintenance',

    'depends': ['base'],

    'data': [
    'security/ir.model.access.csv',
    'views/equipment_views.xml',
    'views/main_req_form.xml',
    'views/main_req_kanban.xml',
    'views/main_cal.xml',
    ],
    'installable': True,
    'application': True,
}
