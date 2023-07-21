from odoo import models, fields, api, _

class profiles_system(models.Model):
    _name = 'profiles.setting'

    empolyeename = fields.Char(string="Empolyee Name")
    teachersname = fields.Text(string="Teachers Name", required=True)
    time = fields.Selection([
        ('part time', 'Part Time'),
        ('full time', 'Full time'),
        ('monday to friday', 'Monday To Friday')
    ], string='eg : part time')
    resofacaclass = fields.Selection([
        ('time management', 'Time Management'),
        ('proper evaluation', 'Proper Evaluation'),
        ('currect time schedule', 'Currect Time Schedule')
    ], string='responsibility of academical classes')
    coursesubject = fields.Selection([
        ('full stack developer', 'Full Stack Developer'),
        ('front end developer', 'Front End Developer'),
        ('back end developer', 'Back End Developer')
    ], string='Course Subject', required=True)
    campus = fields.Char(string='Campus')
    tick1 = fields.Boolean('is parent')

    #notebook details
    workaddress = fields.Selection([
        ('kannur', 'Kannur'),
        ('kozhikkode', 'Kozhikkode'),
        ('malappuram', 'Malappuram'),
        ('kasargod', 'Kasargod')
    ], string='Work Address')

    workmobile = fields.Char(string='Work Address')
    worklocation = fields.Char(string='Work Location')
    workemail = fields.Char(string='Work Email', required=True)
    phonenumber = fields.Integer(string='Phone Number')

    department = fields.Selection([
        ('developer', 'Developer'),
        ('engineer', 'Engineer'),
        ('testing', 'Testing'),
        ('admistration', 'Admnistration')
    ], string='Department')

    jobposition = fields.Selection([
        ('trainee', 'Trainee'),
        ('junior developer', 'Junior Developer'),
        ('assistant engineer', 'Assistant Engineer'),
        ('staff', 'Staff')
    ], string='Job Position')

    manager = fields.Selection([
        ('akhil', 'Akhil'),
        ('sayooj', 'Sayooj'),
        ('ashna', 'Ashna'),
        ('nived', 'Nived')
    ], string='Manager')

    coach = fields.Selection([
        ('adarsh', 'Adarsh'),
        ('amal', 'Amal'),
        ('athul', 'Athul')
    ], string='Coach')

    nationality = fields.Selection([
        ('india', 'India'),
        ('sri lanka', 'Sri Lanka'),
        ('nepal', 'Nepal'),
        ('pakistan', 'Pakistan')
    ], string='Nationality(Country)')

    otherinformation = fields.Text('Other Information')

    #2nd page creating

    identificationno = fields.Integer(string='Identification No')
    passportno = fields.Integer(string='Passport No')
    bankaccountnumber = fields.Selection([
        ('9744', '9744'),
        ('0317', '0317'),
        ('8086', '8086'),
        ('3196', '3196')
    ], string='Bank Account Number')

    address = fields.Selection([
        ('jaya nivas', 'Jaya nivas'),
        ('panjami house', 'Panjami House'),
        ('uppukunnumal house', 'Uppumkunnumal House'),
        ('sneha deepan', 'Sneha Deepam')
    ], string='Address')

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ], string='Gender')

    martialstatus = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married')
    ], string='Martial Status')

    dateofbirth = fields.Date(string='Date Of Birth')

    # SECOND MODELS PARENTS
class profiles_system(models.Model):
    _name = 'profiles.parents'

    myname = fields.Char(string='Name', required=True)
    relationwithchild = fields.Selection([
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('brother', 'Brother'),
        ('relative', 'Relative')
    ], string='Relation With child')
    language = fields.Many2one('res.lang')



#FOR CREATING ADDRESS

    street = fields.Text()
    street2 = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one('res.country.state')
    pin = fields.Char()
    country_id = fields.Many2one('res.country')
#Createing IDS
    mobile_ids = fields.One2many('children.setting', 'mobile')
    phone = fields.Integer(string='Phone')
    mobile = fields.Integer(string='Mobile')
    email = fields.Char(string='Email', required=True)
    title = fields.Selection([
        ('title1', 'Title1'),
        ('title2', 'Title2'),
        ('title3', 'Title3')
    ], string='Title')

    tags = fields.Selection([
        ('tags1', 'Tags1'),
        ('tags2', 'Tags2'),
        ('tags3', 'Tags3')
    ], string='Tags')

    internalnote = fields.Text(string='Internal notes')




class children_system(models.Model):
    _name = 'children.setting'

    studentid = fields.Integer(string='Student ID')
    name = fields.Date(string='Name')
    academicyear = fields.Date(string='Academic Year')
    admissiondate = fields.Date(string='Admission Date')
    gender = fields.Char(string='Gender')
    status = fields.Char(string='Status')
    school = fields.Char(string='School')
    mobile = fields.Many2one('profiles.parents', string='Mobile')


















