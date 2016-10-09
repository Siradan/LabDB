text_entercommand = "Enter command: "

def main_menu():
    print("""
    1. View data
    2. Add element
    3. Change element
    4. Delete element
    5. Delete data
    6. Save data
    7. Load data
    0. Exit""")
    return  input(text_entercommand)


def sec_menu():
    print("""
        1. Group
        2. Student""")
    return input(text_entercommand)

def showList(key, list):
    if key == 0:
        text = "Group", "Students' count"
        text_shift = 20
        print "{:{}}{}".format(text[0], text_shift, text[1])
        for element in list:
            print "{:{}}{}".format(element['name'], text_shift, element['count'])
    else:
        text = "First name", "Last name", "Group"
        text_shift = 30
        print "{:{}}{:{}}{}".format(text[0], text_shift, text[1], text_shift, text[2])
        for element in list:
            print "{:{}}{:{}}{}".format(element['firstname'], text_shift, element['lastname'], text_shift, element['group'])

def getValue(key):
    if key == 0:
        return raw_input("Enter name: ")
    elif key == 1:
        return raw_input("Enter first name: "), raw_input("Enter last name: "), raw_input("Enter group: ")
    elif key == 2:
        return raw_input("Enter name: "), raw_input("Enter new name: ")
    elif key == 3:
        return raw_input("Enter first name: "), raw_input("Enter last name: "), raw_input("Enter group: "), input("Command: "), raw_input("New value: ")