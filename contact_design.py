'''
Store contacts as a list of dictionaries. Each contact is a dictionary with keys (name: n, phone: #, email: @)
1. Add a new contact
2. Remove contact by name
3. Search contacts by name
4. List all contacts sorted alphabetically
'''

contact = []

def addContact(name = '-/-', email = '-/-' , phone = '-/-') -> None:
    for c in contact:
        if c['phone'] == phone:
            print('''\
                  Phone number is already in 
                  your contacts, check your contacts!
                  ''')
            return
    contact.append({'name': name, 'email': email, 'phone' : phone})

def removeContact(name) -> None:
    if not name:
        return
    for c in contact:
        if c['name'] == name:
            contact.remove(c)

def searchContact(name) -> None:
    for c in contact:
        if c['name'] == name:
            for w, i in c.items():
                print(w, ' : ', i)
            return
        else:
            continue
    print('name not found')
    return

def currContracts() -> None:
    for c in sorted(contact):
        print(c)

    
if __name__ == "__main__":
    while True:
        c_in = input("Add, Remove, or Search ('e' to exit) : ").lower()
        match c_in:
            case 'add' | 'a':
                name = input("What Name? : ")
                email = input("What Email? : ")
                phone = input("What Phone # ? : ")
                addContact(name, email, phone)
            case 'remove' | 'r':
                name = input("What Contact? : ")
                removeContact(name)
            case 'search' | 's':
                while True:
                    name = input("What Contact? ('e to go back) : ")
                    if name == 'e':
                        break
                    searchContact(name)
            case 'contacts' | 'c':
                currContracts()
            case 'e':
                break
        