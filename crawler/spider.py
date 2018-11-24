import ssl
from urllib import request
import re

import os
import requests
from contextlib import closing


class Spider():
    root_url = ""
    # ? 非贪婪模式
    root_pattern = '<li class="col-md-14 col-sm-16 col-xs-12 clearfix news-box">([\s\S]*?)</li>'
    url_pattern = '<a href="([\s\S]*?)" title='
    name_pattern = 'title="([\s\S]*?)" target="'

    def __fetch_content(self, url): # 私有方法
        # https
        context = ssl._create_unverified_context()
        # 防止403
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        # http base auth 'Authorization': Basic asdfiasef

        req = request.Request(url=url, headers=headers)
        r = request.urlopen(req, context=context)
        html = r.read()
        return str(html, encoding='utf-8')

    def __fetch_image(self, url):
        filename = os.path.basename(url)
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        with closing(requests.get(url, headers=headers, stream=True)) as resp:
            with open(filename, 'wb') as fd:
                for chunk in resp.iter_content(128):
                    fd.write(chunk)


    def __analysis(self, html):
        li = re.findall(Spider.root_pattern, html)
        image_urls = []
        for sp in li:
            url = re.findall(Spider.url_pattern, sp)
            name = re.findall(Spider.name_pattern, sp)
            image_url = {'url':Spider.root_url + str(url[0]), 'name':name[0]}
            image_urls.append(image_url)
        return image_urls

    def __refine(self, image_urls):
        for img in image_urls:
            print(img)

    def run(self):
        for i in range(100, 250, 1):
            url = Spider.root_url + '/htm/piclist9/'+str(i)+'.htm'
            html = self.__fetch_content(url)
            image_urls = self.__analysis(html)
            # self.__refine(image_urls)

    def download_image(self, url):
        self.__fetch_image(url=url)


splider = Spider()
# splider.run()
splider.download_image('https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/logo_white_fe6da1ec.png')