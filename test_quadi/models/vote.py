# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Vote(models.Model):
    _name = 'test_quadi.vote'

    idea_id = fields.Many2one('test_quadi.idea', string='Idea')
    name = fields.Char(related='idea_id.name', readonly=True, store=True)
    qualy = fields.Integer('Qualification')
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.uid, \
        domain=[('partner_id.is_company','=',False)])
    date = fields.Datetime('Date', default=fields.Datetime.now(), readonly=True)
    active_c = fields.Boolean('Active', default=True)
    # getting date from idea model
    idea_end_date = fields.Datetime(related='idea_id.end_date', readonly=True, store=True)

    @api.constrains('qualy')
    def _check_qualy(self):
        for record in self:
            if record.qualy > 10:
                raise exceptions.ValidationError("It can only be from 0 to 10: %s" % record.qualy)
            elif record.qualy < 0:
                raise exceptions.ValidationError("It can only be from 0 to 10: %s" % record.qualy)

    @api.multi
    @api.constrains('idea_end_date', 'date')
    def _check_date_idea(self):
        for record in self:
            if record.date > record.idea_end_date:
                raise exceptions.ValidationError("Expired date to vote on the idea: %s" % record.idea_end_date)
    
    #REQ-0000004: Constraint that validate votes for another user 
    @api.constrains('user_id')
    def _check_date_idea(self):
        for record in self:
            if record.user_id != self.env['res.users'].browse(self.env.uid):
                raise exceptions.ValidationError("You cannot vote for another user: %s" % record.user_id.name)
    
    #REQ-0000004: A user only can vote for each idea
    # @api.ulti
    # @api.constrains('idea_id', 'user_id')
    # def _check_unique_number(self):
    #     if self.search_count([
    #             ('idea_id', '=', self.user_id)
    #         ]) > 1:
    #         raise ValidationError(_("Notice Number duplicated!"))

    # @api.multi
    # @api.constrains('idea_id', 'user_id')
    # def _check_only_idea(self):
    #     for record in self:
    #         # if record.search_count([('idea_id', '=', record.idea_id)]) > 1 and
    #         if record.idea_count > 1 and record.user_id == self.env['res.users'].browse(self.env.uid):
    #             raise ValidationError("A user can only vote once for each idea!!")