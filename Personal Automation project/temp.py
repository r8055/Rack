import xlrd
import logging

def excelreader():


    list=[]

    logging.info("Excel read begin")
    excelwbook=xlrd.open_workbook('Book1.xlsx')
    sheet= excelwbook.sheet_by_index(0)
    rows=sheet.nrows
    cols=sheet.ncols

    logging.info(rows)
    logging.info(cols)

    x=1

    while x<rows:
        status = sheet.cell_value(x,1)
        if status=="Yes":
            testcase=sheet.cell_value(x, 0)
            list.append(testcase)
        x+=1
    logging.info(list)
    return list




