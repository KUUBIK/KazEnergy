
import time, http.server
import serial
import json
import requests


url = ' http://127.0.0.1:5000/'

while True:
    headers = {'Content-type': 'application/json',
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}



    answer = requests.post(url)
    print(answer)
    time.sleep(1)
