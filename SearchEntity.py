import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 1:
        search_request = {
            "filters":{
                "ASSET_TYPE":[
                    "PHOTO", "VIDEO", "PDF", "DOC", "EXCEL", "PRESENTATION", "PSD", "TEXT", "RICH_TEXT", "LINK", "POST"
                ]
            },
            "sortList":[
                {
                    "order":"DESC",
                    "key":"createdTime"
                }
            ],
            "rangeCondition":{
            "start":0,
            "fieldName":"createdTime",
            "end":1924363439363
        },
        "onlyAvailable":True,
        "start":0,
        "rows":2
        }
        rp.process_response(client, client.search_asset(search_request))
    else:
        print("FetchWebhookTypes - Returns JSON object of assets - modify program to alter search conditions")

if __name__ == "__main__":
    rp.main(call_api)