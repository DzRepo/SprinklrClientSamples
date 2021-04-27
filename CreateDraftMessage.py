import sys
import resultprocessor as rp
import json

def call_api(client):
    # create_asset(name, asset_type, description, uploaded_content_id)
    #  create_asset(sys.argv[2], sys.argv[3], sys.argv[4],sys.argv[5])
    if len(sys.argv) == 2:
        draft_message = None
        with open(sys.argv[1]) as f_in:
            draft_message = json.load(f_in)

        if draft_message is not None:
            rp.process_response(client, client.create_draft_message(draft_message))
    else:
        print("Usage: CreateDraftMessage {message.json} - reads file containing message draft")

if __name__ == "__main__":
    rp.main(call_api)