import openpyxl
from openpyxl.styles import Font

wb= openpyxl.load_workbook('cheese.xlsx')
sheet = wb.get_sheet_by_name('Sheet')
fontObject = Font(name='Avenir', size=30, bold=True)
sheet['A1'].font = fontObject
wb.save('cheese.xlsx')

wb= openpyxl.load_workbook('cheese.xlsx')
sheet = wb.get_sheet_by_name('Sheet')
sheet['A5'] = '=SUM(A1:A4)'
wb.save('cheese.xlsx')