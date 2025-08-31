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


def delete_contact(Contacts):
    name = str(input("contact name to delete : "))
    if name in Contacts:
        del Contacts[name]
        print(f"Contact {name} is deleted")
    else:
        print(f"Contact {name} isn't found")

def search_contact(contacts):
    name = str(input("contact name : "))
    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else :
        print(f"{name} isn't found")


def show_contacts(contacts):
    if not contacts:
        print("there is no contacts")
        return
    print("Contacts : ")
    for name in contacts:
        print(f"{name} : {contacts[name]}")


    

