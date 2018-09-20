from sys import maxsize

class Contact:

    def __init__(self, id=None, firstname=None, middlename=None, lastname=None,
                 company=None, home=None, address=None, mobile=None,
                 email=None, email2=None, email3=None, address2=None, homephone=None,
                 workphone=None, secondaryphone=None, all_phones_from_home_page=None,
                 all_email_from_home_page=None, new_group=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.company = company
        self.home = home
        self.address = address
        self.mobile = mobile
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.address2 = address2
        self.id = id
        self.homephone = homephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page
        self.new_group = new_group

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize