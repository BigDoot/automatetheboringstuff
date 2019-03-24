#!python3
#this program converts txt files to excel spreadsheets
import os, openpyxl

filepath='C:\\Users\\glend\\OneDrive\\Desktop\\python stuff\\chapter 12'
listoffiles = os.listdir(filepath)
txtfiles = []
for file in listoffiles:
    if file.endswith('.txt'):
        txtfiles.append(file)
thecolumn = 1
wb = openpyxl.Workbook()
sheet = wb.active
for txtfile in txtfiles:
    file = open(os.path.join('C:\\Users\\glend\\OneDrive\\Desktop\\python stuff\\chapter 12', txtfile))
    readedfile = file.readlines()
    for items in range(len(readedfile)):
                sheet.cell(row=items+1, column=thecolumn).value=readedfile[items]
    file.close()
    thecolumn += 1
        
wb.save('C:\\Users\\glend\\OneDrive\\Desktop\\python stuff\\chapter 12\\txttoss.xlsx')
print('done')
