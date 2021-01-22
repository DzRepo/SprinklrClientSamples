import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 2:
        rp.process_response(client, client.read_asset(sys.argv[1]))
    else:
        print("Usage: FetchAssetById {account_type} {channel_id}")

if __name__ == "__main__":
    rp.main(call_api)