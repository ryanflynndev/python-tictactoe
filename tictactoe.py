result = input("please enter a value:")

def user_choice():

    choice = 'WRONG'
    acceptable_range = range(0,10)
    within_range = False

    while choice.isdigit() == False or within_range == False :
        choice = input("Please enter a number (0-10): ")
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
        if choice.isdigit():
            if(int(choice in acceptable_range)):
                within_range = True
            else:
                print('Sorry the number must be 0-10!')
                within_range = False

    return int(choice)


user_choice()