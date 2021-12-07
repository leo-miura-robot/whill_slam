#!/usr/bin/env python

import rospy
import roslibpy
from std_msgs.msg import String
from tf2_msgs.msg import TFMessage

class TfBridge:
	def __init__(self): #innsutannsu_
		rospy.Subscriber('/tf',TFMessage,self.callback)
		self.ros_client = Ros('roboworks-whill.local', 9090)
		self.listener = Topic(self.ros_client, '/tf','tf2_msgs/TFMessage')
		self.listener.subscribe(self.callback)

		self.ros_client.run_forever()	

	def callback(self,data):
		self.tf_data=data
		print data

if __name__=='__main__':
	rospy.init_node('listener')
	TfBridge()

	rospy.spin()
