import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 2:
        update_request = {
         "tags":["UpdatedViaAPI"]
        }
        rp.process_response(client, client.update_asset(sys.argv[1], update_request))
    else:
        print("Usage: UpdateAsset {asset_id}")
        print("This command will add an 'UpdatedViaAPI' tag to an asset")

if __name__ == "__main__":
    rp.main(call_api)