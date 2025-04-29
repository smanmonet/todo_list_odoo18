{
    'name': 'Todo List',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'A custom module for specific needs',
    'description': """This module is for...""",
    'author': 'SMAN',
    'website': 'http://www.example.com/',
    'depends': ['base'],
    'data': [
        'views/todo_view.xml',  
        'views/todo_menus.xml',
        'data/todo_tag_data.xml',
        'security/ir.model.access.csv',  
    ],
    'installable': True,
    'application': True,
}                    