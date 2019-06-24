# AutoReplyRobot
AutoReply Robot

This project introduces a kind of "Auto Chat Robot" in a Chinese App named Wechat, which mainly auto reply manager based on Itchat API and Turling robot API. Generally, when the code is executing, user can easily setup several functions in his/her Android or IOS mobile phone. All code is based on Python.

Setup Environment
Firstly, the Itchat API need to be installed previously(pip need to be install previously).

    sudo pip install Itchat

Then, Get Turling Robot APT code
and replace the key in main.py line 16: KEY = ''.
For more introduction, visit http://www.tuling123.com/help/h_cent_webapi.jhtml.

Execute procedure
run main.py directly. 

    python main.py

If the procedure starts at the first time, it will display SQ code to scan by using mobile Wechat.
(picture)

In Wechat, use find user of yourself and type related command to achieve all functions. If you type non-function word, it will display main interface to remind you to type several kinds of words to achieve related function

# Please feel free to commend it. This is only a test project. I am look forward to hearing from you!




A example is shown below:

Main User Interface
 ![image](https://github.com/baiye225/AutoReplyRobot/blob/master/Image/MainInterface.jpg)
 
Open/Close AutoReply Robot
Activate/Deactivate AutoReply Robot
 ![image](https://github.com/baiye225/AutoReplyRobot/blob/master/Image/TurnOnOffRobot.jpg)

Add/Delete AutoReply List
Add/Delete your friend in the list of AutoReply
 ![image](https://github.com/baiye225/AutoReplyRobot/blob/master/Image/AddUser.jpg)
 
View Current AutoReply List
View who is in your list

Clear AutoReply List
Clear all friends in the list


