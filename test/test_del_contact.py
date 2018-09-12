from model.contact import Contact
import random

def test_del_contact(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.contact.init_contact_creation()
        app.contact.fill_form(Contact(firstname="Test"))
        app.contact.submit_form_creation()
    old_contacts = db.get_group_list()
    contact1 = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact1.id)
    new_contacts = db.get_group_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact1)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)