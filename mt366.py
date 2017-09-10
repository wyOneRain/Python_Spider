import requests
from bs4 import BeautifulSoup
import re

class Mt366:
    def __init__(self,seed_url):
        #网站入口
        self.header={ "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        self.linkQuence = linkQuence()
        self.linkQuence.addUnvisitedUrl(seed_url)

    def get_urls(self):
        while self.linkQuence.unVisitedUrlsEnmpy() is False:
            #从待访问列表中取出队尾url，并添加到已访问列表中
            visitedUrl = self.linkQuence.unVisitedUrlDeQuence()
            self.linkQuence.addVisitedUrl(visitedUrl)

            req = requests.get(url=visitedUrl, headers=self.header)
            req.encoding = 'utf-8'
            url_soup = BeautifulSoup(req.text, 'lxml')
            target_urls = url_soup.find_all(attrs={'target': '_blank'})

            for target in target_urls:
                try:
                    temp=target.get('href')
                    if 'http' not in temp:
                        temp = 'http://www.mt366.com' + temp
                    if '.xml' not in temp and 'http://www.mt366.com' in temp:
                            self.linkQuence.addUnvisitedUrl(temp)
                except:
                    continue
                    
            print("待访问个数：",self.linkQuence.getUnvistedUrlCount())
            print("已访问个数：",self.linkQuence.getVisitedUrlCount())



'''
关于队列的创建
'''
class linkQuence:
    def __init__(self):
        # 已访问的url集合
        self.visted = []
        # 待访问的url集合
        self.unVisited = []

    # 获取访问过的url队列
    def getVisitedUrl(self):
        return self.visted

    # 获取未访问的url队列
    def getUnvisitedUrl(self):
        return self.unVisited

    # 添加到访问过得url队列中
    def addVisitedUrl(self, url):
        self.visted.append(url)

    # 移除访问过得url
    def removeVisitedUrl(self, url):
        self.visted.remove(url)

    # 未访问过得队尾的url出队列
    def unVisitedUrlDeQuence(self):
        try:
            return self.unVisited.pop()
        except:
            return None

    # 保证每个url只被访问一次,插入到队首
    def addUnvisitedUrl(self, url):
        if url != "" and url not in self.visted and url not in self.unVisited:
            self.unVisited.insert(0, url)

    # 获得已访问的url数目
    def getVisitedUrlCount(self):
        return len(self.visted)

    # 获得未访问的url数目
    def getUnvistedUrlCount(self):
        return len(self.unVisited)

    # 判断未访问的url队列是否为空
    def unVisitedUrlsEnmpy(self):
        return len(self.unVisited) == 0
