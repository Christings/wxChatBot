# -*- coding:utf-8 -*-

from wxChatBot.handler import MonitorHandler, XiaodouHandler,TuringHandler
from wxChatBot.wxChatBot import WxChatBot

if __name__ == '__main__':
    chatbot = WxChatBot(hot_reload=True)

    monitor = MonitorHandler()
    chatbot.register_handler(monitor)

    # xiaodou_key = 'aGRvc0d3bGh1dGZrPW89RVFMdC9wY1VRWkJRQUFBPT0'
    # xiaodou = XiaodouHandler(xiaodou_key)
    # chatbot.register_handler(xiaodou)

    turling_key='26987b82e566438b8177ae54cb81e0b2'
    turling_user='wechat.robot'
    turling=TuringHandler(turling_key,turling_user)
    chatbot.register_handler(turling)

    chatbot.run()
