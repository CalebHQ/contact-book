from database_manager import create_contact, update_contact, delete_contact, select_all, select_name
from texttable import Texttable
from termcolor import colored


def menu():
    print('+' + '*'*40 + '+')
    print('|' + ' '*14 + colored('Contact ', 'red') +
          colored('Book', 'green') + ' '*14 + '|')
    print('+' + '='*40 + '|')
    print('|' + ' 1. Create New Contact' + ' '*18 + '|')
    print('|' + ' 2. Update Contact' + ' '*22 + '|')
    print('|' + ' 3. Delete Contact' + ' '*22 + '|')
    print('|' + ' 4. Show All Contacts' + ' '*19 + '|')
    print('|' + ' 5. Show All Contacts Based on Name' + ' '*5 + '|')
    print('|' + ' q. Quit' + ' '*32 + '|')
    print('+' + '*'*40 + '+')
    return input('> ')


def store_contact():
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")
    address = input(f"Enter {fname}'s Physical Street Address: ")
    suburb = input('Enter Suburb: ')
    postcode = input('Enter Postcode: ')
    state = input('Enter State: ')
    country = input('Enter Country: ')
    relationship = input(f'Enter your Relationship with {fname}: ')

    create_contact(fname, lname, phone, email, address, suburb,
                   postcode, state, country, relationship)

    print(colored('Successful!', 'blue'))


def edit_contact():
    id = input('Enter Contact ID: ')
    column = input('Which attribute do you want to change? (column): ')
    value = input('Change to: ')

    update_contact(column, value, id)

    print(colored('Successful!', 'blue'))


def remove_contact():
    column = input('Which attribute do you want to delete? (column): ')
    value = input('With what value: ')

    delete_contact(column, value)

    print(colored('Successful!', 'blue'))


def show_all():
    t = Texttable()
    t.set_cols_align(["c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"])
    t.set_cols_dtype(['i', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't'])
    t.set_cols_width([2, 10, 11, 12, 25, 20, 10, 8, 5, 11, 14])
    data = select_all()
    for i in range(len(data)):
        id, fname, lname, phone, email, address, suburb, postcode, state, country, relationship = data[
            i]
        t.add_rows([['ID', 'First Name', 'Last Name', 'Phone Number', 'Email', 'Street Address', 'Suburb', 'Postcode', 'State', 'Country', 'Relationship'], [
                   id, fname, lname, phone, email, address, suburb, postcode, state, country, relationship]])
    print(t.draw())


def show_name():
    name = input('Enter First Name: ')
    data = select_name(name)

    t = Texttable()
    t.set_cols_align(["c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"])
    t.set_cols_dtype(['i', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't'])
    t.set_cols_width([2, 10, 11, 12, 25, 20, 10, 8, 5, 11, 14])
    for i in range(0, len(data)):
        id, fname, lname, phone, email, address, suburb, postcode, state, country, relationship = data[
            i]
        t.add_rows([['ID', 'First Name', 'Last Name', 'Phone Number', 'Email', 'Street Address', 'Suburb', 'Postcode', 'State', 'Country', 'Relationship'], [
                   id, fname, lname, phone, email, address, suburb, postcode, state, country, relationship]])
    print(t.draw())
