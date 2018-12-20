# coding:utf-8
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  # 未爬取 URL 集合
        self.old_urls = set()  # 已爬取 URL 集合

    def new_url_size(self):
        """
        获取未爬取 URL 集合的大小
        :return:
        """
        return len(self.new_urls)

    def old_url_size(self):
        """
        获取已经爬取 URL 集合的大小
        :return:
        """
        return len(self.old_urls)

    def has_new_url(self):
        """
        判断是否有未爬取的 URL
        :return:
        """
        return self.new_url_size() != 0  # 这是一个判断，返回False或者True

    def get_new_url(self):
        """
        从new_urls中获取一个未爬取的 URL
        :return:
        """
        new_url = self.new_urls.pop()  # set集合的pop方法返回的是被随机移除掉的元素
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        """
         将新的 URL 添加到未爬取的 URL 集合中
        :param url:单个 URL
        :return:
        """
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        """
        将新的 URL 添加到未爬取的 URL 集合中
        :param urls:url 集合
        :return:
        """
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
