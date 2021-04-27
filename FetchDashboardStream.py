import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) > 3 and len(sys.argv) < 8:
        dashboard_id = sys.argv[1]
        start = sys.argv[2]
        rows = sys.argv[3]
        start_date = None
        until_date = None
        sort_order = 'snCreatedTime%20desc'

        if len(sys.argv) > 4:
            start_date = sys.argv[4]

        if len(sys.argv) > 5:
            until_date = sys.argv[5]

        if len(sys.argv) > 6:
            sort_order = sys.argv[6]
        
        rp.process_response(client, client.fetch_dashboard_stream(dashboard_id, start, rows, start_date, until_date, sort_order))

    else:
        print("FetchDashboardStream {stream_id} {start} {rows} [from_date] [until_date] [sort_order]")

if __name__ == "__main__":
    rp.main(call_api)
