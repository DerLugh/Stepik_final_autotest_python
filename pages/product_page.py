from .base_page import BasePage
from .locators import ProductPageLocators

class PageObject(BasePage):
    def add_poduct_to_basket(self):
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_PAGE)
        button_add.click()