from odoo import models, fields, api, _

class config_menu(models.Model):
    _name = 'menu.config'

    name = fields.Char(string='Name')
    secondname = fields.Char(string='Second Name')
