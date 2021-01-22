import sys
import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 5:
        rp.process_response(client, client.send_email(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))
    else:
        print("Usage: SendEmail {to_address} {from_address} {subject} {message}")

if __name__ == "__main__":
    rp.main(call_api)