from odoo import models, fields, api

class emsReport(models.TransientModel):
    _name = 'ems.wizard'

    start_date = fields.Date()
    end_date = fields.Date()




