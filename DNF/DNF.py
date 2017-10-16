from selenium import webdriver
import time
import http.cookiejar as cookielib

class DNF:
    def __init__(self):
        self._driver = webdriver.Firefox(executable_path='geckodriver.exe')
        self._userQQ='3561647063'
        self._userPwd='101WANGyu10_'

    def login(self):
        self._driver.get('http://tq.qq.com/events/dnf16/index.html?ADTAG=dnfgw')
        time.sleep(3)
        self._driver.find_element_by_class_name('bt_login').click()
        time.sleep(3)
        self._driver.switch_to.frame('ui_ptlogin')
        self._driver.find_element_by_id('switcher_plogin').click()
        self._driver.find_element_by_id('u').send_keys(self._userQQ)
        self._driver.find_element_by_id('p').send_keys(self._userPwd)
        self._driver.find_element_by_id('login_button').click()
        self._driver.switch_to.default_content()
        time.sleep(3)
        #self._driver.refresh()

    def getCookies(self):
        print(self._driver.get_cookies())
        print('')
        print(self._driver.page_source)





d=DNF()
d.login()
d.getCookies()

DNFcookies={'expiry': 9223372036854776000, 'domain': '.qq.com', 'httpOnly': False, 'secure': False, 'name': 'pgv_info', 'value': 'ssid=s7818809988', 'path': '/'}, {'expiry': 2147385600, 'domain': '.qq.com', 'httpOnly': False, 'secure': False, 'name': 'pgv_pvid', 'value': '8429872344', 'path': '/'}, {'expiry': 9223372036854776000, 'domain': '.qq.com', 'httpOnly': False, 'secure': False, 'name': '_qpsvr_localtk', 'value': '0.8392416369181104', 'path': '/'}, {'expiry': 2147385600, 'domain': '.qq.com', 'httpOnly': False, 'secure': False, 'name': 'pgv_pvi', 'value': '8992568320', 'path': '/'}, {'expiry': 9223372036854776000, 'domain': '.qq.com', 'httpOnly': False, 'secure': False, 'name': 'pgv_si', 'value': 's9986930688', 'path': '/'}, {'expiry': 9223372036854776000, 'domain': '.qq.com', 'httpOnly': False, 'secure': False, 'name': 'ptisp', 'value': 'cm', 'path': '/'}, {'expiry': 1509892113, 'domain': '.qq.com', 'httpOnly': False, 'secure': False, 'name': 'ptui_loginuin', 'value': '3561647063', 'path': '/'}, {'expiry': 1577923200, 'domain': '.qq.com', 'httpOnly': False, 'secure': False, 'name': 'pt2gguin', 'value': 'o3561647063', 'path': '/'}, {'expiry': 9223372036854776000, 'domain': '.qq.com', 'httpOnly': False, 'secure': False, 'name': 'uin', 'value': 'o3561647063', 'path': '/'}, {'expiry': 9223372036854776000, 'domain': '.qq.com', 'httpOnly': False, 'secure': False, 'name': 'skey', 'value': '@7xLcjZusy', 'path': '/'}, {'expiry': 1822660115, 'domain': '.qq.com', 'httpOnly': False, 'secure': False, 'name': 'RK', 'value': 'xg8vnorKn0', 'path': '/'}, {'expiry': 1577923200, 'domain': '.qq.com', 'httpOnly': False, 'secure': False, 'name': 'ptcz', 'value': 'c5cc19950c4cefc643dc616e1f908020f55f0061bddcd72875d8afd644068a51', 'path': '/'}, {'expiry': 1507386514, 'domain': '.tq.qq.com', 'httpOnly': False, 'secure': False, 'name': '_uin', 'value': '3561647063', 'path': '/'}, {'expiry': 1507386514, 'domain': '.tq.qq.com', 'httpOnly': False, 'secure': False, 'name': '_nick', 'value': 'OneRain', 'path': '/'}, {'expiry': 1507386514, 'domain': '.tq.qq.com', 'httpOnly': False, 'secure': False, 'name': '_avctar', 'value': 'http%3A%2F%2Fthirdqq.qlogo.cn%2Fg%3Fb%3Dsdk%26k%3DBrOsqYwsTsayvHApWW53uw%26s%3D40%26t%3D1481253499', 'path': '/'}, {'expiry': 1507301914, 'domain': '.tq.qq.com', 'httpOnly': False, 'secure': False, 'name': 'ts_last', 'value': 'tq.qq.com/events/dnf16/index.html', 'path': '/'}, {'expiry': 1522852114, 'domain': '.tq.qq.com', 'httpOnly': False, 'secure': False, 'name': 'ts_refer', 'value': 'ADTAGdnfgw', 'path': '/'}, {'expiry': 1570372114, 'domain': '.tq.qq.com', 'httpOnly': False, 'secure': False, 'name': 'ts_uid', 'value': '4790337110', 'path': '/'}

