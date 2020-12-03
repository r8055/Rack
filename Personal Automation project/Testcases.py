import temp
import logging

def exeTestcases():

    list1=temp.excelreader()

    for x in list1:
        if x == "HS1":
            HS1()
        elif x=="HS2":
            HS2()
        elif x=="HS3":
            HS3()
        elif x=="HS4":
            HS4()
        elif x=="HS5":
            HS5()




def HS1():
    logging.info("testcase HS1 executed")

def HS2():
    logging.info("testcase HS2 executed")

def HS3():
    logging.info("testcase HS3 executed")

def HS4():
    logging.info("testcase HS4 executed")

def HS5():
    logging.info("testcase HS5 executed")




