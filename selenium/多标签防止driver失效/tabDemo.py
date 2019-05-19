#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import traceback

def browser(driver, url):
	# driver.get 保护罩,防止打开浏览器超时
	try:
		main_win = driver.current_window_handle	#得到主窗口句柄

		if len(driver.window_handles) == 1 : 
			# 打开保护罩
			js='window.open("https://www.baidu.com");'
			driver.execute_script(js)
			for handle in driver.window_handles:
				if handle == main_win:
					# print('保护罩WIN', handle, '\nMain', main_win)
					driver.switch_to.window(handle)

		driver.get(url)

	except Exception as e:
		print(e)
		# 关闭当前超时页面
		for handle in driver.window_handles:
			if handle != main_win:
			    driver.switch_to_window(handle)
			    browser(driver, url)
			else:
				print("切换保护罩")
				driver.close()


driver = webdriver.Chrome()
driver.set_page_load_timeout(20)
driver.set_script_timeout(20)
url = 'http://eddid-bos-uat.ntdev.be'
# url = 'https://www.google.com/'
browser(driver, url)

print(driver.current_url)


