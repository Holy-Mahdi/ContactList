╔════════════════════════════════════════╗
║           Contact Manager CLI          ║
╚════════════════════════════════════════╝

A simple command-line contact manager in Python. Manage your contacts easily with add, edit, delete, search, and display functionality. Data is saved in `contacts.json` for persistence. Color-coded notifications are provided via `colorama`.

╔════════════════════════════════════════╗
║               Features                 ║
╚════════════════════════════════════════╝

- Add new contacts (name + phone number)
- Edit existing contacts (name or phone number)
- Delete contacts
- Search contacts by name
- Display all contacts sorted
- Persistent storage in `contacts.json`
- Color-coded notifications:
  - ✅ Green → Success
  - ❌ Red → Error
  - ⚠️ Yellow → Warning

╔════════════════════════════════════════╗
║             Installation               ║
╚════════════════════════════════════════╝

1. Clone the repository:

```bash
git clone <repo-url>
cd <repo-folder>
```

2. Install dependencies:

```bash
pip install colorama
```

╔════════════════════════════════════════╗
║                Usage                   ║
╚════════════════════════════════════════╝

Run the script:

```bash
python contact_manager.py
```

Interactive menu:

```
--- contact list ---
1. add contact
2. delete contact
3. search contact
4. show all contacts
5. edit contact
6. exit
-- for back to menu enter menu ---
```

- Type `menu` at any input to return to the main menu.
- Phone numbers must be numeric or start with `+` for international format.

╔════════════════════════════════════════╗
║             File Storage               ║
╚════════════════════════════════════════╝

Contacts are saved in `contacts.json` in the same directory as the script. Automatically loaded on startup and saved on any changes.

╔════════════════════════════════════════╗
║               Example                  ║
╚════════════════════════════════════════╝

```
your choice: 1
contact name: John Doe
contact number: +1234567890
Contact 'John Doe:+1234567890' added.
```

╔════════════════════════════════════════╗
║               License                  ║
╚════════════════════════════════════════╝

MIT License
