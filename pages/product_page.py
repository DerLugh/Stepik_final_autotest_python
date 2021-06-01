from .base_page import BasePage
from .locators import ProductPageLocators

class PageObject(BasePage):
    def add_poduct_to_basket(self):
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_PAGE)
        button_add.click()


    def should_be_correct_item_in_the_basket(self):
        product_name = self.is_element_present(*ProductPageLocators.PRODUCT_TITLE)
        alert_product_name = self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_NAME)
        assert product_name == alert_product_name


    def should_be_correct_basket_cost(self):
        product_price = self.is_element_present(*ProductPageLocators.PRODUCT_PRICE)
        alert_price_name = self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_PRICE)
        assert product_price == alert_price_name