import selenium
import requests


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
baseurl = "https://www.robinhood.com"
liveresponse = requests.get(url = baseurl,headers = headers)

if not liveresponse.status_code == 200:
    print("fuck")