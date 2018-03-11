#!/usr/bin/env python
# coding: utf-8

# import
import rospy
from std_msgs.msg import Int32MultiArray


# LEDに対応する行列の定義
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
# mainプログラム
if __name__ == '__main__':
    rospy.init_node('Blink') # なんていうプログラムか ノードの定義

    #パブリッシャの定義
    pub = rospy.Publisher('BlinkPub', Int32MultiArray, queue_size=100)

    rate = rospy.Rate(1000) # 毎秒1000回 回す
    dataline = Int32MultiArray() # メッセージのタイプ

    # ループ
    n = 0
    while not rospy.is_shutdown(): # rospyが落ちていない場合は

        # 送信データの定義
        dataline.data = [len(mat)] # matの行数の格納
        for i in xrange(len(mat)):
            dataline.data.extend(mat[i])

        # データ送信
        pub.publish(dataline)
        rate.sleep() # 指定した分だけ休む


        if n==500: # 500回に1度データの更新それ以外はそのまま次のループに移る
            for i in xrange(len(mat)):
                for j in xrange(len(mat[0])):
                    mat[i][j] = 1 if mat[i][j]==0 else 0 # 1, 0の入れ替え
            n=0
        n+=1
