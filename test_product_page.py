from .pages.product_page import PageObject
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import pytest



class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = "1234QWer56789"
        page.register_new_user(email, password)
        page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = PageObject(browser, link)
        page.open()
        page.should_not_be_success_message_item_added_text()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = PageObject(browser, link)
        page.open()
        page.add_poduct_to_basket()
        page.should_be_correct_item_in_the_basket()
        page.should_be_correct_basket_cost()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = PageObject(browser, link)
    page.open()
    page.add_poduct_to_basket()
    page.should_be_correct_item_in_the_basket()
    page.should_be_correct_basket_cost()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = PageObject(browser, link)
    page.open()
    page.add_poduct_to_basket()
    page.should_not_be_success_message_item_added_text()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = PageObject(browser, link)
    page.open()
    page.should_not_be_success_message_item_added_text()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = PageObject(browser, link)
    page.open()
    page.add_poduct_to_basket()
    page.should_message_disappeared_item_added_text()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = PageObject(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_message_basket_is_empty()
    basket_page.should_not_be_items_in_basket()