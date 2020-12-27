import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 1:
        rp.process_response(client, client.fetch_um_priorities())
    else:
        print("FetchUMPriorities - Returns JSON object of Universal Message Priorities available")

if __name__ == "__main__":
    rp.main(call_api)