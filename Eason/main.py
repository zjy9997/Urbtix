# This is a sample Python script.
import os
import pickle

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# 主页
url = "https://ticket.urbtix.hk/internet/"
# 登录页
login_url = "https://ticket.urbtix.hk/internet/login/memberLogin"
# 抢票目标页
target_url = 'https://ticket.urbtix.hk/internet/eventSearch/keyword?keyword=FWD+%E5%AF%8C%E8%A1%9B%E4%BF%9D%E9%9A%AA%E5%91%88%E7%8D%BB+FEAR+AND+DREAMS+EASON+CHAN+IN+CONCERT+%28%E5%8A%A0%E5%A0%B4%29'

'''
date1209 = 'tr[1]'
date1210 = 'tr[2]'
date1211 = 'tr[3]'
date1213 = 'tr[4]'
date1214 = 'tr[5]'
date1216 = 'tr[6]'
date1217 = 'tr[7]'
date1218 = 'tr[8]'
date1220 = 'tr[9]'
date1221 = 'tr[10]'
date1222 = 'tr[11]'
date1224 = 'tr[12]'
date1225 = 'tr[13]'
date1226 = 'tr[14]'
date1228 = 'tr[15]'
date1229 = 'tr[16]'
date1230 = 'tr[17]'
date1231 = 'tr[18]'
'''

date0102 = 'tr[1]'
date0103 = 'tr[2]'
date0106 = 'tr[3]'
date0107 = 'tr[4]'

date = date0102  # 想抢的日期

"""
    def keep_cookie(self):
        try:
            cookies = pickle.load(open("cookies.pkl", "rb"))  # 载入cookie
            #print(cookies)
            for cookie in cookies:
                if cookie.get('name') == 'Auth_Token':
                    s = str(cookie.get('value')).split("-")
                    new_Auth_Token = str(int(s[0])+5) + '-' + s[1] + '-' + s[2]
                    cookie_dict = {
                        'domain': cookie.get('domain'),  # 必须有，不然就是假登录
                        'httpOnly': cookie.get('httpOnly'),
                        'name': cookie.get('name'),
                        'path': cookie.get('path'),
                        'secure': cookie.get('secure'),
                        'value': new_Auth_Token
                    }
                else:
                    cookie_dict = {
                        'domain': cookie.get('domain'),  # 必须有，不然就是假登录
                        'httpOnly': cookie.get('httpOnly'),
                        'name': cookie.get('name'),
                        'path': cookie.get('path'),
                        'secure': cookie.get('secure'),
                        'value': cookie.get('value')
                    }
                print(cookie_dict)
                self.driver.get(target_url)
                self.driver.delete_all_cookies()
                self.driver.add_cookie(cookie_dict)
                pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))
            print('###载入new_Cookie###')
        except Exception as e:
            print(e)
"""


class Concert:
    def __init__(self):
        self.status = 0  # 状态,表示如今进行到何种程度
        self.login_method = 1  # {0:模拟登录,1:Cookie登录}自行选择登录方式
        self.driver = webdriver.Chrome(executable_path='./chromedriver')  # 默认Chrome浏览器

    def set_cookie(self):
        print(self.driver.title)
        self.driver.get(login_url)
        time.sleep(10)
        while self.driver.title == 'URBTIX':
            self.driver.get(login_url)
            print("please wait for the login")
            time.sleep(1)
        if self.driver.title == '城市售票網':
            self.driver.get(login_url)
        print("###请点击登录###")
        self.driver.find_element(By.XPATH, '//*[@class="login-member-login-tbl"]/tbody/tr[3]/td[4]/input').send_keys('username')
        self.driver.find_element(By.XPATH, '//*[@class="login-member-login-tbl"]/tbody/tr[4]/td[4]/input').send_keys('password')

        while self.driver.title == '城市售票網 - 會員登入':
            time.sleep(1)
        print("###扫码成功###")
        pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))
        print("###Cookie保存成功###")
        self.driver.get(target_url)

    def get_cookie(self):
        try:
            cookies = pickle.load(open("cookies.pkl", "rb"))  # 载入cookie
            print(cookies)
            for cookie in cookies:
                cookie_dict = {
                    'domain': cookie.get('domain'),  # 必须有，不然就是假登录
                    'httpOnly': cookie.get('httpOnly'),
                    'name': cookie.get('name'),
                    'path': cookie.get('path'),
                    'secure': cookie.get('secure'),
                    'value': cookie.get('value')
                }
                print(cookie_dict)
                self.driver.add_cookie(cookie_dict)
            print('###载入Cookie###')
        except Exception as e:
            print(e)

    def login(self):
        if self.login_method == 0:
            self.driver.get(login_url)
            # 载入登录界面
            print('###开始登录###')

        elif self.login_method == 1:
            if not os.path.exists('cookies.pkl'):
                # 如果不存在cookie.pkl,就获取一下
                self.set_cookie()
            else:
                self.driver.get(target_url)
                self.driver.delete_all_cookies()
                self.get_cookie()

    def enter_concert(self):
        """打开浏览器"""
        print('###打开浏览器，进入大麦网###')
        # self.driver.maximize_window()           # 最大化窗口
        # 调用登陆
        self.login()  # 先登录再说
        print("###登录成功###")

    def isElementExist(self, element):
        flag = True
        browser = self.driver
        try:
            browser.find_element(By.XPATH, element)
            return flag

        except:
            flag = False
            return flag

    def finish(self):
        self.driver.quit()

    def buy_ticket(self):
        while not self.isElementExist('//*[@class="event-list-normal-tbl"]/tbody/tr[2]/td[5]/div[1]/div[1]'):
            # self.driver.refresh()
            print("please wait for botton1")
            time.sleep(0.5)
        if self.isElementExist('//*[@class="event-list-normal-tbl"]/tbody/tr[2]/td[5]/div[1]/div[1]'):
            self.driver.find_element(By.XPATH,
                                     '//*[@class="event-list-normal-tbl"]/tbody/tr[2]/td[5]/div[1]/div[1]').click()
        else:
            print("can't find botton1")

        while not self.isElementExist('//*[@id="evt-perf-items-tbl"]/tbody/' + date + '/td[6]/div[1]/img[1]'):
            print("please wait for botton2")
            # self.driver.refresh()
            time.sleep(0.5)

        if self.isElementExist('//*[@id="evt-perf-items-tbl"]/tbody/' + date + '/td[6]/div[1]/img[1]'):
            self.driver.find_element(By.XPATH,
                                     '//*[@id="evt-perf-items-tbl"]/tbody/' + date + '/td[6]/div[1]/img[1]').click()
        else:
            print("can't find botton2")

        while not self.isElementExist(
                '//*[@id="ticket-select-tbl"]/tbody/tr[1]/td[3]/table/tbody/tr[1]/td[2]/select/option[5]'):
            print("please wait for botton3")
            time.sleep(0.5)

        if self.isElementExist(
                '//*[@id="ticket-select-tbl"]/tbody/tr[1]/td[3]/table/tbody/tr[1]/td[2]/select/option[5]'):
            self.driver.find_element(By.XPATH,
                                     '//*[@id="ticket-select-tbl"]/tbody/tr[1]/td[3]/table/tbody/tr[1]/td[2]/select/option[5]').click()
        else:
            print("can't find botton3")

        while not self.isElementExist('//*[@class="perf-purchase-btn-blk"]/div[1]/div[1]/div[1]'):
            print("please wait for botton4")
            time.sleep(0.5)

        if self.isElementExist('//*[@class="perf-purchase-btn-blk"]/div[1]/div[1]/div[1]'):
            self.driver.find_element(By.XPATH, '//*[@class="perf-purchase-btn-blk"]/div[1]/div[1]/div[1]').click()
        else:
            print("can't find botton4")

        while not self.isElementExist('//*[@class="ticket-review-confirm-btn"]/div[1]/div[1]'):
            print("please wait for botton5")
            time.sleep(0.5)

        if self.isElementExist('//*[@class="ticket-review-confirm-btn"]/div[1]/div[1]'):
            self.driver.find_element(By.XPATH, '//*[@class="ticket-review-confirm-btn"]/div[1]/div[1]').click()
        else:
            print("can't find botton5")


if __name__ == '__main__':
    try:
        #while time.strftime("%Y%m%d-%H%M%S") != "20221006-100000":
        #    print("wait")
        #    time.sleep(0.5)
        con = Concert()  # 具体如果填写请查看类中的初始化函数
        con.enter_concert()  # 打开浏览器
        con.buy_ticket()

    except Exception as e:
        print(e)
        con.finish()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
