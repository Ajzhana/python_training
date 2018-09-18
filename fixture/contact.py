from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def submit_form_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_home_page()
        self.contact_cache = None

    def return_home_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_xpath("//div[@id='content']/form[2]/div[1]/input")) > 0):
            wd.find_element_by_xpath("//div/div[3]/ul/li[1]/a").click()

    def edit_contact(self, new_contact_data):
        wd = self.app.wd
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self,new_contact_data, index):
        wd = self.app.wd
        self.init_update_contact_by_index(index)
        self.fill_form(new_contact_data)
        self.submit_update()
        self.return_home_page()

    def edit_contact_by_id(self,new_contact_data, id):
        wd = self.app.wd
        self.init_update_contact_by_id(id)
        self.fill_form(new_contact_data)
        self.submit_update()
        self.return_home_page()

    def init_update(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def init_update_contact_by_index(self, index):
        wd = self.app.wd
        self.return_home_page()
        wd.find_element_by_xpath("//table [@id='maintable']/tbody/tr[%s]/td[8]/a/img"%(index+2)).click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.return_home_page()
        wd.find_element_by_xpath("//table [@id='maintable']/tbody/tr[%s]/td[7]/a/img"%(index+2)).click()

    def submit_update(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_cache = None

    def delete_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.init_update_contact_by_index(index)
        #wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        #wd.switch_to_alert().accept()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.init_update_contact_by_id(id)
        #wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        #wd.switch_to_alert().accept()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

    def init_update_contact_by_id(self, id):
        wd = self.app.wd
        self.return_home_page()
        wd.find_element_by_css_selector("a[href='edit.php?id=%s'] img" % (id + 2)).click()

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

    def change_contact_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def init_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def count(self):
        wd = self.app.wd
        self.return_home_page()
        return len(wd.find_elements_by_name("selected[]"))
    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cells = element.find_elements_by_css_selector("td")
                text = cells[1].text
                text2 = cells[2].text
                address = cells[3].text
                all_email = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, lastname=text, firstname=text2,
                                                  address=address, all_email_from_home_page=all_email,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.init_update_contact_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                       homephone=homephone, mobile=mobile, workphone=workphone,
                       secondaryphone=secondaryphone, email = email, email2 = email2, email3 =email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobile=mobile, workphone=workphone,
                       secondaryphone=secondaryphone)
