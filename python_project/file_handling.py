
from cryptography.fernet import Fernet

# def write():
#     key = Fernet.generate_key()
#     with open('encrypted.key2', 'wb') as x:
#         x.write(key)

# write()


def read_key():
    key = Fernet.generate_key()
    file = open('encrypted.key', 'rb')
    key = file.read()
    file.close()
    return key


login_password = input("Enter login password: ")
key = read_key() + login_password.encode()
fer = Fernet(key)


if login_password == "bardewa":

    def view():
        with open("passwords.txt", 'r') as f:               
            for y in f.readlines():
                data = y.rstrip()
                # print(data)
                user, pwd = data.split('|')
                print('User: ', fer.decrypt(user.encode()).decode(), '& Password: ',
                      fer.decrypt(pwd.encode()).decode())

    def add():
        name = input("Enter name: ")
        pwd = input("Enter password: ")
        with open("passwords.txt", 'a') as f:
            f.write(fer.encrypt(name.encode()).decode() + ' | ' + fer.encrypt(pwd.encode()).decode() + '\n')

    while True:

        theme = input(
            "Would you like to view or add the password to your account (view/add), Press e to exit?: ")

        if theme == "e":
            break
        if theme == "view":
            view()
        elif theme == "add":
            add()
        else:
            print("invalid input theme")
            continue


else:
    print("Wrong password")
