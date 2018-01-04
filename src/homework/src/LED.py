#!/usr/bin/env python
#coding: utf-8

import rospy
from std_msgs.msg import Int32MultiArray
import wiringpi as w
OUTPUT = 1
HIGH = 1
LOW  = 0

anode   = [21,20,16,12,25,24,23,18]
cathode = [26,19,13, 6, 5,22,27,17]

def initGPIO():
    for i in xrange(len(anode)):
        w.pinMode(anode[i], OUTPUT)
    for i in xrange(len(cathode)):
        w.pinMode(cathode[i], OUTPUT)
def ResetPin():
    for i in xrange(len(anode)):
        w.digitalWrite(anode[i],   LOW)
        w.digitalWrite(cathode[i], HIGH)

def WriteLED(row, vector):
    w.digitalWrite(anode[row], HIGH)
    for i in xrange(len(vector)):
        w.digitalWrite(cathode[i], vector[i])

def cb(message):
    # 中身
    message_data = list(message.data)
    split = message_data[0]
    message_data.pop(0)
    message_len = len(message_data)
    for j in xrange(message_len/split):
        vector = [message_data[j*split+0]]
        for i in range(1,split):
            vector.extend([message_data[j*split+i]])
        WriteLED(j, vector)
        rate.sleep()
        ResetPin()

if __name__ == '__main__':
    rospy.init_node('LED')
    rate = rospy.Rate(100000)
    w.wiringPiSetupGpio()
    initGPIO()
    ResetPin()
    sub = rospy.Subscriber('BlinkPub', Int32MultiArray, cb)
    rospy.spin()