import openpyxl

wb = openyxl.Workbook()
wb.get_sheet_names()
sheet = wb.active
wb.title
sheet.title = 'Test Sheet'
sheet.title
wb.get_sheet_names()
wb.save('Python.xlsx')