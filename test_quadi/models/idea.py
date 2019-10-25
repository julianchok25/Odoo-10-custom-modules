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
    qualy = fields.Float(digits=(3, 2), compute="_compute_vote", store=True)
    start_date = fields.Datetime('Start date', default=fields.Datetime.now(), \
        attrs="{'readonly':[('create_uid','!=',self.env.uid)]}")
    end_date = fields.Datetime('End date', compute='_get_end_date', readonly=True)
    user_id = fields.Many2one('res.users', string='Owner', default=lambda self: self.env.uid, \
        domain=[('partner_id.is_company','=',False)])
    vote_ids = fields.One2many(comodel_name='test_quadi.vote', inverse_name='idea_id', \
        string='Votes')
    vote_count = fields.Integer('Votes', compute='_vote_count',
        default=0, readonly=True, store=True)
    #vote_id = fields.Many2one('test_quadi.vote')
    user_vote = fields.Char(related='vote_ids.user_id.name', readonly=True, store=True)

    @api.one    
    @api.depends('vote_ids')
    def _vote_count(self):
        if self.vote_ids:
            self.vote_count = len(self.vote_ids)
        else:
            self.vote_count = 0

    @api.one
    @api.depends('vote_count')
    def _compute_vote(self):
        data_obj = self.env['test_quadi.vote'].search([('active_c','=', True)])
        #a = 0 
        #for x in data_obj:
        #    a += 1
        for r in self:
            if not data_obj:
                r.qualy = 0.0
            else:
                r.qualy =  (float(r.vote_count / float(len(data_obj)))) * 100.0

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

    #@api.constrains('user_id')
    #def _check_user_start_date(self):
    #    for r in self:
    #        if r.user_id != create_uid
    #            raise exceptions.ValidationError("The initial date should only \
    #            be placed by the person who created it")