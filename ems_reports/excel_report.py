from odoo import models


class admissioncardxlsx(models.AbstractModel):
    _name = 'report.educational_management_system.report_card_xlsx'
    _inherit = 'report.report_xlsx.abstract'
#link in manifest xlsx
    def generate_xlsx_report(self, workbook, data, lines):

        print("lines", lines)
        format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
        format2 = workbook.add_format({'font_size': 10, 'align': 'vcenter'})
        sheet = workbook.add_worksheet('report_Card')
        sheet.write(2, 2, 'First name', format1)
        sheet.write(2, 3, lines.firstname, format2)
        sheet.write(3, 2, 'Middle Name', format1)
        sheet.write(3, 3, lines.middlename, format2)






class teacherxlsx(models.AbstractModel):
    _name = 'report.educational_management_system.report_card1_xlsx'
    _inherit = 'report.report_xlsx.abstract'


    def generate_xlsx_report(self, workbook, data, lines):

        print("lines", lines)
        format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
        format2 = workbook.add_format({'font_size': 10, 'align': 'vcenter'})
        sheet = workbook.add_worksheet('report_Card')
        sheet.write(2, 2, 'Empolyee Name', format1)
        sheet.write(2, 3, lines.empolyeename, format2)
        sheet.write(3, 2, 'Teachers Name', format1)
        sheet.write(3, 3, lines.teachersname, format2)





class parentsxlsx(models.AbstractModel):
    _name = 'report.educational_management_system.report_card2_xlsx'
    _inherit = 'report.report_xlsx.abstract'



    def generate_xlsx_report(self, workbook, data, lines):

        print("lines", lines)
        format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
        format2 = workbook.add_format({'font_size': 10, 'align': 'vcenter'})
        sheet = workbook.add_worksheet('report_Card')
        sheet.write(2, 2, ' Name', format1)
        sheet.write(2, 3, lines.myname, format2)
        sheet.write(3, 2, 'Relation With child', format1)
        sheet.write(3, 3, lines.relationwithchild, format2)







class remainderssxlsx(models.AbstractModel):
    _name = 'report.educational_management_system.report_card3_xlsx'
    _inherit = 'report.report_xlsx.abstract'



    def generate_xlsx_report(self, workbook, data, lines):

        print("lines", lines)
        format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
        format2 = workbook.add_format({'font_size': 10, 'align': 'vcenter'})
        sheet = workbook.add_worksheet('report_Card')
        sheet.write(2, 2, ' Name', format1)
        sheet.write(2, 3, lines.name, format2)
        sheet.write(3, 2, 'Second Name', format1)
        sheet.write(3, 3, lines.secondname, format2)
