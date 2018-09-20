import re
from random import randrange
from model.contact import Contact

def test_feilds_on_home_page(app, db):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_base = db.get_contact_list2()[0]
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_base, key=Contact.id_or_max)
    assert contact_from_home_page.firstname == contact_from_base.firstname
    assert contact_from_home_page.lastname == contact_from_base.lastname
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_base)
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_base)
    # contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    #assert contact_from_home_page.address == contact_from_edit_page.address


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda  x: x is not  None,
                                                          [contact.homephone, contact.mobile, contact.workphone, contact.secondaryphone]))))

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
