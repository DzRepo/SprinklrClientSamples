import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 1:
        filter = {"query": "",
              "filters": [
                  {
                      "filterType": "IN",
                      "field": "channelType",
                      "values": ["SPRINKLR"]
                  },
                  {
                      "filterType": "IN",
                      "field": "archived",
                      "values": ["true"]
                  }
              ],
              "paginationInfo": {
                  "start": 0,
                  "rows": 100,
                  "sortKey": "caseModificationTime"
              }}
        rp.process_response(client, client.search_case_v1(filter))
    else:
        print("FetchArchivedCases (no parameters passed): Returns JSON object of all archived cases accessible by current user/access token")

if __name__ == "__main__":
    rp.main(call_api)