from options import menu, store_contact, edit_contact, remove_contact, show_all, show_name
from termcolor import colored


def start():
    option = menu()
    print('What would you like to do?')
    while option != 'q':
        if option == '1':
            store_contact()
        if option == '2':
            edit_contact()
        if option == '3':
            remove_contact()
        if option == '4':
            show_all()
        if option == '5':
            show_name()
        option = menu()

    exit()


if __name__ == '__main__':
    pin = int(input(colored('Enter Pin: ', 'green')))
    if pin == 1924:
        print(colored('Successful!', 'blue'))
        start()
    print(colored('Wrong', 'red'))
