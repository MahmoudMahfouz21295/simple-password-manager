import password_functions

def create_menu():
    while True:
        application = input('Please Enter Your Application / Site Name: ')
        email = input('Please Enter Your Email: ')
        password_length = int(input('Please Enter Your Password Length [ Default 16 ]: ') or 16) 
        username = input('Please Enter Your Username [Optional]: ')
        url = input('Please Enter Your Application / Site URL [Optional]: ')

        
        password = password_functions.generate_password(password_length)
        insert_case = password_functions.insert_data(application,email,password,username,url)
        
        if insert_case == 1:
            print('You Forget Something ... Try Again')
            continue
        elif insert_case == 2:
            print('Ther is an Error With Database Connection ... Try Again')
            continue
        else:
            print('-'*31)
            print('| Your Data Has Been Inserted |')
            print('-'*31)
            print(f'Application Name: {application}')
            print(f'Email: {email}')
            print(f'Password: {password}')
            if len(username) > 0:
                print(f'Username: {username}')
            if len(url) > 0:
                print(f'URL: {url}')
            print('-'*31)
            break

        

def handel_data(data):
    if data == False:
        print('Ther is an Error With Database Connection ... Try Again')
    else:
        print('-'*31)
        for i in data:
            print(f'Application Name: {i[0]}')
            print(f'Email: {i[1]}')
            print(f'Password: {i[2]}')
            if len(i[3]) > 0:
                print(f'Username: {i[3]}')
            if len(i[4]) > 0:
                print(f'URL: {i[4]}')
            print('-'*31)


def delete_menu():
    application = input('Please Enter Your Application / Site Name: ')
    email = input('Please Enter Your Email: ')
    if input('\nAre You Sure You Want To Delete Your Data [y/N] ? ').upper() == 'Y':
        if password_functions.delete_data(application,email) == True:
            print('\n*** Your Data Has Been Deleted ***\n')
        else:
            print('Invalid Inputs')


def main_menu():
    print('# Select one choice')
    print(' - Create New Password (1)')
    print(' - Show My Passwords (2)')
    print(' - Delete My Password (3)')
    print(' - Exit (0)')
    chois = int(input('?  '))
    if chois == 0:
        print('Exiting')
        exit()
    elif chois == 1:
        print('Create New Password\n')
        create_menu()
    elif chois == 2:
        print('Show My Passwords\n')
        handel_data(password_functions.retreve_data())
    elif chois == 3:
        print('Delete My Password\n')
        delete_menu()
    else:
        print('Invalid Input')
        print('Exiting')
        exit()


main_menu()
