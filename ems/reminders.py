from odoo import models, fields, api, _

class reminders_menu(models.Model):
    _name = 'menu.reminders'

    name = fields.Char(string='Name')
    secondname = fields.Char(string='Second Name')



