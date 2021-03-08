# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import datetime
from request_data import request

# cuteen 友链规则
def cuteen_get_friendlink(friendpage_link, friend_poor):
    result = request.get_data(friendpage_link)
    soup = BeautifulSoup(result, 'html.parser')
    main_content = soup.find_all('div', {"class": "col-md-4"})
    for item in main_content:
        img = item.find('img').get('src')
        link = item.find('a').get('href')
        name = item.find('div', {"class": "friends-name"}).text
        if "#" in link:
            pass
        else:
            user_info = []
            user_info.append(name)
            user_info.append(link)
            user_info.append(img)
            print('----------------------')
            try:
                print('好友名%r' % name)
            except:
                print('非法用户名')
            print('头像链接%r' % img)
            print('主页链接%r' % link)
            friend_poor.append(user_info)
