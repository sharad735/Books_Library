class Library:
    def __init__(self,listofbooks):
        self.books = listofbooks
    
    def displayavailablebooks(self):
        print("Books present in the library are : ")
        for book in self.books:
            print("\t *" +book)
    def borrowbook(self,bookname):
        if bookname in self.books:
            print(f"you have issued {bookname}.please keep it safe and return it in 30 days")
            self.books.remove(bookname)
            return True
        else:
            print("Sorry! This book has either been unavailable or has already been issued to someone else,please wait until the book is available")
            return False
    def returnbook(self,bookname):
        self.books.append(bookname)
        print(f"Thanks for returning/adding {bookname} book.")


class Student:
    
    def requestbook(self):
        self.books = input("Enter a name of the book you want to borrow: ") 
        return self.books

    def returnbook(self):
        self.books = input("Enter the name of the book you want to return or Add: ")
        return self.books

if __name__ == "__main__":
    centrallibrary = Library(["Algorithm","Django","clrs","python"])
    student = Student()
    centrallibrary.displayavailablebooks()
    while(True):
        WelcomeMsg = ''' **** Welcome to central library!****\n
        Choose an option:
        1.List all the books available.
        2.Request a book.
        3.Return/Add a book.
        4.Exit the library.'''
        print(WelcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centrallibrary.displayavailablebooks()
        elif a == 2:
            centrallibrary.borrowbook(student.requestbook())
        elif a == 3:
            centrallibrary.returnbook(student.returnbook())
        elif a == 4:
            print("Thanks for choosing central library!.Have a great day.")
            exit()
        else:
            print("Invalid choice!")
