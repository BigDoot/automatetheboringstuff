#!python3
#this program inverts spreadsheets

import os, openpyxl

wb = openpyxl.load_workbook('C:\\Users\\glend\\OneDrive\\Desktop\\python stuff\\chapter 12\\example.xlsx')
sheet = wb.active
newwb = openpyxl.Workbook()
newsheet = newwb.active
for rows in range(1, sheet.max_row+1):
    for columns in range(1, sheet.max_column+1):
        newsheet.cell(row=columns, column=rows).value = sheet.cell(row=rows, column=columns).value
newwb.save('C:\\Users\\glend\\OneDrive\\Desktop\\python stuff\\chapter 12\\inverted.xlsx')
print('done')
