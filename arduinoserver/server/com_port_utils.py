import serial
from serial import SerialTimeoutException
import time


ser = serial.Serial('COM3', 9600, timeout=1)
command_list = ['home']


def send(message):
    pass


def receive():
    global command_list

    while 1:
        try:
            message = ser.readline()
            print(message)
            command_list.append(message)
            time.sleep(1)

        except SerialTimeoutException:
            print('Data could not be read')
            time.sleep(1)

