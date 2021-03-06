import logging
import sys


def read_data(isTest=False, value='default'):
    current_day = (sys.argv[0].split('/')[-1].split('.')[0])
    if isTest:
        filename = current_day + "_test.txt"
        logging.warning("*** Using Test Data from " + filename)
    else:
        filename = current_day + "_input.txt"
        logging.warning(" Using Data from " + filename)
    with open(filename) as f:
        if value == 'default':
            return f.read().splitlines()
            logging.info("using default parsing")
        elif value == 'int':
            return [int(x) for x in f]
        elif value == 'str':
            return [str(x) for x in f]
        elif value == 'intlist':
            data = f.read()
            return [int(x) for x in data.split(",")]
        else:
            logging.error("Unsupported value of " + value)
