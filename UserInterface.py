#coding=utf8
import sys
import itchat

reload(sys)
sys.setdefaultencoding('utf8')


# user interface interaction
class UI(object):
	'''
	input:
		msg    	  --- typed message from user
		header    --- current header (command fucntion dictionary)
	output:
		reply_msg --- message reply
		header    --- update header (command fucntion dictionary)
	'''
	def __init__(self):
		# command level management dictionary
		self.interface_main = {
		1: self.interface_level_1,
		2: self.interface_level_2
		}

		# level 1 command dictionary
		self.interface_dict_level_1 = {
		"开启": self.open,
		"关闭": self.close,
		"添加": self.add,
		"删除": self.delete,
		"查看": self.view,
		"清空": self.clear
		}

		# level 2 command dictionary
		self.interface_dict_level_2 = {
		"add_user"   : self.add_user,
		"delete_user": self.delete_user
		}

	############################
	######### main API #########
	############################
	def interface_handle(self, msg, header): 
		# convert 'unicode' into 'str'
		msg = msg.encode('utf8')
		# redirect command to related level 
		return self.interface_main[header['interface_level']](msg, header)
	############################
	############################
	############################


	'''
	main API receive 'interface_level',
	and distribute current command into
	related interface level
	'''
	def interface_level_1(self, msg, header):
		if self.interface_dict_level_1.has_key(msg):
			reply_msg, header = self.interface_dict_level_1[msg](header)
		else:
			reply_msg = self.main()
		reply_msg = self.interface_frame() + reply_msg
		return reply_msg, header

	def interface_level_2(self, msg, header):
		reply_msg, header = \
		self.interface_dict_level_2[header['user_status']](msg, header)
		reply_msg = self.interface_frame() + reply_msg
		return reply_msg, header


	# default interface	title frame
	def interface_frame(self):
		 return "***自动回复小助手***\n"

	# default interface	main frame(level 1)
	def main(self):		
		return	 ".......开启.......\n"\
				+".......关闭.......\n"\
				+".......添加.......\n"\
				+".......删除.......\n"\
				+".......查看.......\n"\
				+".......清空.......\n"	

	# all level interface
	## level 1 interface			
	def open(self, header):
		reply_msg = "[自动回复]已经打开"
		header['robot_reply'] = True
		return reply_msg, header

	def close(self, header):
		reply_msg = "[自动回复]已经关闭"
		header['robot_reply'] = False
		return reply_msg, header

	def add(self, header):
		reply_msg = "...请输入添加的好友..."
		header['user_status'] = 'add_user'
		header['interface_level'] = 2
		return reply_msg, header

	def delete(self, header):
		reply_msg = "...请输入删除的好友..."
		header['user_status'] = 'delete_user'
		header['interface_level'] = 2
		return reply_msg, header

	def view(self, header):
		reply_msg = "...当前好友列表..."\
				  + self.display_user_nickname(header['user_list'])
		return reply_msg, header

	def display_user_nickname(self, user_list):
		if not user_list:
			nickname_list = "\n" + ".......空......."
		else:
			nickname_list = ""
			for user in user_list:
				nickname_list += '\n' + user[0]["NickName"]
		return nickname_list

	def clear(self, header):
		reply_msg = "...自动回复好友列表已清空..."
		header['user_list'] = []
		header['user_name_list'] = []
		return reply_msg, header

	## level 2 interface	
	def add_user(self, msg, header):
		operable_user = itchat.search_friends(name = msg)
		if operable_user:
			if operable_user not in header['user_list']:
				reply_msg = "好友添加成功"
				header['user_list'].append(operable_user)
				header['user_name_list'].append(operable_user[0]["UserName"])
			else:
				reply_msg = "好友添加失败:" + "\n" + "好友已存在自动回复列表"
		else:
			reply_msg = "好友添加失败:" + "\n" + "好友不存在"
		header['interface_level'] = 1
		header['user_status'] = ""
		return reply_msg, header

	def delete_user(self, msg, header):
		operable_user = itchat.search_friends(name = msg)
		if operable_user in header['user_list']:
				reply_msg = "好友删除成功"
				header['user_list'].remove(operable_user)
				header['user_name_list'].remove(operable_user[0]["UserName"])
		else:
			reply_msg = "好友删除失败:" + "\n" + "好友不存在自动回复列表"
		header['interface_level'] = 1
		header['user_status'] = ""
		return reply_msg, header
