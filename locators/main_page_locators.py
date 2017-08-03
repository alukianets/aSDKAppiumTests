from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    MORE_BUTTON = (By.ID, 'Другие параметры')
    REFRESH_BUTTON = (By.XPATH, '//android.widget.TextView[@text="Refresh"]')
    EXIT_BUTTON = (By.XPATH, '//android.widget.TextView[@text="Выйти"]')
    REGISTER_BUTTON = (By.ID, 'ru.beeline.feeds_sdk:id/button_register')
