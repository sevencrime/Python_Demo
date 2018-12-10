# coding = utf-8

#导入selenium包
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


#初始化webdriver的chromedriver
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver')
#打开页面
driver.get('C:/Users/Administrator/Desktop/demo/2.html')
# driver.maximize_window()

#alert
# driver.find_element_by_id("btn_alert").click()
# time.sleep(1)
# str_alert = driver.switch_to_alert()
# print(str_alert.text)
# str_alert.accept()  #accept() 点击alert中的确定
# time.sleep(3)
# driver.find_element_by_id("demo").send_keys("sssss")

#confirm
# time.sleep(1)
# driver.find_element_by_id("btn_confirm").click()
# confirm = driver.switch_to_alert()
# print(confirm.text)
# confirm.dismiss()
# print(confirm.text)

#prompt
# driver.find_element_by_id("btn_prompt").click()
# prompt = driver.switch_to_alert()
# print(prompt.text)
# time.sleep(3)
# prompt.send_keys("onedi")
# time.sleep(2)
# prompt.accept()

#单选框多选框
# driver.find_element_by_xpath("//input[@value='Bike']").click()
# car = driver.find_element_by_xpath("//input[@value='Car']")
# #is_selected()  判断是否选中,返回一个bool值
# s= car.is_selected()
# print(s)
# # car.click()
# if s == False :
#     car.click()
#     time.sleep(3)
# else:
#     time.sleep(3)
#     print("该选项已选中")

# 多选框选多个
# checkboxs = driver.find_elements_by_xpath("//input[@type = 'checkbox']")
# checkboxs[1].click()
# checkboxs[2].click()

#<input type="email" name="email">
# time.sleep(3)
# driver.find_element_by_name("email").send_keys("onedi")
# time.sleep(5)

#上传文件
driver.find_element_by_xpath('//input[@type="file"]').send_keys('F:/downloads/apps/bilibili.apk')
time.sleep(1)
filename = driver.find_element_by_xpath('//input[@type="file"]')

#调用JS修改元素属性
#document.querySelectorAll(selectors),返回一个list对象,
# selectors 是一个由逗号连接的包含一个或多个CSS选择器的字符串
js = 'document.querySelectorAll("select")[0].style.display="block";'
driver.execute_script(js)
sel = driver.find_element_by_tag_name('select')
#使用此方法获取select中的元素
Select(sel).select_by_value('opel') 






time.sleep(5)
print("结束脚本")
driver.quit()