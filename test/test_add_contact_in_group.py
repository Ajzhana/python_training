
from model.contact import Contact


def test_add_contact_in_group(app, db, json_contacts):
    cont = json_contacts
    old_contacts = db.get_contact_list3()
    app.contact.init_contact_creation()
    app.contact.fill_form(cont)
    app.contact.submit_form_creation()
    #assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list3()
    old_contacts.append(cont)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)