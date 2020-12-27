import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 1:
        rp.process_response(client, client.fetch_partner_account_groups())
    else:
        print("FetchPartnerAccountGroups (no parameters passed): Returns JSON object of Parther Account Groups")

if __name__ == "__main__":
    rp.main(call_api)