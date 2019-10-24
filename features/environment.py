""" Configure the Behave Instance on starup """

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

HOST = 'http://automationpractice.com'


def find_by_xpath(self, xpath):
    return self._web_driver_wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))


def before_all(context):
    context.host = HOST
    context.webdriver = webdriver.Chrome(executable_path='./chromedriver')
    context.wait = WebDriverWait(context.webdriver, 10)


def after_all(context):
    context.webdriver.quit()



