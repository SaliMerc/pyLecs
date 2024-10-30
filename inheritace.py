# creating a library management system
# this is the parent class
class Books:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}"

# this is the child class : super method is for inheritance here
class LibraryBook(Books):
    def __init__(self, title, author, isbn, copies_available):
        super().__init__(title, author)
        self.isbn = isbn
        self.copies_available = copies_available
    def borrow_book(self):
        if self.copies_available>0:
            self.copies_available-=1
            return f"{self.title} borrowed. Copies left are {self.copies_available}"
        else:
            return f"No copies of {self.title} are available"

    def return_book(self):
        self.copies_available+=1
        return f"{self.title} returned. Copies left are {self.copies_available}"
book1=LibraryBook("Giften hands", "Ben Carson", 78337, 20)
print(book1.display_info())
print(book1.borrow_book())
print(book1.return_book())