

import serial
SERIAL_PORT_NAME = "/dev/ttyUSB0"
SERIAL_PORT_SPEED = 9600
ser = serial.Serial(SERIAL_PORT_NAME, SERIAL_PORT_SPEED, timeout=1)
case = []
case2 = []



def read_port():
    while True:
        s = ser.readline()
        s = s.decode('utf-8')
        s = s.strip()
        if s == '42':
            print("Допускаем машину на объект")
            data = []
            data.append(read_port())
            if not read_port in data:
                data.append(read_port())
                return data
            else:
                pass
            return s
        else:
            pass

read_port()