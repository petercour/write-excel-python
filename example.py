#coding: utf-8
import xlsxwriter
 
file_name = "data.xlsx"
workbook = xlsxwriter.Workbook(file_name)
 
worksheet = workbook.add_worksheet('sheet1')
 
worksheet.write(0, 0, 'id')
worksheet.write(0,1, 'name')
worksheet.write(0,2, 'class')
worksheet.write(0,3, 'data')
 
worksheet.write_row(1, 0, [1, 2, 3])
worksheet.write_column('D2', ['a', 'b', 'c'])
 
workbook.close()
