from odoo import models, fields, api
from odoo.exceptions import ValidationError
class TodoList(models.Model):
    _name = "todo.lists"
    _description = "To Do List"
    _rec_name = "title"

    title = fields.Char(string="Title", required=True)
    tags = fields.Many2many("todo.tag", string="Tags")
    status = fields.Selection(
        [
            ("draft", "DRAFT"),
            ("in_progress", "IN PROGRESS"),
            ("complete", "COMPLETE"),
        ],
        default="draft",
    )
    start_date = fields.Datetime(string="Start Date", required=True)
    end_date = fields.Datetime(string="End Date", required=True)
    details_ids = fields.One2many(
        "todo.details",
        "todo_list_id",
        string="Program",
    )
    user_id = fields.Many2many("res.users", string="Attendee")
    check_completed = fields.Boolean(
        string="Is Complete", compute="all_details_completed"
    )

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for rec in self:
            if rec.start_date and rec.end_date and rec.end_date < rec.start_date:
                raise ValidationError("End Date must be greater than or equal to Start Date.")
    def action_start_progress(self):
        for record in self:
            record.status = "in_progress"

    def action_mark_done(self):
        for record in self:
            record.status = "complete"

    @api.onchange("details_ids.is_complete")
    def all_details_completed(self):
        if not self.details_ids:
            self.check_completed = False
        else:
            for record in self:
                if all(details.is_complete for details in record.details_ids):
                    record.check_completed = True
                else:
                    record.check_completed = False
