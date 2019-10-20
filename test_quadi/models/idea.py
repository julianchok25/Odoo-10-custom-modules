# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Idea(models.Model):
    _name = 'test_quadi.idea'

    name = fields.Char('Name', required=True)
    group = fields.Char('Group')
    description = fields.Text('Description')
    vote = fields.Integer('Votes')
    qualy = fields.Float(compute="_compute_vote", store=True)

    @api.depends('vote')
    def _compute_vote(self):
        self.qualy = float(self.vote) / 100