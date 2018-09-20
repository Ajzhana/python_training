from model.contact import Contact
import random


def test_del_contact_from_group(app, db):
    if len(db.get_group_list()) == 0:
        app.contact.init_contact_creation()
        app.contact.fill_form(Contact(firstname="Test", new_group="label=1"))
        app.contact.submit_form_creation()
    app.contact.select_group()
    old_contacts = db.get_group_list()
    contact1 = random.choice(old_contacts)
    app.contact.delete_contact_from_group_id(contact1.id)
    new_contacts = db.get_group_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact1)
    assert old_contacts == new_contacts
