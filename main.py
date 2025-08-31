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


def main():

    contacts = load_contacts()

    while True :
        print("\n---  contact list ---")
        print("1. add contact")
        print("2. delete contact")
        print("3. search contact")
        print("4. show all contacts")
        print("5. exit")

        choose = int(input("your choose : "))

        if choose   == 1:
            add_contact(contacts)
        elif choose == 2:
            delete_contact(contacts)
        elif choose == 3:
            search_contact(contacts)
        elif choose == 4:
            show_contacts(contacts)
        elif choose == 5 :
            save_contacts(contacts)
            print("exited")
            break
        else : 
            print("Enter valid option")


if __name__ == "__main__":
    main()


