import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 1:
        rp.process_response(client, client.fetch_um_statuses())
    else:
        print("FetchUMStatuses - Returns JSON object of Universal Message Statuses available")

if __name__ == "__main__":
    rp.main(call_api)