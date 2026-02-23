import requests

url = "https://sigdef.eauxetforets.gov.ma/arcgis/apps/webappviewer/index.html?id=57a4e93c2c0e47358208c66930f360e5"

def fetch(url, timeout=15 ):
    try:
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        return resp
    except requests.exceptions.ContentDecodingError:
        # Server advertised gzip but returned invalid gzip bytes — retry without gzip
        headers = {"Accept-Encoding": "identity"}
        resp = requests.get(url, headers=headers, timeout=timeout)
        resp.raise_for_status()
        return resp




if __name__ == '__main__':
    try:
        response = fetch(url)
        if response.status_code == 200:
           FILE= open("webpage.html","w")
           FILE.write(response.text)
           FILE.close()
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    except Exception as e:
        print('Error:', repr(e))

