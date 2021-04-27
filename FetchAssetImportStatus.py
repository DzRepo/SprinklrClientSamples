import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 2:
        rp.process_response(client, client.fetch_asset_import_status(sys.argv[1]))
    else:
        print("FetchAssetImportStatus {task_id} - returns status of asset import")

if __name__ == "__main__":
    rp.main(call_api)