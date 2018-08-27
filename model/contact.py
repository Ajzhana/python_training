from sys import maxsize

class contact:

    def __init__(self, firstname=None, middlename=None, lastname=None,
                 company=None, home=None, address=None, mobile=None,
                 email=None, address2=None, id=None, homephone=None,
                 workphone=None, secondaryphone=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.company = company
        self.home = home
        self.address = address
        self.mobile = mobile
        self.email = email
        self.address2 = address2
        self.id = id
        self.homephone = homephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize