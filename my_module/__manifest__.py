{
 'name': 'My Custom Module',
 'version': '1.0',
 'summary': 'Simple module to demonstrate Odoo development',
 'author': 'Your Name',
 'depends': ['base'],
 'data': [
     'security/ir.model.access.csv',
     'views/my_model_views.xml',
 ],
 'installable': True,
 'application': True,
}
