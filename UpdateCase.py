import sys
import resultprocessor as rp
import json

def call_api(client):
    if len(sys.argv) == 2:
        case_object = None
        with open(sys.argv[1]) as f_in:
            case_object = json.load(f_in)
        rp.process_response(client, client.update_case(case_object))
    else:
        print("UpdateCase {case_object.json}")

if __name__ == "__main__":
    rp.main(call_api)