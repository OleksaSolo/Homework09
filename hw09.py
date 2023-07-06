CONTACTS = {}

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return "Enter Key"
        except IndexError as e:
            return "You are entering an invalid command."
    return inner    
    
@input_error
def add(*args):
    name = args[0]
    phone = args[1]
    #print(CONTACTS)
    CONTACTS[name] = phone
    #print(CONTACTS)
    return f"Add success {name} {phone}"

def hello(*args):
    return f"How can I help you?"

@input_error
def change(*args):
    name = args[0]
    phone = args[1]
    #print(CONTACTS)
    if CONTACTS.get(name) != None:
        CONTACTS.pop(name)
        CONTACTS[name] = phone
        #print(CONTACTS)
        return f"Update success {name} {phone}"
    else:
        return f"Notebook have not {name}"

@input_error
def phone(*args):
    name = args[0]
    #print(CONTACTS)
    if CONTACTS.get(name) != None:
        #CONTACTS.pop(name)
        phone = CONTACTS[name]
        #print(CONTACTS)
        return f"{name} have phone number: {phone}"
    else:
        return f"Notebook have not {name}"

def show_all(*args):
    result = "\nNotebook \n"
    if len(CONTACTS) > 0:
        sort_contacts = sorted(CONTACTS.items(), key=lambda item: item[0])
        print(sort_contacts)
        for key, value in sort_contacts:
        #for key, value in CONTACTS.items():
            result += "name: " + key + "  phone: " + value + "\n"
    else:
        result += "is blank"
    return result

def end(*args):
    return f"Good bye!"

def no_command(*args):
    return "Unknown command. I don't understand. Please, input rigth command."


def parser(text: str) -> tuple[callable, tuple[str]|None]:
    input_start = text.strip().split()
    input_command = input_start[0].lower()
    #print(input_start[0].lower())
    if input_command == "good" or input_command == "show":
        if len(input_start) > 1:
            input_command += " " + input_start[1].lower()
    #print(input_command)
    if input_command == "add":
        return add, text.replace(input_start[0], "").strip().split()
    elif input_command == "hello":
        return hello, ""
    elif input_command == "change":
        return change, text.replace(input_start[0], "").strip().split()
    elif input_command == "phone":
        return phone, text.replace(input_start[0], "").strip().split()
    elif input_command == "show all":
        return show_all, ""
    elif input_command == "exit" or input_command == "close" or input_command == "good bye":
        #return end, text.replace("end", "").strip().split()
        return end, ""
    return no_command, ""
    

def main():
    print("Input command: hello, add name phone, change name phone, phone name, show all, good bye/close/exit")
    while True:
        user_input = input(">>>")
        command, data = parser(user_input)
        result = command(*data)
        print(result)
        if result != "Good bye!":
            print("\nInput command: hello, add name phone, change name phone, phone name, show all, good bye/close/exit")
        else:
            break
    
if __name__ == "__main__":
    main()
    
