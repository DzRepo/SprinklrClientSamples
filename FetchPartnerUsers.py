import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 1:
        rp.process_response(client, client.fetch_partner_users())
    else:
        print("FetchPartnerUsers (no parameters passed): Returns JSON object of Partner Users visible to current user/access token")

if __name__ == "__main__":
    rp.main(call_api)