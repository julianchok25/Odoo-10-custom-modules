# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api

class Idea(models.Model):
    _name = 'test_quadi.idea'

    name = fields.Char('Name', required=True)
    group = fields.Selection([
        ('grp1','Group 1'),
        ('grp2','Group 2'),
        ('grp3','Group 3'),
        ], default='grp1', string='Group')
    description = fields.Text('Description')
    vote = fields.Integer('Votes')
    qualy = fields.Float(compute="_compute_vote", store=True)
    start_date = fields.Datetime('Start date', default=fields.Datetime.now(), \
        domain="[('create_uid','=',user.id)]")
    end_date = fields.Datetime('End date', compute='_get_end_date', readonly=True)
    user_id = fields.Many2one('res.users', string='Owner', default=lambda self: self.env.uid)

    @api.depends('vote')
    def _compute_vote(self):
        self.qualy = float(self.vote) / 100

    @api.one
    @api.depends('start_date')
    def _get_end_date(self):
        if self.start_date:
            try:
                start = fields.Datetime.from_string(self.start_date)
                duration = timedelta(days=30)
                self.end_date = (start + duration)
            except:
                pass