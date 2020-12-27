import sys
import resultprocessor as rp
import json

def call_api(client):
    if len(sys.argv) == 2:
        report_object = None
        with open(sys.argv[1]) as f_in:
            report_object = json.load(f_in)
        rp.process_response(client, client.fetch_report(report_object))
    else:
        print("FetchReportByFile {filename.json} - reads and executes a report as defined in a file")

if __name__ == "__main__":
    rp.main(call_api)