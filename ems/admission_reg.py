from odoo import models, fields, api, _

class education_system(models.Model):
    _name = 'education.management'


#Create the action (draft,confirm etc)
    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                            ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string='Status')










#sequence creating code

    seq = fields.Char(string="Order Reference", required=True, copy=False, readonly=True,
                                        index=True, default=lambda self: _('New'))
    @api.model
    def create(self, vals):
        if vals.get('seq', _('New')) == _('New'):
            vals['seq'] = self.env['ir.sequence'].next_by_code('1byorder') or _('New')
        result = super(education_system, self).create(vals)
        return result







    firstname = fields.Char(string='First Name', required=True)
    middlename = fields.Char(string='Middle Name', required=True )
    lastname = fields.Char(string='Last Name', required=True)
    school = fields.Selection([
        ('kannur', 'Kannur'),
        ('kozhikode', 'Kozhikode'),
        ('kasargod', 'Kasargod')
    ], string='School Name', required=True)
    academicyear = fields.Date(string='Academic Year')
#address details
    street = fields.Text()
    street2 = fields.Char()
    city = fields.Char(required=True)
    state_id = fields.Many2one('res.country.state',required=True)
    pin = fields.Char()
    country_id = fields.Many2one('res.country', required=True)
    phone = fields.Char(string='Phone')
    mobile = fields.Char(string='Mobile')
    email = fields.Char(string='Email')
    websitelink = fields.Char(string='Website Link')
    image = fields.Binary(string='Image')
#



# #class information
    medium = fields.Selection([
        ('english', 'English'),
        ('malayalam', 'Malayalam'),
        ('tamil', 'Tamil')
    ], string='Medium')

    class1 = fields.Selection([
        ('1st class', '1st Class'),
        ('2nd class', '2nd Class'),
        ('3rd class', '3rd Class')
    ], string='Class')


#General information
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ], string='Gender', required=True)

    birthdate = fields.Date(string='Birthdate', required=True)
    age = fields.Integer()
    mothertongue = fields.Selection([
        ('malayalam', 'Malayalam'),
        ('english', 'English'),
        ('tamil', 'Tamil')
    ], string='Mother Toungue')
    admissiondate = fields.Date(default=fields.Date.today(), string='Admission Date')
    martialstatus = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ], string='Martial Status')

    phoneno = fields.Integer(string='Phone Number')
    mobileno = fields.Integer(string='Mobile Number')
    remark = fields.Text(string='Remarks')

# CREATE IDS
    parents_ids = fields.One2many('parent.education', 'firstname')
    references_ids = fields.One2many('reference.education', 'firstname')
    previousschool_ids = fields.One2many('previousschool.education', 'firstname')
    familydetails_ids = fields.One2many('familydetails.education', 'firstname')


#    NEW MODEL

class parents(models.Model):
    _name = 'parent.education'

    name = fields.Char(string='Name')
    relationwithchild = fields.Char(string='Relation With Child')
    phone = fields.Integer(string='Phone')
    email = fields.Char(string='Email')
    city = fields.Char(string='City')
    country = fields.Char(string='Country')
    firstname = fields.Many2one('education.management', string='First Name')

class references(models.Model):
    _name = 'reference.education'

    firstname = fields.Char(string='First Name')
    middlename = fields.Char(string='Middle Name')
    surname = fields.Char(string='surname')
    designation = fields.Char(string='Designation')
    phone = fields.Integer(string='Phone')
    firstname = fields.Many2one('education.management', string='First Name')


class previousschool(models.Model):
    _name = 'previousschool.education'

    name = fields.Char(string='Name')
    registrationno = fields.Integer(string='Registration No')
    admissiondate = fields.Date(string='Admission Date')
    exitdate = fields.Date(string='Exit Date')
    course = fields.Char(string='Course')
    firstname = fields.Many2one('education.management', string='First Name')

class familydetails(models.Model):
    _name ='familydetails.education'

    name = fields.Char(string='Name')
    relation = fields.Char(string='Relation')
    phone = fields.Integer(string='Phone')
    firstname = fields.Many2one('education.management', string='First Name')


