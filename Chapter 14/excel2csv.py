#!python3
#yay this works

import os, openpyxl, csv

directory = 'C:\\Users\\glend\\OneDrive\\Desktop\\python stuff\\chapter 12'
directory2 = 'C:\\Users\\glend\\OneDrive\\Desktop\\python stuff\\chapter 14\\convertedexcels'
for excelFile in os.listdir(directory):
    # Skip non-xlsx files, load the workbook object.
    if excelFile.endswith('.xlsx'):
        wb = openpyxl.load_workbook(os.path.join(directory, excelFile))
        for sheetName in wb.sheetnames:
            # Loop through every sheet in the workbook.
            sheet = wb[sheetName]
            csvfilename = os.path.splitext(excelFile)[0] + '_' +sheetName + '.csv'
            csvfile = open(os.path.join(directory2,csvfilename), 'w', newline='')
            # Create the CSV filename from the Excel filename and sheet title.
            # Create the csv.writer object for this CSV file.
            csvwriter = csv.writer(csvfile)

            # Loop through every row in the sheet.
            for rowNum in range(1, sheet.max_row + 1):
                rowData = []    # append each cell to this list
                # Loop through each cell in the row.
                for colNum in range(1, sheet.max_column + 1):
                    rowData.append(sheet.cell(row=rowNum, column=colNum).value)
                    # Append each cell's data to rowData.

                # Write the rowData list to the CSV file.
                csvwriter.writerow(rowData)

            csvfile.close()
print('done')

