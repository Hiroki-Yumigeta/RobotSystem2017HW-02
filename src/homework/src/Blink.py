#!/usr/bin/env python
# coding: utf-8
import rospy
from std_msgs.msg import Int32MultiArray

n = 0

mat=[
    [0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,1,1,0,0,0],
    [0,0,0,1,1,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0]
]

if __name__ == '__main__':
    rospy.init_node('Blink') # なんていうプログラムか
    pub = rospy.Publisher('BlinkPub', Int32MultiArray, queue_size=100)
    rate = rospy.Rate(1000) # 毎秒10回 回す
    dataline = Int32MultiArray()
    while not rospy.is_shutdown(): # rospyが落ちていない場合は
        dataline.data = [len(mat)]
        for i in xrange(len(mat)):
            dataline.data.extend(mat[i])
        pub.publish(dataline)
        rate.sleep() # 指定した分だけ休む

        if n==500:
            for i in xrange(len(mat)):
                for j in xrange(len(mat[0])):
                    mat[i][j] = 1 if mat[i][j]==0 else 0
            n=0
        n+=1
