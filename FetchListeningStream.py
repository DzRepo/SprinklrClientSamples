import sys
import resultprocessor as rp
# fetch_listening_stream(stream_id, since_time, until_time, timezone_offset=14400000,  time_field="SN_CREATED_TIME",
#                           details="STREAM", dimension="TOPIC", metric="MENTIONS", trend_aggregation_period=None, start=1,
#                           rows=1, echo_request=True, tag=None, sort_key=None, message_format_options=None)

def call_api(client):
    if len(sys.argv) > 3 and len(sys.argv) < 16:
        stream_id = sys.argv[1]
        since_time = sys.argv[2]
        until_time = sys.argv[3]
        timezone_offset = 14400000
        details = "STREAM"
        dimension="TOPIC"
        metric="MENTIONS"
        trend_aggregation_period = None
        start = 1
        rows = 1
        echo_request = True
        tag = None
        sort_key = None
        message_format_options = None

        stream = {
            "sinceTime": since_time,
            "untilTime": until_time,
            "timezoneOffset": timezone_offset,
            "details": {
                "widgetType": details
            },
            "filters": 
            [
                {
                    "dimension": dimension,
                    "filterValues": [stream_id]
                }
            ],
            "metric": metric,
            "start": start,
            "rows": rows,
            "timeField": "SN_CREATED_TIME",
            "echoRequest": echo_request
        }
        rp.process_response(client, client.fetch_listening_stream(stream))
    else:
        print("FetchListeningStream {id} {sinceTime} {untilTime} - returns data from listening stream (other options can be set in code)")

if __name__ == "__main__":
    rp.main(call_api)