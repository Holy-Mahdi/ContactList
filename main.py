import json
import os 

FILE_NAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r") as f:
            return json.load(f)
    
    return {}


def save_contacts(contacts):
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"w") as f:
            json.dump(contacts,f,indent=4)


def add_contact(contacts):
    name = str(input("contact name : "))
    phone = str(input("contact number : "))
    contacts[name] = phone
    print("Contact added.")