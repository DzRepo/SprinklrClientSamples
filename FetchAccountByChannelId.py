import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 3:
        rp.process_response(client, client.fetch_account_by_channel_id(sys.argv[1], sys.argv[2]))
    else:
        print("Usage: FetchAccountByChannelId {account_type} {channel_id}")

if __name__ == "__main__":
    rp.main(call_api)