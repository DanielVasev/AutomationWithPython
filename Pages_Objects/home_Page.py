class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = "welcome"
        self.logout_link_linkText = "//a[contains(text(),'Logout')]"

    def click_welcome_button(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout_link(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()

    def get_driver(self, title):
        title = self.driver.title()
