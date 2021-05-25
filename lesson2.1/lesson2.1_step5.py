import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = browser.find_element_by_id("input_value").text

    y = calc(x_value)

    input_text = browser.find_element_by_id("answer")
    input_text.send_keys(y)

    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_class_name("btn").click()

finally:
    time.sleep(20)
    browser.quit()
