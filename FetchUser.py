import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 1:
        rp.process_response(client, client.fetch_user())
    else:
        print("FetchUser (no parameters passed): Returns JSON object of current user (determined by Access Token)")

if __name__ == "__main__":
    rp.main(call_api)