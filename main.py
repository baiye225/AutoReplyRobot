#coding=utf8
import itchat
from itchat.content import TEXT
from itchat.content import *
import sys
import time
import re
import requests, json
import aiml

reload(sys)
sys.setdefaultencoding('utf8')
import os
from UserInterface import UI

KEY = 'b5cbd2ae7ca34f39a58929d93f76731d'
intfce = UI()
# turling robot
def get_response(msg): 
	apiUrl = 'http://www.tuling123.com/openapi/api' 
	data = {'key'    : KEY, 
			'info'   : msg, 
			'userid' : 'wechat-robot', 
			} 
	try: 
		r = requests.post(apiUrl, data=data).json() 
		return r.get('text') 
	except: 
		return

	
# When recieve the following msg types, trigger the auto replying.
@itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO]\
	,isFriendChat=True, isMpChat=True)
def text_reply(msg):
	global header

	# userinterface for user command
	if msg['FromUserName'] == myUserName:
		reply_msg, header = intfce.interface_handle(msg['Content'], header)
		itchat.send_msg(reply_msg, myUserName)

	# auto_reply from friends command 
	elif header[robot_reply] and msg['FromUserName'] in header[user_name_list]:
		# Let Turing reply the msg.
		# Sleep 1 second is not necessary. Just cheat human.
		time.sleep(2)
		reply_msg = get_response(msg['Content'])
		itchat.send(reply_msg, msg['FromUserName'])
	return

# Main
if __name__ == '__main__':
	# Set the hot login
	itchat.auto_login(hotReload = True)

	# Get your own UserName
	myUserName = itchat.get_friends(update=True)[0]["UserName"]

	# Initialize AutoReply header (command fucntion dictionary)
	header = {
	'interface_level': 1,	  # user interface level
	'robot_reply'	 : False, # robot reply switch
	'user_list'		 : [],	  # general user database
	'user_name_list' : [],    # username database <=> msg['FromUserName']
	'user_status'	 : ""	  # user interface status(drive sub_level function)
	}
	
	itchat.run()