# coding:utf-8
from DataOutput import DataOutput
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from UrlManager import UrlManager

class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        # 添加入口 URL
        self.manager.add_new_url(root_url)
        # 判断 url 管理器中是否有新的 url，同时判断抓取了多少个 url
        while(self.manager.has_new_url() and self.manager.old_url_size() < 100):
            try:
                # 从 URL 管理器获取新的 url
                new_url = self.manager.get_new_url()
                # HTML下 载器下载网页
                html = self.downloader.download(new_url)
                # HTML 解析器抽取网页数据
                new_urls, data = self.parser.parser(new_url, html)
                # 将抽取的 url 添加到 URL 管理器中
                self.manager.add_new_urls(new_urls)
                # 数据存储器存储文件
                self.output.store_data(data)
                print("已经抓取%s个链接" % self.manager.old_url_size())
            except Exception as e:
                print("crawl failed")
                # 数据存储器将文件输出成指定格式
        self.output.output_html()

if __name__ == "__main__":
    spider_man = SpiderMan()
    spider_man.crawl("http://baike.baidu.com/view/284853.htm")
