from odoo import models, fields
from odoo.exceptions import UserError

class TodoList(models.Model):
    _name = 'to.do.list'
    _description = 'To Do List'

    title = fields.Char(string="Title", required=True)
    tags = fields.Many2many('todo.tag', string="Tags")
    
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], default='draft')
    
    start_date = fields.Datetime(string="Start Date", required=True)
    end_date = fields.Datetime(string="End Date", required=True)

    def action_start_progress(self):
        for rec in self:
            if rec.status != 'draft':
                raise UserError(_('Can only start progress from Draft.'))
            rec.status = 'in_progress'

    def action_mark_done(self):
        for rec in self:
            if rec.status != 'in_progress':
                raise UserError(_('Can only mark done from In Progress.'))
            rec.status = 'completed'

class TodoTag(models.Model):
    _name = 'todo.tag'
    _description = 'Todo Tags'

    name = fields.Char(string='Name', required=True)