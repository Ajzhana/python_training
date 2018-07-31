

class SessionHelper:

    def __init__(self, manager):
        self.manager = manager

    def login(self, name, password):
        wd = self.manager.app.wd
        self.manager.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(name)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        wd = self.manager.app.wd
        wd.find_element_by_link_text("Logout").click()
