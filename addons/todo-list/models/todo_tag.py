from odoo import models, fields


class TodoTag(models.Model):
    _name = "todo.tag"
    _description = "Todo Tags"

    name = fields.Char(string="Name", required=True)
