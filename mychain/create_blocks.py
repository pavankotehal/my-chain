__author__ = 'Pavan Kotehal'
import requests
import time

for i in range(0, 10):
    url = 'http://localhost:5000/mine'
    payload = {}
    headers = {}
    time.sleep(5)
    res = requests.get(url)
    print(res)