from odoo import models, fields, api


class Document(models.Model):
    _name = 'document.document'
    _description = 'Document Management'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    company_id = fields.Many2one('res.company', string='Company',
                                 default=lambda self: self.env.company)
    user_id = fields.Many2one('res.users', string='Created by',
                              default=lambda self: self.env.user, readonly=True)
    responsible_ids = fields.Many2many('hr.employee', string='Responsible Employees')

    # Additional useful fields
    create_date = fields.Datetime('Created on', readonly=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ], string='Status', default='draft')