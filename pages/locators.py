from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_INPUT_REPASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators():
    BUTTON_PAGE = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "h1")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini .btn-group .btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
