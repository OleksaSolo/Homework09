CONTACTS = {}

def input_error(func):
    def inner(*args):
        try:
            result = add(*args)
        except KeyError:
            return f"Enter Key"
        print(result)
        if result == "KeyError":
            return f"Enter Key"
        else:
            return result
    return inner    
    # if func == "add":
    #     return f"Enter Key"
    # if text_error == "ValueError":
    #     return f"Enter Value"
    # if text_error == "IndexError":
    #     return f"Enter Index"
    # else:
    #     return f"All OK."
    
@input_error
def add(*args):
    name = args[0]
    phone = args[1]
    print(CONTACTS)
    CONTACTS[name] = phone
    print(CONTACTS)
    return f"Add success {name} {phone}"

def end(*args):
    return f"Good bye!"


def no_command(*args):
    return "Unknown command"


def parser(text: str) -> tuple[callable, tuple[str]|None]:
    #print(text.startswith(text))
    if text.startswith("add"):
        return add, text.replace("add", "").strip().split()
    elif text.startswith("exit") or text.startswith("close") or text.startswith("good bye"):
        #return end, text.replace("end", "").strip().split()
        return end, ""
    return no_command, None
    

def main():
    while True:
        user_input = input("Input command: hello, add name phone, change name phone, phone name, show all, good bye/close/exit>>>")
        command, data = parser(user_input)
        result = command(*data)
        print(result)
        if result == "Good bye!":
            break
    
if __name__ == "__main__":
    main()

