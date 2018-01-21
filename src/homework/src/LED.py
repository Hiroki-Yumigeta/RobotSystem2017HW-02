#!/usr/bin/env python
#coding: utf-8

# import
import rospy
from std_msgs.msg import Int32MultiArray
import wiringpi as w

# ドットマトリクスLEDのピンに対応するGPIOの定義
anode   = [21,20,16,12,25,24,23,18]
cathode = [26,19,13, 6, 5,22,27,17]

# 関数の定義
# GPIOの初期化(OUTPUT)
def initGPIO():
    for i in xrange(len(anode)):
        w.pinMode(anode[i], w.OUTPUT)   # anode側
    for i in xrange(len(cathode)):
        w.pinMode(cathode[i], w.OUTPUT) # cathode側

# LEDをオフにする
def ResetPin():
    for i in xrange(len(anode)):
        w.digitalWrite(anode[i],   w.LOW)  # anode側はLOW
        w.digitalWrite(cathode[i], w.HIGH) # cathode側はHIGH

# データに基づきLEDを点灯
def WriteLED(row, vector):
    # anode(行)
    w.digitalWrite(anode[row], w.HIGH)
    #  cathode(列)
    for i in xrange(len(vector)):
        w.digitalWrite(cathode[i], w.LOW if vector[i]==0 else w.HIGH)

# 送られてきたデータの処理
def cb(message):
    type(message.data)
    message_data = list(message.data) # list型に変換
    split = message_data[0] # 先頭のデータ（行数）を取得
    message_data.pop(0) #先頭のデータを削除

    for j in xrange(split):

        # 1行分のデータを取得
        vector = [message_data[j*split+0]]
        for i in range(1,split):
            vector.extend([message_data[j*split+i]])
         
        WriteLED(j, vector) # 関数WriteLEDに渡す
        rate.sleep() # 指定時間wait
        ResetPin() # PINのリセット

# mainプログラム
if __name__ == '__main__':
    rospy.init_node('LED') # ノードの定義
    rate = rospy.Rate(10000) #1秒間に10000回処理

    # GPIO初期化
    w.wiringPiSetupGpio()
    initGPIO()
    ResetPin()

    # サブスクライバの設定
    sub = rospy.Subscriber('BlinkPub', Int32MultiArray, cb)
    rospy.spin()
