import sys
import resultprocessor as rp
import time

def call_api(client):

    now = int(time.time()) * 1000
    thirty_days_ago = now - 2592000000

    if len(sys.argv) == 2:
        filter = \
            { "filter": 
                {
                    "type": "EQUALS",
                    "key": "postId",
                    "values": [ sys.argv[1] ]
                },
                "timeFilter":
                {
                    "key":"channelCreatedTime",
                    "since":thirty_days_ago,
                    "until":now
                }
            }
        rp.process_response(client, client.search_entity("MESSAGE", filter))
    else:
        print("SearchForMessageByPostId - Returns JSON object of message if found")

if __name__ == "__main__":
    rp.main(call_api)
