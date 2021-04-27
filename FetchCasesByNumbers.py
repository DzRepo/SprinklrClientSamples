import sys
import resultprocessor as rp


def call_api(client):
    if len(sys.argv) > 1:
        case_list = "', '".join(sys.argv[1:])
        case_list = "'" + case_list + "'"

        search_request = {
            "filter": {
                "type": "AND",
                "filters": [
                    {
                        "type": "IN",
                        "key": "caseNumber",
                        "values": 
                            sys.argv[1:]
                    }
                ]
            },
            "sorts": {
                "key": "caseNumber",
                "order": "ASC"
            }
        }
        rp.process_response(client, client.search_entity("CASE", search_request))
    else:
        print(
            "FetchCasesByNumbers {case_number} [case_number] [case_number] [case_number]...")

if __name__ == "__main__":
    rp.main(call_api)
