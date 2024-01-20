from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
import threading



def re_now(arg1):
    text_name = datetime.datetime.now().strftime('doc\\' + '%Y-%m-%d-%H-%M-%S') + '.txt'
    start_time = time.time()  # 记录开始时间
    end_time = start_time + 600  # 计算结束时间点

    # 创建浏览器实例
    driver = webdriver.Chrome()

    # 进入指定的直播间
    driver.get('https://live.douyin.com/' + arg1)
    # 定位直播间弹幕互动消息框，并获取其元素对象
    interact_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="webcast-chatroom___messages"]')))  # 聊天及其他消息
    interactbox_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="webcast-chatroom___bottom-message"]')))  # 新进直播间消息
    oldval = ""
    oldboxval = ""
    # 循环获取弹幕互动消息内容
    while True:
        time.sleep(1)
        # 从弹幕互动消息框中获取弹幕互动消息内容
        current_time = time.time()  # 获取当前时间
        if current_time >= end_time:  # 判断是否达到结束时间点
            break  # 如果已经超过了结束时间点，则跳出循环
        interact_msg = interact_box.text
        if oldval != interact_msg:
            #  print("弹幕聊天关注送礼消息")
            print(interact_msg.replace(oldval, ""))
            file1 = open(text_name, 'w', encoding='utf-8')
            #  file1 = open(text_name,'a',encoding='utf-8')
            file1.write(interact_msg.replace(oldval, "") + '\n')
            file1.close()
            oldval = interact_msg
        print(arg1)

def thread_1(lid):
    t1 = threading.Thread(target=re_now, kwargs={'arg1': lid})
    t1.start()
