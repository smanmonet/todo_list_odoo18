from odoo import models, fields


class TodoDetails(models.Model):
    _name = "todo.details"
    _description = "Todo Details"

    name = fields.Char(string="Name", required=True)
    description = fields.Char(string="Description")
    is_complete = fields.Boolean(string="Is Complete")
    todo_list_id = fields.Many2one(
        "todo.lists",
        string="Todo List",
    )
