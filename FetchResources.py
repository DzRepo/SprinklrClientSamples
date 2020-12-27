import sys
import resultprocessor as rp

def call_api(client):
    if len(sys.argv) == 2:
        rp.process_response(client, client.fetch_resources(sys.argv[1]))
    else:
        print("FetchResources {resource type} (one of: PARTNER_ACCOUNTS, PARTNER_CAMPAIGNS, PARTNER_ACCOUNT_GROUPS, "
        "PARTNER_USERS, CLIENT_USERS, CLIENTS, CLIENT_URL_SHORTNERS, INBOUND_CUSTOM_FIELDS, OUTBOUND_CUSTOM_FIELDS, "
        "PROFILE_CUSTOM_FIELDS, MEDIA_ASSET_CUSTOM_FIELDS, ACCOUNT_CUSTOM_FIELDS, UM_STATUSES, UM_PRIORITIES, ACCESSIBLE_USERS, "
        "APPROVAL_PATHS, PARTNER_QUEUES, CLIENT_QUEUES, PARTNER_PROFILE_LISTS, CLIENT_PROFILE_LISTS, MACROS, PERMISSIONS, USER_GROUPS)")

if __name__ == "__main__":
    rp.main(call_api)