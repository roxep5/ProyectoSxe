# -*- coding: utf-8 -*-

from odoo import models, fields, api


class proyecto(models.Model):
    _name = 'proyecto.suceso'
    _description = 'proyecto.suceso'

    name = fields.Char(string="proyecto")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
