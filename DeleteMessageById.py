import sys
import resultprocessor as rp
import time

TIMELINE_TYPE_CODE = "1"
UPDATE_TYPE_CODE = "2"
SENT_DM_TYPE_CODE = "3"
REC_MENTION_TYPE_CODE = "4"
REC_DM_TYPE_CODE = "5"
REPLY_TYPE_CODE = "7"
RETWEET_TYPE_CODE = "8"
SENT_REPLY_TYPE_CODE = "11"
SENT_RETWEET_TYPE_CODE = "12"
SENT_MENTION_TYPE_CODE = "13"


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

        if client.search_entity("MESSAGE", filter):
            result = client.result
            if result is not None:

                message = result["data"]["results"][0]

                sn_type = message["channelType"]
                sn_message_id = message["channelMessageId"]
                source_id = message["sourceId"]
                source_type = message["sourceType"]
                sn_created_time = message["channelCreatedTime"]
                channel_id = message["senderProfile"]["channelId"]

                universal_message_key = \
                {
                    "snType": sn_type,
                    "msgType": UPDATE_TYPE_CODE,
                    "snMsgId": sn_message_id,
                    "sourceId": str(source_id),
                    "sourceType": source_type,
                    "snCreatedTime": sn_created_time
                }

                print("key:", universal_message_key)

                if client.message_action(universal_message_key, sn_type, source_id, "DELETE"):
                    print("Success")
                else:
                    print("Failed. " + client.raw)


    else:
        print("DeleteMessageByPostId - Returns JSON object of message if found")

if __name__ == "__main__":
    rp.main(call_api)
