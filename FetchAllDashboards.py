import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 1:
        rp.process_response(client, client.fetch_all_dashboards())
    else:
        print("FetchAllDashboards (no parameters passed): Returns JSON object of all dashboards accessible by current user/access token")

if __name__ == "__main__":
    rp.main(call_api)