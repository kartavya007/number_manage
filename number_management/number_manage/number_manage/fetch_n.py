import requests
def fetch(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res.text
    return "{'url' : 'invalid'}"