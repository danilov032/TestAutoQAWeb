import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = browser.find_element_by_id("input_value").text
    print(x_value)
    y = calc(x_value)

    input_text = browser.find_element_by_id("answer")
    input_text.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()

    browser.find_element_by_class_name("btn").click()
finally:
    time.sleep(20)
    browser.quit()
