import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 3:
        rp.process_response(client, client.add_comment("CASE", sys.argv[1], sys.argv[2]))
    else:
        print("AddCommentToCase {Case_Number} {Comment}")

if __name__ == "__main__":
    rp.main(call_api)