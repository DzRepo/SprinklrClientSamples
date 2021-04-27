import sys
import resultprocessor as rp
import json

def call_api(client):
    if len(sys.argv) == 2:
        message = None
        with open(sys.argv[1]) as f_in:
            message = json.load(f_in)

        if message is not None:
            rp.process_response(client, client.publish_post(message))
    else:
        print("Usage: PublishPost {message.json} - reads file containing message")

if __name__ == "__main__":
    rp.main(call_api)