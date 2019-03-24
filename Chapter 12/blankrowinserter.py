#!python3
#this program adds a blank row to your excel file, please create a bat file to run this
#usage: blankrowinserter.bat N M filename

import os, openpyxl, sys

N = int(sys.argv[1])
M = int(sys.argv[2])
filename = sys.argv[3]
os.chdir('C:\\Users\\glend\\OneDrive\\Desktop\\python stuff\\chapter 12')
wb = openpyxl.load_workbook(filename)
sheet = wb.active
newwb = openpyxl.Workbook()
newsheet = newwb.active
for rows in range(1, sheet.max_row+1):
    for columns in range(1, sheet.max_column+1):
        if rows<N:
            newsheet.cell(row=rows, column=columns).value=sheet.cell(row=rows, column=columns).value
        else:
            newsheet.cell(row=rows+M, column=columns).value=sheet.cell(row=rows, column=columns).value
newwb.save('C:\\Users\\glend\\OneDrive\\Desktop\\python stuff\\chapter 12\\blanksinserted.xlsx')
print('done')
