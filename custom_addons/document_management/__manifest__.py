{
    'name': 'Document Management',
    'version': '13.0.1.0.0',
    'category': 'Document Management',
    'author': 'Your Name',
    'summary': 'Module for managing documents and books',
    'description': """
        This module allows to:
        * Store documents/books information
        * Assign responsible employees
        * Filter documents by date and employee
    """,
    'depends': [
        'base',  # basic module
        'hr',    # module for working with employees
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/document_views.xml',
        'wizards/document_report_wizard.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}