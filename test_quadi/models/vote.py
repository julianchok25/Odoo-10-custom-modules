# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Vote(models.Model):
    _name = 'test_quadi.vote'

    name = fields.Char('Name', required=True)
    qualy = fields.Integer('Qualification')
    partner_id = fields.Many2one('res.partner', string='Person')
    date = fields.Datetime('Date', default=fields.Datetime.now())