import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 1:
        rp.process_response(client, client.fetch_accessible_users())
    else:
        print("FetchAccessibleUsers (no parameters passed): Returns JSON object of accessible users")

if __name__ == "__main__":
    rp.main(call_api)