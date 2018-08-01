from model.contact import contact

def test_del_contact(app):
    app.session.login("admin", "secret")
    app.contact.delete_contact()
    app.session.logout()