


import serial
import pygame
import time



class MicroBitComms:
    def __init__(self, port):
        self.port = str(port)
        self.ser = serial.Serial(self.port, 19200, timeout=100)

    def send(self, data):
        # encode the data into bytes using utf-8 protocal
        data = bytes(str(data) + "\n", 'utf-8')
        # write the bytes via serial
        self.ser.write(data)
        self.ser.flush()

    def recieve(self):
        return self.ser.readline()

    def wait_until_rx(self):
        while not self.ser.inWaiting():
            msg = self.recieve()
            return msg



#Declare us both
me = MicroBitComms("COM7")


while True:
    msg = input("WHat do you want to say bitch")
    me.send(msg)
    if me.ser.inWaiting():
        me.recieve()
        msg = input("WHat do you want to say bitch")
        me.send(msg)



