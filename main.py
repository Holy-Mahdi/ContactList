import json
import os 

FILE_NAME = "contacts.json"



def notify(message):
    clear_screen()
    print(message)




def clear_screen():
    os.system("cls" if os.name =="nt" else 'clear')


def back_menu(user_input):
    if user_input == "menu" :
        clear_screen()
        return True
    
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
    name = name.strip()
    if back_menu(name) : return
    while True : 
        try : 
            phone = int(input("contact number : "))
            break
        except:
            print("Invalid Phone number")

        
    contacts[name] = phone
   
    notify(f"Contact '{name}:{phone}' added.")
    save_contacts(contacts)


def delete_contact(contacts):
    while True: 
        name = str(input("contact name to delete : "))
        if back_menu(name) : return
        if name in contacts:
            del contacts[name]
            
            notify(f"Contact {name} is deleted")
            break
        else:
            print(f"Contact {name} isn't found")
    save_contacts(contacts)

def search_contact(contacts):
    while True: 
        name = str(input("contact name : "))
        if back_menu(name) : return
        
        if name in contacts:
            
            notify(f"{name} : {contacts[name]}")
        else :
            print(f"{name} isn't found")
            



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
            choice = int(input("your choice : "))
        except:
            clear_screen()
            print("Enter number of each option")
            continue
            

        if choice   == 1:
            add_contact(contacts)
        elif choice == 2:
            delete_contact(contacts)
        elif choice == 3:
            search_contact(contacts)
        elif choice == 4:
            show_contacts(contacts)
        elif choice == 5 :
            save_contacts(contacts)
            print("exited")
            break
        else : 
            clear_screen()
            print("Enter valid option")


if __name__ == "__main__":
    main()


