import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 1:
        rp.process_response(client, client.fetch_outbound_custom_fields())
    else:
        print("FetchOutboundCustomFields (no parameters passed): Returns JSON object of Outbound Message Custom Fields")

if __name__ == "__main__":
    rp.main(call_api)