#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 20:45:28/01/19/19
# Author  : Hugh Sun
# File    : python_repos.py
# Software: python_repos.py
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS 

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)#status_code告诉我们请求是否成功了（状态码200表示成功）

# 将API存储在一个变量中
response_dict = r.json()
print(response_dict.keys())
print("Total repositories:",response_dict['total_count'])

# 研究有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

names, polt_dits = [], []
#print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    #Get the project description, if one is available
    description = repo_dict['description']
    if not description:
        description = "No description provided."
    
    polt_dit = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url']
    }
    polt_dits.append(polt_dit)
####print('\nName:',#repo_dict['name'])
####print('Owner:',#repo_dict['owner']['login'])
####print('Stars:',#repo_dict['stargazers_count'])
####print('Repository:',#repo_dict['html_url'])
####print('Description:',#repo_dict['description'])
# Make visualization.
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000


wm = pygal.Bar(my_config,style=my_style)

wm.title = "Most-Starred Python project on Github"
wm.x_labels = names
wm.x_title = 'Items'
wm.y_title = 'Stars'

wm.add('Stars',polt_dits)

wm.render_to_file('python_repos.svg')