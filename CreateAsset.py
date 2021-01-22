import sys
import resultprocessor as rp

def call_api(client):
    # create_asset(name, asset_type, description, uploaded_content_id)
    #  create_asset(sys.argv[2], sys.argv[3], sys.argv[4],sys.argv[5])
    if len(sys.argv) == 5:
        asset_data = {
            "name": sys.argv[1],
            "assetType": sys.argv[2],
            "description": sys.argv[3],
            "uploadedContentId": sys.argv[4]
        }
        rp.process_response(client, client.create_asset(asset_data))
    else:
        print("Usage: CreateAsset {name}, {assetType}, {description}, {uploadedContentId}")

if __name__ == "__main__":
    rp.main(call_api)