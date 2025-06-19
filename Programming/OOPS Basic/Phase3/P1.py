# 🔸 1. Library Management System (Using List of Objects)
# Question:
# Create a Book class with attributes: title, author, and is_available.
# Create a Library class that can:
# Add a book
# Display all books
# Lend a book (mark as unavailable)
# Return a book (mark as available)
# Use a list to manage multiple Book objects.

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        # self.is_available=True

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author},"

    def __repr__(self):
        return self.__str__()

class Library:
    def __init__(self):
        self.books=[]
        self.isTittleMatch=False

    def addBook(self,title,author):
        newBook=Book(title,author)
        self.books.append(newBook)
        print(f"Book {title} added to library")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            print(book)
    # Why here id is printing

    def lend_books(self,title):
        for book in self.books:
            if book.title == title:
                self.isTittleMatch=True
                if book.is_available:
                    book.is_available=False
                    print(f"You have borrowed {book.title}")
                    break
                else:
                    print(f"{book.title} is not available")
        if not self.isTittleMatch:
            print(f'"{title}" not found in the library.')



    def return_book(self,title):
        for book in self.books:
            if book.title == title:
                if not  book.is_available:
                    book.is_available=True
                    print(f"Thank you for returning {title}")
                else:
                    print(f"{title} is wrong book")


library = Library()
library.addBook("The Alchemist", "Paulo Coelho")
library.addBook("To Kill a Mockingbird", "Harper Lee")
library.display_books()
library.lend_books("To Kill a ngbird")
library.return_book("the")

# 🔸 2. Inheritance – Vehicle and Car
# Question:
# Create a base class Vehicle with attributes: brand, speed.
# Create a subclass Car that inherits from Vehicle and adds an attribute fuel_type.
# Add methods to display details in both classes. Use super() where needed.
#
# 🔸 3. Shopping Cart System with Total Calculation
# Question:
# Create a Product class with name, price, and quantity.
# Create a Cart class that:
#
# Adds products to the cart
#
# Calculates total price
#
# Displays items in the cart
#
# Use composition (a list of Product objects inside Cart).
#
# 🔸 4. Private Attributes and Getter/Setter
# Question:
# Create an Account class with private attribute __balance.
# Add:
#
# Method to deposit/withdraw
#
# Getter and setter for balance using property decorators (@property, @balance.setter)
#
# A rule: balance cannot be set below 1000
#
# 🔸 5. Employee Management with Class Variables
# Question:
# Create an Employee class with:
#
# Class variable employee_count
#
# Instance variables: name, salary
#
# A class method to show total number of employees
#
# Each time an object is created, employee_count should increase.