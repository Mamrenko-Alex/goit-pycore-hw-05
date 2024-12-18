def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Incorrect input."
    return inner

contacts = {}

@input_error
def add_contact(name, phone):
    if not name or not phone:
        raise ValueError()
    contacts[name] = phone
    return f"Contact {name} added."

@input_error
def change_contact(name, phone):
    if name not in contacts:
        raise KeyError()
    contacts[name] = phone
    return f"Contact {name} updated."

@input_error
def get_contact(name):
    return contacts[name]

print(add_contact("John", "123456789"))
print(get_contact("John"))
print(change_contact("John", "987654321"))
print(get_contact("John"))
