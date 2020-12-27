import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 1:
        rp.process_response(client, client.fetch_profile_custom_fields())
    else:
        print("FetchProfileCustomFields (no parameters passed): Returns JSON object of Profile Custom Fields")

if __name__ == "__main__":
    rp.main(call_api)