
def user_choice():

    choice = 'WRONG'
    acceptable_range = range(0,10)
    within_range = False

    while choice.isdigit() == False or within_range == False :
        choice = input("Please enter a number (0-10): ")
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
        if choice.isdigit():
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print('Sorry the number must be 0-10!')
                within_range = False

    return int(choice)


class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author 
        self.pages = pages
    def __str__(self):
        return f'{self.title} by {self.author}'

    def __len__(self):
        return self.pages

    def __del__(self):
        print("DELETED")

b = Book('Elon Musk', "Ashlee Vance", 350)

print(len(b))