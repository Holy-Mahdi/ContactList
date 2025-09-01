import json
import os 

FILE_NAME = "contacts.json"

def back_menu(user_input):
    if user_input == "menu" :
        clear_screen()
        return True

def clear_screen():
    os.system("cls" if os.name =="nt" else 'clear')

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r") as f:
            return json.load(f)
    
    return {}


def save_contacts(contacts):
    with open(FILE_NAME,"w") as f:
        json.dump(contacts,f,indent=4)


def add_contact(contacts):
    name = str(input("contact name : "))
    if back_menu(name) : return
    phone = str(input("contact number : "))
    contacts[name] = phone
    clear_screen()
    print(f"Contact '{name}:{phone}' added.")
    save_contacts(contacts)


def delete_contact(contacts):
    while True: 
        name = str(input("contact name to delete : "))
        if back_menu(name) : return
        if name in contacts:
            del contacts[name]
            clear_screen()
            print(f"Contact {name} is deleted")
            break
        else:
            print(f"Contact {name} isn't found")
    save_contacts(contacts)

def search_contact(contacts):
    while True: 
        name = str(input("contact name : "))
        if back_menu(name) : return
        
        if name in contacts:
            clear_screen()
            print(f"{name} : {contacts[name]}")
        else :
            print(f"{name} isn't found")
            search_contact(contacts)



def show_contacts(contacts):
    clear_screen()
    if not contacts:
        print("there is no contacts")
        return
    print("Contacts : \n ")
    for name in contacts:
        print(f"{name} : {contacts[name]}")


def main():
    clear_screen()
    contacts = load_contacts()

    while True :
        
        print("\n---  contact list ---")
        print("1. add contact")
        print("2. delete contact")
        print("3. search contact")
        print("4. show all contacts")
        print("5. exit")
        print("-- for back to menu enter menu ---")

        try : 
            choose = int(input("your choose : "))
        except:
            clear_screen()
            print("Enter number of each option")
            continue
            

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
            clear_screen()
            print("Enter valid option")


if __name__ == "__main__":
    main()


