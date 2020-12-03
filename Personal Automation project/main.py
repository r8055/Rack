import logging
import logging.config
import json
import Testcases
import temp
import file1

def main():

    with open("logging.json",'r') as f:
        dict= json.load(f)

    logging.config.dictConfig(dict)
    Testcases.exeTestcases()







if __name__ == '__main__':
    main()