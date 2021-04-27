import sys
import resultprocessor as rp
import os
import uuid

def call_api(client):
    if len(sys.argv) == 4:
        content_type = sys.argv[1]
        url = sys.argv[2]
        tracker = sys.argv[3]

        print("Uploading the", content_type.lower() + " from " + url)
        rp.process_response(client, client.import_asset(content_type, url, tracker))
    else:
        print("Usage: ImportAssetAsyn {mediaType} {URL} {trackerId}")

if __name__ == "__main__":
    rp.main(call_api)