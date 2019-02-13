#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 16:22:31/01/28/19
# Author  : Hugh Sun
# File    : novel.py
# Software: novel.py
import requests
from bs4 import BeautifulSoup

req_head = {
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding':'gzip, deflate, br',
'accept-language':'zh,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
'cache-control':'max-age=0',
'cookie':' __cfduid=d80381aec1738b356108562acb314f6811548849832; UM_distinctid=1689ea4ed27d9c-0ef7fed5b0b022-18211c0a-100200-1689ea4ed2847d; CNZZDATA1261736110=1463701021-1548849240-https%253A%252F%252Fwww.google.com%252F%7C1548849240; Hm_lvt_5ee23c2731c7127c7ad800272fdd85ba=1548849836,1548849858,1548849951; PPad_id_PP=1; Hm_lpvt_5ee23c2731c7127c7ad800272fdd85ba=1548850512; bookid=31177; chapterid=2143136; chaptername=%25u7B2C%25u56DB%25u767E%25u516B%25u5341%25u4E8C%25u7AE0%2520%25u53E6%25u4E00%25u4E2A%25u6731%25u655B; bcolor=; font=; size=; fontcolor=; width=',
'referer': 'https://www.qu.la/book/31177/',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
"""获取目录页面"""
url_base = "https://www.qu.la/book/31177/"
txt_section = "2143136.html"
r = requests.get(url_base+str(txt_section),params=req_head)
print("Status code",r.status_code)
soup = BeautifulSoup(r.text,"html.parser")
    #获取章节名称      id用#表示 .表示class                                  
section_name=soup.select('#wrapper .content_read .box_con .bookname h1')[0]        
    #获取章节文本
section_text=soup.select('#wrapper .content_read .box_con #content')[0].text             
for ss in section_text.select("script"):                #删除无用项
    ss.decompose()
    #按照指定格式替换章节内容，运用正则表达式
#section_text=re.sub( '\s+', '\r\n\t', section_text.text).strip('\r\n')          

#for ss in section_text.select("script"):                #删除无用项
 #   ss.decompose()
#按照指定格式替换章节内容，运用正则表达式
#section_text=re.sub( '\s+', '\r\n\t', section_text.text).strip('\r\n')          

print('章节名:'+str(section_name))
print("章节内容：\n"+str(section_text))
#    container
 #   chapter-list clearfix
    
  #  readerPageWrap
   # rw_3 id="reader_warp"
    #rft_1
    #reader_box
    #title/ bookinfo /content
