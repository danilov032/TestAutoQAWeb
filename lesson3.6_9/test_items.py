import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_for_the_presence_of_the_basket(browser):
    browser.get(link)
    basket = browser.find_elements_by_css_selector("button.btn-add-to-bask")
    assert len(basket) > 0, "Кнопки нет :("
    time.sleep(30)
