import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) > 3 and len(sys.argv) < 6:
        stream_id = sys.argv[1]
        
        start = None
        rows = None
        sort_order = 'ASC'

        if len(sys.argv) > 2:
            start = sys.argv[2]

        if len(sys.argv) > 3:
            rows = sys.argv[3]

        if len(sys.argv) > 4:
            sort_order = sys.argv[4]
        
        print("Case Stream Id:", stream_id, "start:", start, "rows:", rows, "sort:", sort_order)
        rp.process_response(client, client.fetch_case_stream(stream_id, start, rows, sort_order))

    else:
        print("FetchCaseStream {stream_id} [start] [rows] [sort_order]")

if __name__ == "__main__":
    rp.main(call_api)
