from model.contact import contact

def test_del_contact(app):
    app.contact.delete_contact()