import sys
import SprinklrClient as sc
import webbrowser as wb

def main():
    if len(sys.argv) > 4 or len(sys.argv) < 3:
        print("Usage: Authorize {apikey} {redirect_uri} [environment]")
    else:
        key = sys.argv[1]
        redirect_uri = sys.argv[2]

        if len(sys.argv) == 4:
            path = sys.argv[3]
        else:
            path = None

        client = sc.SprinklrClient(key, path)        
        url = client.authorize(redirect_uri)
        wb.open(url, new=2)

if __name__ == "__main__":
    main()