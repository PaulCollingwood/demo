""" Configure the Behave Instance on starup """

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

HOST = 'http://automationpractice.com'


def before_all(context):
    context.host = HOST
    context.webdriver = webdriver.Chrome(executable_path='./chromedriver')
    context.wait = WebDriverWait(context.webdriver, 10)


def after_all(context):
    context.webdriver.quit()



