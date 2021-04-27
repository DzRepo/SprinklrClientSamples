import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 1:
        rp.process_response(client, client.search_custom_field(None))
    else:
        print("FetchAllCustomFields (no parameters passed): Returns JSON object of custom fields")

if __name__ == "__main__":
    rp.main(call_api)