import pytest
import time
import math

@pytest.mark.parametrize('url', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, url):
        browser.implicitly_wait(10)
        link = f"https://stepik.org/lesson/{url}/step/1"
        browser.get(link)

        answer = math.log(int(time.time()))
        edit_text = browser.find_element_by_css_selector("textarea")
        print(str(answer))
        edit_text.send_keys(str(answer))

        browser.find_element_by_css_selector("button.submit-submission").click()
        answer_text = browser.find_element_by_css_selector("pre.smart-hints__hint").text
        assert answer_text == "Correct!"
