import time
import os
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_name("firstname").send_keys("PEtr")
    browser.find_element_by_name("lastname").send_keys("PEtr")
    browser.find_element_by_name("email").send_keys("PEtr")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '../testFile.txt')
    print(file_path)

    button_file = browser.find_element_by_name("file")
    button_file.send_keys(file_path)

    browser.find_element_by_class_name("btn").click()
finally:
    time.sleep(20)
    browser.quit()
