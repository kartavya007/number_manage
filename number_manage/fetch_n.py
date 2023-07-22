import requests
def fetch(url):
    res = requests.get(url)
    if res.status_code == 200:
        print(res.json())
        return res.json()
    return "{'url' : 'invalid'}"