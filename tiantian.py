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

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
  CurUserName = msg['FromUserName']
  sendGroupInviteMsg(msg,CurUserName)

#send group invite msg according to digits
def sendGroupInviteMsg(msg,CurUserName):
  msgText = msg['Text']
  msgText = msgText.replace(" ","")
  x = re.findall(r'\d+', msgText)
  auto = True 
  #print x
  if(len(x) >0):
    y= int(x[0])
    if(y>=0 and y<=4):
      pullMembersMore(msg, settings.chatGroups[y], CurUserName)
      sleep(0.5)
    elif(y==5):
      CurUserName = msg['FromUserName']
      settings.mutes.append(CurUserName)
    elif(y==6):
      CurUserName = msg['FromUserName']
      if CurUserName in settings.mutes: settings.mutes.remove(CurUserName)
    elif(y==99):
      advertiseQR0(CurUserName)
    elif(y==100):
      advertiseQR1(CurUserName)
    elif(y==101):
      pullMembersMore(msg, settings.chatGroups[5], CurUserName)
      sleep(0.5)

  xList = re.findall(r'(?:Cs|cs|CS)\d+', msgText)
  addToCourse(xList,msg,CurUserName)
  xList = re.findall(r'(?:Ece|ece|ECE)\d+', msgText)
  addToCourse(xList,msg,CurUserName)
  xList = re.findall(r'(?:Stat|STat|STAT|stat)\d+', msgText)
  addToCourse(xList,msg,CurUserName)
  xList = re.findall(r'(?:ECON|econ|Econ)\d+', msgText)
  addToCourse(xList,msg,CurUserName)
  xList = re.findall(r'(?:MATH|Math|math|MAth)\d+', msgText)
  addToCourse(xList,msg,CurUserName)
  if CurUserName not in settings.mutes:
    if(u'小助手' not in msg['Content']):
      itchat.send_msg(settings.vT, CurUserName)
      sleep(0.5)
      itchat.send_msg(settings.vU, CurUserName)
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

itchat.run() 

