import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 1:
        rp.process_response(client, client.fetch_client_users())
    else:
        print("FetchClientUsers (no parameters passed): Returns JSON object of all Users in the current client environment")

if __name__ == "__main__":
    rp.main(call_api)