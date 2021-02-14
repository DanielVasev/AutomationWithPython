from selenium.webdriver.common.keys import Keys
from Pages_Objects import locators

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        # Locator we need for this page

        self.userName_textBox_id = "txtUsername"
        self.password_textBox_id = "txtPassword"
        self.login_button_id = "btnLogin"

        # All of the actions in the page

    def enter_username(self, username):
        self.driver.find_element_by_id(self.userName_textBox_id).clear()
        self.driver.find_element_by_id(self.userName_textBox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textBox_id).clear()
        self.driver.find_element_by_id(self.password_textBox_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_id("btnLogin").send_keys(Keys.RETURN)


