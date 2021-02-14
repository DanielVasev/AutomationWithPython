"""
This test going to cover login functionality Search
"""

import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from Pages_Objects import login_Page, home_Page
from Util.constants import Constants


class LoginPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 1. Initialise webdriver
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())

        # 2. Smart wait timer for element to appear
        cls.driver.implicitly_wait(10)

        # 3. Maximise the browser screen
        cls.driver.maximize_window()

        # 4. Open the browser and navigate to URL..
        cls.driver.get(Constants.BASE_URL)

    def test_login_functionality(self):
        driver = self.driver
        login = login_Page.LoginPage(driver)
        home_page = home_Page.HomePage(driver)
        constants = Constants()

        login.enter_username(constants.USER_NAME)
        login.enter_password(constants.PASSWORD)
        login.click_login_button()

        home_page.click_welcome_button()
        home_page.click_logout_link()

        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Finished!")


if __name__ == "__main__":
    unittest.main()
