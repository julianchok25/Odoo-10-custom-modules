# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Vote(models.Model):
    _name = 'test_quadi.vote'

    idea_id = fields.Many2one('test_quadi.idea', string='Idea')
    qualy = fields.Integer('Qualification')
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.uid, \
        domain=[('partner_id.is_company','=',False)])
    date = fields.Datetime('Date', default=fields.Datetime.now(), readonly=True)
    active_c = fields.Boolean('Active', default=True)

    @api.constrains('qualy')
    def _check_qualy(self):
        for record in self:
            if record.qualy > 10:
                raise exceptions.ValidationError("It can only be from 0 to 10: %s" % record.qualy)
            elif record.qualy < 0:
                raise exceptions.ValidationError("It can only be from 0 to 10: %s" % record.qualy)