import sys
from easysettings import EasySettings
import SprinklrClient as sc

def main():
    print("Number of args:", len(sys.argv))
    if len(sys.argv) > 6 or len(sys.argv) < 5:
        print(
            "Usage: FetchAccessToken {apikey} {secret} {code} {redirect URI} [path]")
    else:
        path = None
        key = sys.argv[1]
        secret = sys.argv[2]
        code = sys.argv[3]
        redirect = sys.argv[4]

        if len(sys.argv) == 6:
            path = sys.argv[5]

        settings = EasySettings("Sprinklr.conf")
        client = sc.SprinklrClient(key, path)

        success = client.fetch_access_token(secret=secret, code=code, redirect_uri=redirect)

        if success:
            settings.set('access_token', client.access_token)
            settings.set('refresh_token', client.refresh_token)
            settings.set('redirect_uri', redirect)
            settings.set('key', key)
            settings.set('secret', secret)
            settings.set('path', path),
            settings.save()
            print("Successfully retrieved and stored access tokens to Sprinklr.conf")
        else:
            print("Access Token NOT retrieved or stored. API call result:")
            print(client.result)


if __name__ == "__main__":
    main()