import codecs
import json

import requests
from lxml import etree
import time
import webbrowser


DOWNLOAD_DELAY = 1
IS_FIRSTTIME_RUN = False

class HtmlDownloader(object):
   """html下载器"""
   time.sleep(DOWNLOAD_DELAY)
   def download(self, url):
       try:
           kv = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'}
           r = requests.get(url, timeout=30, headers=kv)
           r.raise_for_status()
           r.encoding = 'utf-8'
           return r.text
       except:
           print("服务器请求失败")
           return


class HtmlParser(object):
    """html解析器"""
    def parse_search(self, html_content):
        if html_content is None:
            return
        select = etree.HTML(html_content)
        cont = select.xpath("//*[@class='search_oprate']/p/span")[0]

        if "阅读免费章节" in cont.xpath('a[1]/text()'):
            href = cont.xpath('a[1]/@href')[0]
        else:
            href = cont.xpath('a[2]/@href')[0]

        return href

    def parse_chapters(self, html_content, name):
        if html_content is None:
            return
        select = etree.HTML(html_content)
        chapters = select.xpath("//@chaptername")
        chapters_url = select.xpath('//td[@chaptername]/a/@href')

        try:
            filename = 'novel.json'
            with open(filename, encoding='utf-8') as f:
                last_chapter = json.load(f)
            index = chapters.index(last_chapter['chapter'])
        except:
            index = 0

        unrend_chapters = []
        for n, chapter in enumerate(chapters[(index+1):]):
            if '第' in chapter:
                unrend_chapters.append((chapter, chapters_url[index+1+n]))
                if IS_FIRSTTIME_RUN is False:
                    print(chapter + '\t\t\t\t' + chapters_url[index+1+n])
        return unrend_chapters, chapters[-1]


class HtmlOutputer(object):
    def output_print(self, unrend_chapters):
        first_item = unrend_chapters[0]
        url = first_item[1]
        webbrowser.open(url)


class SpiderMain(object):
    def __init__(self):
        """实例化 html下载器 、html解析器 、 html输出器"""

        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.outputer = HtmlOutputer()
        self.novel_detail = {}


    def craw(self, novel_name, root_url):
        url = root_url + novel_name + '/1.html'
        html_cont_search = self.downloader.download(url)
        chapters_url = self.parser.parse_search(html_cont_search)

        html_cont_chap =  self.downloader.download(chapters_url)
        unrend_chapters, late_chapter = self.parser.parse_chapters(html_cont_chap, novel_name)

        self.novel_detail['name'] = novel_name
        self.novel_detail['chapter'] = late_chapter


        lines = json.dumps(dict(self.novel_detail), ensure_ascii=False) + '\n'
        file = codecs.open('novel.json', 'w', encoding='utf-8')
        file.write(lines)
        file.close()

        if unrend_chapters == []:
            print("恭喜您, 您已经看完全部章节!!!")
        else:
            if IS_FIRSTTIME_RUN is False:
                print("\r\n您有{0}章没有阅读".format(len(unrend_chapters)))
                self.outputer.output_print(unrend_chapters)
            else:
                print("第一次查看或切换关键字将会保存最新章节数据^0^")


def main():
    # novel_name = input("您想要看的小说: ").strip()
    novel_name = '元尊'
    #novel_name = '剑来'
    root_url = 'http://search.zongheng.com/search/all/'

    obj_spider = SpiderMain()
    obj_spider.craw(novel_name, root_url)


if __name__ == '__main__':
   main()


