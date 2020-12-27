import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 1:
        rp.process_response(client, client.fetch_user_groups())
    else:
        print("FetchUserGroups - Returns JSON object of User groups")

if __name__ == "__main__":
    rp.main(call_api)