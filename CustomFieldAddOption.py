import sys
import resultprocessor as rp

def call_api(client):
    # custom_field_add_option(sys.argv[2], sys.argv[3])
    if len(sys.argv) == 3:
        option_data = {"addOptions": [sys.argv[2]]}

        if client.update_custom_field_options(sys.argv[1], option_data):
            rp.process_response(client, client.fetch_custom_field(sys.argv[1]))
        else:
            print(client.raw)
    else:
        print("CustomFieldAddOption {field_id} {option_to_add}")

if __name__ == "__main__":
    rp.main(call_api)