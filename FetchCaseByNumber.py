import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 2:
        rp.process_response(client, client.fetch_case_by_number(sys.argv[1]))
    else:
        print("FetchCaseByNumber {case_number}")

if __name__ == "__main__":
    rp.main(call_api)