#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep
import random
from selenium.webdriver.common.keys import Keys
import os
import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from selenium.webdriver.common.by import By
def slp():
    sleep(random.randint(2,5))#延遲函數



def sign():    #打卡函數
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #每次更新chrome driver
    driver.maximize_window()#窗口最大化
    driver.get("https://paperless.cycu.edu.tw/#/login")#打卡
    slp()#調用延遲函數 等待打卡網站加載

    """
    以下登入指定網頁
    
    """
    username='' #帳號
    password='' #密碼
    driver.find_element(By.ID,'username').send_keys(username)
    slp()
    driver.find_element(By.ID,'pwd').send_keys(password)
    slp()
    driver.find_element(By.CLASS_NAME, 'loginBtn').click()#點登入按鈕
    slp()

 
    """
    確認點按鈕
    """
    driver.find_element(By.CLASS_NAME,"btn.sign.btn-primary").click()#點擊簽到
    slp()
    driver.find_element(By.CLASS_NAME,"swal2-confirm.swal2-styled").click()#點擊簽到確定
    slp()
    driver.quit()       #關閉網頁




def send_mail():

    content = MIMEMultipart()  #建立MIMEMultipart物件
    content["subject"] = "簽到打卡"  #郵件標題
    content["from"] = "a13579230@gmail.com"  #寄件者
    content["to"] = "a13579230@gmail.com" #收件者
    content.attach(MIMEText("ok"))  #郵件內容
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器

        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login("a13579230@gmail.com", "lrkshqorbqbvczga")  # 登入寄件者gmail
        smtp.send_message(content)  # 寄送郵件


if __name__ == '__main__':
    
    sign()
    send_mail()

