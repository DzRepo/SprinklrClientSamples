import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 1:
        rp.process_response(client, client.fetch_client_profile_lists())
    else:
        print("FetchClientProfileLists (no parameters) - returns list of all Profile lists visible to the current user/access token")

if __name__ == "__main__":
    rp.main(call_api)