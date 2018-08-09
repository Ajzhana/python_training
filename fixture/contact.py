

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def submit_form_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def edit_contact(self, new_contact_data):
        wd = self.app.wd
        self.init_update()
        self.fill_form(new_contact_data)
        self.submit_update()

    def init_update(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def submit_update(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

    def delete_contact(self):
        wd = self.app.wd
        self.init_update()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()


    def fill_form(self, contact):
        wd = self.app.wd
        self.change_contact_value("firstname", contact.firstname)
        self.change_contact_value("middlename", contact.middlename)
        self.change_contact_value("lastname", contact.lastname)
        self.change_contact_value("company", contact.company)
        self.change_contact_value("address", contact.address)
        self.change_contact_value("home", contact.home)
        self.change_contact_value("mobile", contact.mobile)
        self.change_contact_value("email", contact.email)
        self.change_contact_value("address2", contact.address2)
        self.submit_form_creation()

    def change_contact_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def init_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()