import sys
import resultprocessor as rp
import os
import uuid

def call_api(client):
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        
        filename_parts = os.path.splitext(filename)
        extension = filename_parts[1][1:]

        # Attempt to determine contentType from filename. Default to FILE if not possible.
        content_type = "FILE"
        if extension in {'png', 'gif', 'jpg', 'jpeg'}:
            content_type = "IMAGE"
        elif extension in {'mov', 'mpeg', 'mp4', 'AVI', 'MPV',}:
            content_type = "VIDEO"
            
        print("Uploading the", content_type.lower(), filename)

        # Using uuid to generate a random tracking number. A date/time stamp or other unique tracking number would probably be better.
        rp.process_response(client, client.asset_upload(content_type, uuid.uuid4(), filename))

    else:
        print("Usage: UploadAsset {filename.ext}")

if __name__ == "__main__":
    rp.main(call_api)