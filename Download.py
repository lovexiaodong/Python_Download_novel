
# coding=utf-8

import requests
import re

def  getCategoryList():
    response = requests.get('http://www.quanshuwang.com')
    response.encoding = 'gbk'
    result = response.text;
    reg = '<li><a href="(.*?)">(.*?)</a></li>'
    return re.findall(reg, result)

def  getSortList(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    reg = r'<a target="_blank" title="(.*?)" href="(.*?)" class="clearfix stitle">'
    novel_url_list = re.findall(reg, response.text)
    return novel_url_list

def  getNovelUrl(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    reg = '<a href="(.*?)" class="reader" title=".*?">.*?</a>'
    novel_url = re.findall(reg, result)[0]
    print(novel_url)
    response = requests.get(novel_url)
    response.encoding = 'gbk'
    result = response.text
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    chapter_url_list = re.findall(reg, result)
    return chapter_url_list

def getChapterContent(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    reg = r'style5\(\);</script>(.*?)<script type="text/javascript">'
    content = re.findall(reg, result, re.S)[0]
    content = content.replace('&nbsp;', '')
    content = content.replace('<br />', '')
    return content

for cate_url, cate_title in getCategoryList():
    print(cate_url, cate_title)
    for novel_title, novel_url in getSortList(cate_url):
        print("正在下载小说：", novel_title)
        file = open("C:/Users/Administrator.O2BV9G0TI9RXZHF/Desktop/python/novel/" + novel_title + ".txt", "a")
        for chapter_url, chapter_title in getNovelUrl(novel_url):
            print('正在下载章节 ：', chapter_title)
            file.write("\n")
            file.write(chapter_title + "\n\n")
            file.flush()
            content = getChapterContent(chapter_url)
            file.write(content)
            file.flush()
            print('章节 ：', chapter_title + "下载完成")
        file.close()
        print("小说：", novel_title, "   下载完成")