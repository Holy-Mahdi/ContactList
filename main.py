import json
import os
from colorama import init, Fore


init(autoreset=True)

FILE_NAME = "contacts.json"


def notify(message, type="info"):
    clear_screen()
    if type == "success":
        print(Fore.GREEN + message)
    elif type == "error":
        print(Fore.RED + message)
    elif type == "warning":
        print(Fore.YELLOW + message)
    else:
        print(message)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def back_menu(user_input):
    return user_input.lower() == "menu"


def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)

    return {}


def save_contacts(contacts):
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)


def number_validation(number):
    number.strip()
    if back_menu(number):
        return

    if number.isdigit() or (number.startswith("+") and number[1:].isdigit()):
        return True
    else:
        notify("Please enter valid phone number", type="error")
        return False


def add_contact(contacts):
    name = str(input("contact name : "))
    name = name.strip()
    if back_menu(name):
        return
    while True:

        phone = input("contact number : ").strip()

        if number_validation(phone):
            break

    contacts[name] = phone

    notify(f"Contact '{name}:{phone}' added.", type="success")
    save_contacts(contacts)


def delete_contact(contacts):
    while True:
        name = str(input("contact name to delete : "))
        if back_menu(name):
            return
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
        if back_menu(name):
            return

        if name in contacts:

            notify(f"{name} : {contacts[name]}")
            return name
        else:
            print(f"{name} isn't found")


def show_contacts(contacts):
    clear_screen()
    if not contacts:
        print("there is no contacts")
        return
    print("Contacts : \n ")
    for name in sorted(contacts):
        print(f"{name} : {contacts[name]}")


def edit_contact(contacts):

    contact_name = search_contact(contacts)
    if not contact_name:
        return 0
    while True:
        print("Do you want change\n 1. name \n 2. number")
        option = int(input("Option : "))
        if option == 1:

            new_name = input("Enter New name : ")
            contacts[new_name] = contacts.pop(contact_name)
            save_contacts(contacts)
            break
        elif option == 2:
            number = input("Enter New Phone number : ")
            while True:
                if number_validation(number):
                    break
                else:
                    number = input("Enter Valid Phone number : ")
            contacts[contact_name] = number

            save_contacts(contacts)
            break
        else:
            notify("Please Enter valid Option", type="error")


def main():
    clear_screen()
    contacts = load_contacts()

    while True:

        print("\n---  contact list ---")
        print("1. add contact")
        print("2. delete contact")
        print("3. search contact")
        print("4. show all contacts")
        print("5. edit contact")
        print("6. exit")
        print("-- for back to menu enter menu ---")

        try:
            choice = int(input("your choice : "))
        except Exception:
            clear_screen()
            print("Enter number of each option")
            continue

        if choice == 1:
            add_contact(contacts)
        elif choice == 2:
            delete_contact(contacts)
        elif choice == 3:
            search_contact(contacts)
        elif choice == 4:
            show_contacts(contacts)
        elif choice == 5:
            edit_contact(contacts)
        elif choice == 6:
            save_contacts(contacts)
            print("exited")
            break
        else:
            clear_screen()
            print("Enter valid option")


if __name__ == "__main__":
    main()
