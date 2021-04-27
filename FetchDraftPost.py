import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 2:
        rp.process_response(client, client.post_draft_read_v1(sys.argv[1]))
    else:
        print("FetchDraftPost {post_id}")

if __name__ == "__main__":
    rp.main(call_api)