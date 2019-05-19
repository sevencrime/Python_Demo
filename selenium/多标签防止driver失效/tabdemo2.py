#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.set_page_load_timeout(10)
browser.set_script_timeout(10)
# url = 'http://eddid-bos-uat.ntdev.be'
url = 'https://www.google.com/'

main_win = browser.current_window_handle #得到主窗口
print(main_win)
all_win = browser.window_handles
print(all_win)

try:
    if len(all_win) == 1:
        print ('弹出保护罩')
        js = 'window.open("https://www.baidu.com");'
        browser.execute_script(js)
        # 还是定位在main_win上的
        for win in all_win:
            if main_win != win:
                print ('保护罩WIN', win, 'Main', main_win)
                browser.switch_to.window(main_win)
    browser.get(url) # 此处访问你需要的URL
    body = browser.page_source
    html = etree.HTML(body)
# 下面是你的抓取逻辑 省略
except:
    # 超时
    print ('Time out')
    # 切换新的浏览器窗口
    for win in all_win:
        if main_win != win:
            print ('WIN', win, 'Main', main_win)
            print ('切换到保护罩')
            browser.close()
            browser.switch_to.window(win)
            main_win = win
            
    js = 'window.open("https://www.baidu.com");'
    browser.execute_script(js)
    if 'time' in str(traceback.format_exc()):
        print ('页面访问超时')