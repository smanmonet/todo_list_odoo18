from odoo import models, fields

class TodoList(models.Model):
    _name = 'todo.lists'
    _description = 'To Do List'

    title = fields.Char(
        string="Title", required=True)
    tags = fields.Many2many(
        'todo.tag', string="Tags")
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], default='draft')
    start_date = fields.Datetime(
        string="Start Date", required=True)
    end_date = fields.Datetime(
        string="End Date", required=True)
    
    name = fields.Char(
        string="Name")
    
    description = fields.Char(
        string="Description")
    
    is_complete = fields.Char(
        string="Is Complete")

    def action_start_progress(self):
        for rec in self:
            if rec.status != 'draft':
                return 'Can only start progress from Draft.'
            rec.status = 'in_progress'

    def action_mark_done(self):
        for rec in self:
            if rec.status != 'in_progress':
                return 'Can only mark done from In Progress.'
            rec.status = 'completed'
            
    def action_list(self):
        pass
    
    def action_attendee(self):
        pass