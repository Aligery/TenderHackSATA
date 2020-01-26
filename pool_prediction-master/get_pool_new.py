import requests, json
from time import sleep
from datetime import datetime
import sys 
import traceback
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("outputfile", nargs='?', default="count_price.json")
parser.add_argument("errorfile", nargs='?', default="count_price_error.txt")
args = parser.parse_args()

def getCountPrice():
    URL = ''
    try:
        r = requests.get(URL)
        countdata = json.loads(r.text)
        countdata['datetime'] = datetime.utcfromtimestamp(int(countdata['timestamp'])).strftime('%Y-%m-%d-%H-%M-%S')

        with open(args.outputfile, mode='a') as file:
            file.write('{},\n'.format(json.dumps(countdata)))

    except:        
        exc_type, exc_value, exc_traceback = sys.exc_info()
        with open(args.errorfile, mode='a') as file:           
           traceback.print_exc(file=file)
           file.write(('-'*100)+'\n\n')


while True:	
    getCountPrice()
    sleep(10)