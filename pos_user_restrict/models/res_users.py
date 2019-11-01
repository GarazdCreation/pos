# -*- coding: utf-8 -*-

from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    pos_config_ids = fields.Many2many(
        comodel_name='pos.config',
        string='Allowed POS',
        help="Allowed POS for users. POS managers can view all Points of Sale.",
    )

    def write(self, values):
        res = super(ResUsers, self).write(values)
        if 'pos_config_ids' in values:
            self.env['ir.default'].clear_caches()
        return res
