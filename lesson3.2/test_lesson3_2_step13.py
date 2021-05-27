import time
import unittest


class TestAbs(unittest.TestCase):
    def test_one(self):
        link = "http://suninjuly.github.io/registration1.html"

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

        self.assertEqual(h1, "Congratulations! You have successfully registered!", "Плак")
        browser.quit()

    def test_two(self):
        link = "http://suninjuly.github.io/registration2.html"

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

        self.assertEqual(h1, "Congratulations! You have successfully registered!", "Плак")
        browser.quit()


from selenium import webdriver

if __name__ == "__main__":
    unittest.main()
# не забываем оставить пустую строку в конце файла
