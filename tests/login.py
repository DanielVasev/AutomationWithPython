"""
This test going to cover login functionality Search
"""

import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
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

    def test_login_positive_test(self):
        driver = self.driver

        # Creating a object fot the page Objects
        login = login_Page.LoginPage(self.driver)
        home_page = home_Page.HomePage(self.driver)
        constants = Constants()

       # Add user_name
        login.enter_username(constants.USER_NAME)
        # Add password to the field password
        login.enter_password(constants.PASSWORD)
        # Click on login button
        login.click_login_button()

        # Click on welcome button in home page
        home_page.click_welcome_button()
        # Click on logout link
        home_page.click_logout_link()

        """
         - Pause the test for a few secconds just to be visible during development process
         - remove when u finished with the test
        """
        time.sleep(3)

    def test_login_negative_invalid_user_name(self):
        driver = self.driver
        constants = Constants()
        login = login_Page.LoginPage(self.driver)

        # Add wrong username
        login.enter_username(constants.INVALID_USER)
        # Add correct password
        login.enter_password(constants.PASSWORD)
        # Click on login button
        login.click_login_button()
        # Check for validation message
        login.validation_message_present()

    def test_login_negative_invalid_password(self):
        driver = self.driver
        constants = Constants()
        login = login_Page.LoginPage(self.driver)

        # Add correct password
        login.enter_username(constants.USER_NAME)
        # Add invalid password
        login.enter_password(constants.INVALID_PASS)
        # Click login button
        login.click_login_button()
        # Validation message present
        login.validation_message_present()

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        driver.close()
        driver.quit()
        print("Test Finished!")


if __name__ == "__main__":
    unittest.main()
