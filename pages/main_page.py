import sys
sys.path.insert(0, "../locators")

from main_page_locators import MainPageLocators

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    def open_main_menu(self):
        more_button = self.driver.find_element(*MainPageLocators.MORE_BUTTON)
        more_button.click()

    def make_log_out(self):
        exit_button = self.driver.find_element(*MainPageLocators.EXIT_BUTTON)
        exit_button.click()
        register_button = self.driver.find_element(*MainPageLocators.REGISTER_BUTTON)
        register_button_text = register_button.get_attribute("text")
        exp_res2 = "Зарегистрироваться"
        print(register_button_text)
