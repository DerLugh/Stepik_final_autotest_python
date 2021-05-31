from .pages.product_page import PageObject
from selenium.webdriver.common.by import By
import time



def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = PageObject(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_poduct_to_basket()
    page.solve_quiz_and_get_code()

    product_name = browser.find_element(By.CSS_SELECTOR, "h1").text
    alert_product_name = browser.find_element(By.CSS_SELECTOR, "#messages .alertinner strong").text
    assert product_name == alert_product_name

    product_price = browser.find_element(By.CSS_SELECTOR, ".product_main .price_color").text
    alert_price_name = browser.find_element(By.CSS_SELECTOR, "#messages .alert-info .alertinner strong").tex
    assert product_price == alert_price_name