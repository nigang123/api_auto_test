import os
import time

import action as action
from selenium import webdriver
from Common.baseui import baseUI
from Common.read_excel import *
import pytest
from selenium.webdriver import ActionChains



class TestMall:
    def test_start(self,driver):
        #确定chromedriver.exe的位置
        driver_path = os.path.join(os.path.dirname(__file__), "../chromedriver/chromedriver.exe")
        #打开浏览器
        # driver = webdriver.Chrome(driver_path)
        # driver.maximize_window()  # 最大化浏览器
        # driver.set_page_load_timeout(10)  # 网页加载超时为10s
        # driver.set_script_timeout(10)  # js脚本运行超时10s
        # driver.implicitly_wait(10)  # 元素查找超时时间10s
        base = baseUI(driver)
        driver.get('https://www.damai.cn/')
        #d定位登录按钮并点击
        driver.find_element_by_xpath('//span[@data-spm="dlogin"]').click()
        f = driver.find_element_by_xpath('//iframe[@id="alibaba-login-box"]')
        driver.switch_to_frame(f)
        # 定位用户名输入框//input[@aria-label="请输入手机号或邮箱"]
        a = driver.find_element_by_xpath('//input[@aria-label="请输入手机号或邮箱"]')
        # 输入用户名'18121256785'
        a.send_keys('18121256785')
        # 定位密码输入框
        b = driver.find_element_by_xpath('//input[@aria-label="请输入登录密码"]')
        # 输入密码' '
        b.send_keys('aa741258')

        # 定位登录并点击//button[@type="submit"]
        base.click('点击登录按钮', '//button[@type="submit"]')

        #滑块
        d= driver.find_element_by_xpath('//span[@id="nc_1_n1z"]')
        action = ActionChains(driver)
        action.click_and_hold(d).perform()
        action.reset_actions()
        action.move_by_offset(300, 40).perform()
        time.sleep(2)


        # # 定位登录并点击//button[@type="submit"]
        # base.click('点击登录按钮','//button[@type="submit"]')