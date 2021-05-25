import time
from selenium import webdriver

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector(".first_block input.first")
    input1.send_keys("Pety")
    input2 = browser.find_element_by_css_selector(".first_block input.second")
    input2.send_keys("Pety")
    input3 = browser.find_element_by_css_selector(".first_block input.third")
    input3.send_keys("Pety")

    button = browser.find_element_by_class_name("btn-default")
    button.click()

    time.sleep(1)
    h1 = browser.find_element_by_css_selector("h1").text

    assert "Congratulations! You have successfully registered!" == h1

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла