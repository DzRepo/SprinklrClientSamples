import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 2:
        rp.process_response(client, client.fetch_user_by_id(sys.argv[1]))
    else:
        print("FetchUserById {user_id}")

if __name__ == "__main__":
    rp.main(call_api)