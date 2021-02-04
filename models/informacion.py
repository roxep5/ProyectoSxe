from odoo import models,fields,api

class informacion(models.Model):
    _name = 'proyecto.informacion'
    _description = 'Tipos de datos básicos'

    autorizado=fields.Boolean(string="¿Autorizado?",default=True)