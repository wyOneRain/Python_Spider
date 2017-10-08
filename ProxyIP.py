"""
参考：http://blog.csdn.net/c406495762/article/details/72793480
运行环境：Win10,Python3.5.2
"""


import requests
from bs4 import BeautifulSoup
from lxml import etree

class PronxyHost:
    def __init__(self):
        self.page=1
        #第一页的URL为：www.xicidaili.com/nn/1,所以通过修改self.page改变页数
        self.Proxy_Urls='http://www.xicidaili.com/nn/%d' %self.page
        self.session=requests.session()
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

    def get_ipList(self):
        respond = self.session.get(self.Proxy_Urls,headers=self.headers)
        bf1_ip_list=BeautifulSoup(respond.text,'lxml')
        #获取ip_list
        tables=bf1_ip_list.find_all('table')

        ipList=[]

        #通过循环打印列表信息
        #tr为每行信息
        for tr in BeautifulSoup(str(tables),'lxml').find_all('tr'):
            ipInfo = []
            #td为一行当中的列信息，因为包括不需要的信息，通过list筛选出来
            for td in BeautifulSoup(str(tr),'lxml').find_all('td'):
                ipInfo.append(td.getText())
            try:
                #从list中取出ip,端口，协议类型
                ip=ipInfo[1]+"#"+ipInfo[2]+"#"+ipInfo[5]
                ipList.append(ip)
            except:
                continue
        return ipList