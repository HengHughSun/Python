#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 22:48:50/01/20/19
# Author  : Hugh Sun
# File    : article_submussions.py
# Software: 
# Description: 查看Hacker News上当前热门文章
import requests

from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print ("Status code:",r.status_code)

#处理有关每篇文章的信息
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    #对于每篇文章，都执行一个API调用
    url = ('https://hacker-news.firebaseio.com/v0/item/'+ str(submission_id) + '.json')
    submission_r = requests.get(url)
    print("Status code",submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants',0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts,key=itemgetter('comment'),reverse=Ture)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])