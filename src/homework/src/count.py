#!/usr/bin/env python
# coding: utf-8
import rospy
from std_msgs.msg import Int32

if __name__ == '__main__':
    rospy.init_node('count') # なんていうプログラムか
    pub = rospy.Publisher('count_up', Int32, queue_size=1)
    rate = rospy.Rate(10) # 毎秒10回 回す

    n = 0
    while not rospy.is_shutdown(): # rospyが落ちていない場合は
        n += 1
        pub.publish(n)
        rate.sleep() # 指定した分だけ休む
