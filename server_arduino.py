
import time, http.server
import serial
import json
import requests
import serial
SERIAL_PORT_NAME = "/dev/ttyUSB0"
SERIAL_PORT_SPEED = 9600
ser = serial.Serial(SERIAL_PORT_NAME, SERIAL_PORT_SPEED, timeout=1)


url = ' http://127.0.0.1:5000/'

headers = {'Content-type': 'application/json',
           'Accept': 'text/plain',
           'Content-Encoding': 'utf-8'}
bad_car = {
    "Бак": "Неисправен",
    "Номер машины": "2",
    "Неисправности": "Вероятная утечка в баке"
}

good_car = {
    id:1,
    "Бак": "Исправен",
    "Номер машины": "1",
    "Неисправности": "Невыявленно"
}


def read_port():
    while True:

        s = ser.readline()
        s = s.decode('utf-8')
        s = s.strip()
        if s == '42':
            answer = requests.post(url, data = json.dumps(bad_car))
            print(answer)
            time.sleep(1)
        if s == '52':
            answer = requests.post(url, data = json.dumps(good_car))
            print(answer)
            time.sleep(1)
        else:
            pass

read_port()