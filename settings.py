# -*- coding: UTF-8 -*-
import datetime
def init():

  global chatGroups
  global vT
  global usersDict
  global admins 
  global ADMIN
  global previousDay
  global mutes

  chatGroups =[
  u'洛杉矶租房二手万能总群',
  u'芝加哥租房二手万能总群',
  u'北美打折总群😊'
  ]

  v0= u"您好,北美加群小助手Jogchat.com创始人为您服务😊机器人托管中马上就回来哦😯\n"
  v1= u"回复 0 加洛杉矶租房二手万能总群\n"
  v2= u"回复 1 加芝加哥租房二手万能总群\n"
  v3= u"回复 2 加北美打折总群😊\n\n"
  v4= u"回复 3 关闭自动回复🐱\n"
  v5= u"回复 4 打开自动回复🐱\n\n"
  v6= u"UIUC 的校友们可以回复课程编号加课程群(如CS225, ECE120, ECON302, Math241, Stat431)\n\n"
  v12=u"回复 99 查看【北美加群小助手Jogchat.com】\n 公众号二维码加硅谷、西雅图、三番、纽约、Purdue等地群\n\n"
  v13=u"回复 100 查看 UIUC经济、统计、CS、物理、心理系大家庭小助手。\n\n"
  vT =v0+v1+v2+v3+v4+v5+v6+v12+v13
  
  usersDict = {}
  admins = []
  mutes = [] 
  ADMIN = u'超然'
  previousDay = datetime.datetime.now().day
