import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 1:
        rp.process_response(client, client.fetch_account_custom_fields())
    else:
        print("FetchAccountCustomFields (no parameters passed): Returns JSON object of custom fields on account objects")

if __name__ == "__main__":
    rp.main(call_api)