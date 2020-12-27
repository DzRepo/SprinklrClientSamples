import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 1:
        rp.process_response(client, client.fetch_webhook_types())
    else:
        print("FetchWebhookTypes - Returns JSON object of available webhooks")

if __name__ == "__main__":
    rp.main(call_api)