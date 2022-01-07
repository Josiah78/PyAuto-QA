import openpyxl

wb= openpyxl.load_workbook('cheese.xlsx')
sheet = wb.get_sheet_by_name('Sheet')
sheet.merge_cells('A1:C1')
wb.save('chees.xlsx')

sheet.freeze_panes = 'A2'
wb.save('cheese.xlsx')