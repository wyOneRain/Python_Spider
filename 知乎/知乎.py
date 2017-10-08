"""
参考：https://github.com/xchaoinfo/fuck-login
运行环境：Win10，Python3.5.2
"""

import requests
from bs4 import BeautifulSoup
import re
import time
import os.path
from PIL import Image
import http.cookiejar as cookielib

class ZhiHu:
    def __init__(self):
        #填写用户名以及密码
        self.userName = '********'
        self.userPwd='*********'
        self.session = requests.session()
        self.header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    def use_cookie(self):
        self.session.cookies=cookielib.LWPCookieJar(filename='cookies')
        try:
            self.session.cookies.load(ignore_discard=True)
        except:
            print("Cookie 未能加载")

    def isLogin(self):
        self.use_cookie()
        url= "https://www.zhihu.com/settings/profile"
        login_code = self.session.get(url, headers=self.header, allow_redirects=False).status_code
        if login_code == 200:
            return True
        else:
            return False

    def get_xsrf(self):
        #获取参数_xsrf
        req = requests.get('https://www.zhihu.com',headers = self.header)
        soup=BeautifulSoup(req.text,'lxml')
        _xsrf = soup.find_all('input',attrs={'name': '_xsrf'})[0].get('value')
        return _xsrf

    def get_captcha(self):
        #获取验证码,然后手动输入
        t = str(int(time.time()*1000))
        captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
        r =self.session.get(captcha_url,headers = self.header)
        with open('captcha.jpg','wb') as f:
            f.write(r.content)
            f.close()
        try:
            im = Image.open('captcha.jpg')
            im.show()
            im.close()
        except:
            print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
        captcha =input("Please input the captcah\n>")
        return captcha

    def login(self):
        """判断用户名是否为电话号码"""
        if re.match(r'\d{11}$',self.userName):
            login_url='http://www.zhihu.com/login/phone_num'
            login_data={'_xsrf':self.get_xsrf(),
                  'password':self.userPwd,
                  'phone_num':self.userName,}
        else:
            login_url='https://www.zhihu.com/login/email'
            login_data = {'_xsrf': self.get_xsrf(),
                    'password': self.userPwd,
                    'email': self.userName,}
        login_respond = self.session.post(url=login_url,headers=self.header,data=login_data)
        login_code = login_respond.json()

        #r: 1表示登陆失败，0则为成功
        if login_code['r'] == 1:
            print("登录失败:"+login_code['msg'])
            #获取验证码并输入
            login_data['captcha'] = self.get_captcha()
            login_respond = self.session.post(url=login_url, headers=self.header, data=login_data)
            login_code = login_respond.json()
            #返回登陆之后提示信息
            print(login_code['msg'])
        else:
            print('登陆成功')

        #保存登陆后的cookie
        self.session.cookies.save()
        self.session.close()