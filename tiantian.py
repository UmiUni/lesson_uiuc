# -*- coding: UTF-8 -*-
import requests
import itchat
from itchat.content import *
import sys  
import json
import time
from time import sleep
import settings
from xiaozhushou_util.xiaozhushou_util import *
import re
reload(sys)  
sys.setdefaultencoding('utf8')

itchat.auto_login(enableCmdQR=2,hotReload=True)
itchat.get_chatrooms(update=True)
settings.init()

@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg(settings.vT, msg['RecommendInfo']['UserName'])
    sleep(0.5)
    itchat.send_msg(settings.vU, CurUserName)
    sleep(0.5)
    itchat.send_msg(settings.v12, msg['RecommendInfo']['UserName'])

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
  CurUserName = msg['FromUserName']
  sendGroupInviteMsg(msg,CurUserName)
  if(u'超然管理员' in msg['Content']):
    settings.admins.append(CurUserName)  
    itchat.send_msg(u'您已是管理员',CurUserName)

#send group invite msg according to digits
def sendGroupInviteMsg(msg,CurUserName):
  msgText = msg['Text']
  CurUserName = msg['FromUserName']
  itchat.send_msg(settings.vT, CurUserName)
  sleep(0.5)
  itchat.send_msg(settings.vU, CurUserName)
  sleep(0.5)
  itchat.send_msg(settings.v12, CurUserName)
  sleep(0.5)

def addToCourse(iL,msg,CurUserName):
  if(len(iL) > 0):
    print iL
    twoL=re.split('(\d+)',iL[0])
    print twoL
    finalC0=twoL[0].upper()+twoL[1]
    finalC1=twoL[0].upper()+" "+twoL[1]

    retVal0 = pullMembersMore(msg, finalC0, CurUserName)
    if not retVal0:
      retVal1 = pullMembersMore(msg, finalC1, CurUserName)
      if not retVal1:
        itchat.send_msg("不好意思，此课程群没有，几分钟内帮你建好😊", CurUserName)
    sleep(0.5)

#if group chat msg contains kick ads, start kicking logic
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
  if msg['ActualUserName'] in settings.admins:
    content = msg['Content']
    if(content[0]=="@"):
      if u'广告' in content:
        delUser(msg['FromUserName'],content,settings.ADMIN)

itchat.run() 

