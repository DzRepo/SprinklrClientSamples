import sys
import logging
import json
import time
from easysettings import EasySettings
import SprinklrClient as sc

def main(call_api):
    try:
        # start logging
        logging.basicConfig(filename='SprinklrClient.log', level=logging.NOTSET)
        logging.debug("Starting " + sys.argv[0] + " with " + str(len(sys.argv) - 1) + " actual parameters")

        #load settings              
        settings = EasySettings("Sprinklr.conf")
        key = settings.get('key')
        path = settings.get('path')
        access_token = settings.get('access_token')

        if len(path) == 0:
            path = None

        # If using a differnent enviornment other that Prod, set path to that value (like 'prod2')
        client = sc.SprinklrClient(key=key, access_token=access_token, path=path)

        # make API Call - use process_response (defined in resultprocessor) to display results
        call_api(client)

    except Exception as ex:
        print("Error: making API Call:" + str(ex))


def process_response(client, success):
    try:
        logging.debug("Success:" + str(success))
        
        if success:
            if client.result is None:
                logging.debug("No Results")
                logging.debug("Status Message:" + client.status_message)
                print('{ "message":' + client.status_message + '}')
            else:
                result_type = type(client.result)
                result = client.result                
                logging.debug("Result Type:" + str(result_type))
                # logging.debug("Result:" + str(client.result))
                if result_type in {dict, list}:
                    print(json.dumps(result, sort_keys=False, indent=4))
                else:
                    print(client.raw)
        else:
            if client.status_message is None:
                if type(client.result) is dict:
                    print(json.dumps(client.result, sort_keys=False, indent=4))
                else:
                    print(client.result)
            else:
                print("Error:" + str(client.status_code) + ":" + client.status_message )
    except Exception as ex:
        logging.error(str(ex))
        print("Error caught: " + str(ex))

def date_time_toepoch(date_time):
    return datetime_toepoch(date_time.year, date_time.month, date_time.day, date_time.hour, date_time.minute)

def datetime_toepoch(year: int, month: int, day: int, hour=0, minute=0):
    return int(float(time.mktime(datetime.datetime(year, month, day, hour, minute).timetuple())) * 1000)

def datetime_fromepoch(epoch):
    return time.strftime('%Y-%m-%d %H:%M:%S:{0:.0f}'.format(epoch % 1000), time.localtime(epoch))
