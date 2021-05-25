import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("button").click()

    browser.switch_to.alert.accept()

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    browser.find_element_by_id("answer").send_keys(y)

    browser.find_element_by_class_name("btn").click()
finally:
    time.sleep(20)
    browser.quit()
