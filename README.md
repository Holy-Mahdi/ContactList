# 📇 Contact Manager CLI

A lightweight **Python command-line contact manager** with **add, edit, delete, search, and display** functionality.  
Contacts are stored in `contacts.json` and notifications are color-coded with `colorama`.

---

## ✨ Features

- **Add** new contacts (name + phone number)  
- **Edit** existing contacts (name or phone number)  
- **Delete** contacts  
- **Search** contacts by name  
- **Display** all contacts sorted  
- **Persistent storage** in `contacts.json`  
- **Color-coded notifications:**  
  - ✅ Green → Success  
  - ❌ Red → Error  
  - ⚠️ Yellow → Warning  

---

## ⚙️ Installation

```bash
git clone https://github.com/Holy-Mahdi/ContactList.git
cd ContactList
pip install colorama
```

---

## 🚀 Usage

Run the script:

```bash
python contact_manager.py
```

Interactive menu:

```
--- Contact Manager ---
1. Add contact
2. Delete contact
3. Search contact
4. Show all contacts
5. Edit contact
6. Exit
--- Type 'menu' anytime to return ---
```

- Phone numbers must be numeric or start with `+` for international format.

---

## 💾 File Storage

Contacts are saved in `contacts.json` in the script directory.  
- Auto-loaded on startup  
- Auto-saved on changes  

---

## 📝 Example

```
Your choice: 1
Contact name: John Doe
Contact number: +1234567890
✅ Contact 'John Doe:+1234567890' added.
```

---

## 🛡 License

MIT License
