from model.contact import contact
import random
import string
import os.path
import jsonpickle
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usege()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    contact(firstname=random_string("firstname", 10),
            middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10),
            company=random_string("company", 10),
            home=random_string("home", 10),
            address=random_string("address", 10),
            mobile=random_string("mobile", 10),
            email=random_string("email", 10),
            address2=random_string("address2", 10))

    for i in range(3)
   ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    #jsonpickle.set_encoder_options("json", indent=2)
    #out.write(jsonpickle.encode(testdata))