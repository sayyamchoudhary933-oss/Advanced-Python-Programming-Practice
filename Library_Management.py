# Write a program to create a simplified Library Management System using object-oriented programming principles in Python. 
# This system should manage books and patrons (library users), allowing for basic operations such as
#  adding new books, registering patrons, borrowing books, and returning books. 

# BOOK
# PATRON
# LIBRARY

#------------------BOOK CLASS--------------------------
# BOOK ID
# BOOK TITLE
# AUTHOR NAME
# NUMBER OF COPIES
# LIST OF PATRONS WHO BORROWED THE BOOK


#--------------------PATRON CLASS---------------------
# PATRON ID
# PATRON NAME

#------------------- LIBRARY CLASS----------------------
# A COLLECTION OF BOOKS OBJECTS
# A COLLECTION OF PARON OBJECTS

#----------FUNCTIONAS-----------
# adding new books, registering patrons, borrowing books, and returning books. 

class Book:
   
    # Syntax of constructor 
    def __init__(self,book_id,title,author,copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies
        self.borrowed_by = []


 


# creating the object of Bokk class book2 = Book(101,"Python Programming","Guido",5)
# book1 = Book(101,"Python Programming","Guido",5)
# book2 = Book(102,"Java Programming ","XYZ",3)

#-------------------------------------------------------------------------------------
#                                Patron class
#-------------------------------------------------------------------------------------

class Patron:

    def __init__(self,patron_id,name):
        self.patron_id=patron_id
        self.name=name
        

# patron1=Patron(1,"Aniket")

#-------------------------------------------------------------------------------------
#                                Library class
#-------------------------------------------------------------------------------------

class Library:
    def __init__(self):
        self.books=[]
        self.patrons=[]
    
    #-------------------------------------------------------------------------------------
    #                               ADD BOOK
    #-------------------------------------------------------------------------------------
    def add_book(self):
        book_id = int(input("Enter the book id "))
        title = input("Enter the title")
        author = input("Enter the Author Name")
        copies = int(input("Enter number of copies"))
        book = Book(book_id,title,author,copies)
        self.books.append(book)
        print("Book Added Successfully")

        
    #-------------------------------------------------------------------------------------
    #                               ADD PATRONS
    #-------------------------------------------------------------------------------------

    def register_patron(self):
        patron_id= int(input("Enter the Patron ID "))
        name=input(" Enter the name of patron")

        patron =Patron(patron_id,name)
        self.patrons.append(patron)

            
    #-------------------------------------------------------------------------------------
    #                                DISPLAY BOOKS
    #-------------------------------------------------------------------------------------

    def display_books(self):
        if len(self.books)==0:
            print(" No Books Available")
            return
        print("\n =================Book list=======================")
        for book in self.books:
            print("Book ID :", book.book_id)
            print("Title :", book.title)
            print("Author :", book.author)
            print("Copies :", book.copies)
        if len(book.borrowed_by)==0:
            print("Issued to:None")
        else:
             print("Issued to:None",book.borrowed_by)
        print("-----------------------------------------------------")


    
            
    #-------------------------------------------------------------------------------------
    #                                MAIN PROGRAM
    #-------------------------------------------------------------------------------------

library= Library()
    
while True:
        print("1. ADD BOOK")
        print("2. REGISTER THE PATRON")
        print("3. DISPLAY BOOKS")
        print("4. DISPLAY PATRONS ")
        print("0.Exit")
        
        choice=int(input("Enter your choise"))
        if choice == 1:
            library.add_book()
        elif choice == 2:
            library.register_patron()
        elif choice ==3:
            library.display_books()
        elif choice == 0:
            print("Thank You")
            break
        else:
            print("invalid choice")
