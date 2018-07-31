from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session2 import SessionHelper
from fixture.contact import ContactHelper
from fixture.manager import Manager

class Application:
    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
       # self.session = SessionHelper(self)
       # self.contact = ContactHelper(self)
        self.manager = Manager(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()