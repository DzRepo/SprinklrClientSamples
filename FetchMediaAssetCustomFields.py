import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 1:
        rp.process_response(client, client.fetch_media_asset_custom_fields())
    else:
        print("FetchMediaAssetCustomFields (no parameters passed): Returns JSON object of custom fields on media assets")

if __name__ == "__main__":
    rp.main(call_api)