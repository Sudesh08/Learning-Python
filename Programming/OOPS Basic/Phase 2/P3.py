# 🔸 3. Book Inventory System
# Question:
# Create a class Book with attributes: title, author, copies.
# Add a method sell_copy() that reduces copies by 1 and a method to display book details.
#
# If copies become 0, print "Out of stock".

class Book:
    def __init__(self,title,author,copies):
        self.title=title
        self.author=author
        self.copies=copies

    def sell_copy(self):
        if self.copies==0:
            print("Out of stock")
        else:
            self.copies-=1

    def displaybookdetails(self):
        print(f"Title: {self.title} , Author: {self.author}")

book1=Book("Harry Potter","Jk Rollins",3)

book1.sell_copy()
book1.sell_copy()
book1.sell_copy()
book1.sell_copy()

book1.displaybookdetails()