#!/usr/bin/env python

import rospy
import roslibpy
from std_msgs.msg import String
from tf2_msgs.msg import TFMessage

class TfBridge:
	def __init__(self):
		self.client = roslibpy.Ros(host='192.168.195.174', port=9090)
                print("wait connecting")
		self.client.run()

	def bridge(self):
		while self.client.is_connected:
	    		self.talker.publish(roslibpy.Message({'data': 'Hello World!'}))
	    		print('Sending message to the hsr')

	def __del__(self):
		self.talker.unadvertise()
		self.client.terminate()

if __name__=='__main__':
	rospy.init_node('listener')
	tf_bridge=TfBridge()
	tf_bridge.bridge()
	del tf_bridge
	rospy.spin()
