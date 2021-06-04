import xlwt
from xlwt import Workbook
import os

# Create workbook
wb = Workbook()

# Create sheet using add_sheet
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0, 0, 'ISBT COLONY')
sheet1.write(1, 0, 'ISBT DEHRADUN')
sheet1.write(2, 0, 'SHASTRADHARA')
sheet1.write(3, 0, 'CLEMEN TOWN')
sheet1.write(4, 0, 'RAJPUR ROAD')
sheet1.write(5, 0, 'CLOCK TOWER')
sheet1.write(6, 1, 'ISBT DEHRADUN')
sheet1.write(7, 2, 'SHASTRADHARA')
sheet1.write(8, 3, 'CLEMEN TOWN')
sheet1.write(9, 4, 'RAJPUR ROAD')
sheet1.write(10, 5, 'CLOCK TOWER')

# if fileExistance:
wb.save('SampleExcel.xls')
fileExistance = os.path.isfile("./SampleExcel.xls")
print(fileExistance)
