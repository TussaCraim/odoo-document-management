from odoo import models, fields, api


class DocumentReportWizard(models.TransientModel):
    _name = 'document.report.wizard'
    _description = 'Document Report Wizard'

    date_from = fields.Date(string='Date From', required=True)
    date_to = fields.Date(string='Date To', required=True)
    employee_id = fields.Many2one('hr.employee', string='Employee')

    def action_print_report(self):
        domain = [
            ('create_date', '>=', self.date_from),
            ('create_date', '<=', self.date_to),
        ]
        if self.employee_id:
            domain.append(('responsible_ids', 'in', [self.employee_id.id]))

        documents = self.env['document.document'].search(domain)

        return {
            'name': 'Documents Report',
            'type': 'ir.actions.act_window',
            'res_model': 'document.document',
            'view_mode': 'tree,form',
            'domain': domain,
            'target': 'current',
        }