import os
import unittest

import sys

sys.path.insert(0, "/Users/andrej/PycharmProjects/aSDKAppiumTests/pages")

import main_page

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Test(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'Appium'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = '42030a4df2899300'
        desired_caps['appPackage'] = 'ru.beeline.feeds_sdk'
        desired_caps['appActivity'] = 'ru.beeline.feeds_sdk.MainActivity'
        # desired_caps['appPackage'] = 'com.veon.veon.candidate'
        # desired_caps['appActivity'] = 'com.vimpelcom.veon.sdk.VeonSdkActivity'
        # desired_caps['app'] = PATH(
        #     '../../../sample-code/apps/ApiDemos/bin/ApiDemos-debug.apk'
        # )
        # desired_caps['app'] = PATH(
        #     '../../../andrej/Downloads/DemoApp_v0.1.1-debug.apk'
        # )

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_log_out(self):
        main_screen = main_page.MainPage(self.driver)
        main_screen.open_main_menu()
        main_screen.make_log_out()


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
