import json


class book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def get_details(self):
        status = "Borrowed" if self.is_borrowed else "available"
        print(
            f"This book {self.title} written by {self.author} with isbn :{self.isbn} is {status} ")

    def check_out(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
            print(f"You have checked out '{self.title}' ")
        else:

            self.is_borrowed == True
            print(f"{self.title} is already borrowed")

    def return_book(self):
        if self.is_borrowed == True:
            self.is_borrowed = False
            print("You have succesfully returned the book")
        else:
            print("This book was not checked out.")

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "is_borrowed": self.is_borrowed
        }


class Library:
    def __init__(self):
        self.books = []

    def add_books(self, book_to_add):
        self.books.append(book_to_add)
        print(f"'{book_to_add.title}' was added to the library!")

    def display_books(self):
        if not self.books:
            print("The library has no books right now.")
        else:
            for item in self.books:
                item.get_details()

    def find_book(self, title):
        for item in self.books:
            if item.title.lower() == title.lower():
                return item
        return None

    def save_to_json(self, filename="library.json"):
        book_list = [b.to_dict() for b in self.books]
        with open(filename, "w") as file:
            json.dump(book_list, file, indent=4)
        print("Library data saved successfully")

    def load_from_json(self, filename="library.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)  # Reads list of dicts from JSON file

                self.books = []  # Reset list before loading
                for item in data:
                    # Recreate each book object using dictionary values
                    new_book = book(
                        item["title"], item["author"], item["isbn"])
                    new_book.is_borrowed = item["is_borrowed"]
                    self.books.append(new_book)

            print("Library data loaded successfully!")
        except FileNotFoundError:
            # If the file doesn't exist yet (first time running), start fresh
            self.books = []


my_library = Library()
my_library.load_from_json()
book1 = book("Atomic habits", "Mark twain", "1234")

while True:

    choice = input(
        "What do you want to do?\n1.Add a book.\n2.Display all books.\n3.Borrow a book.\n4.Return a book.\n5.Exit.\nEnter your choice 1-5:")
    if choice == "1":
        title = input("Enter the title of the book:")
        author = input("Enter the author of this book:")
        isbn = input("Enter the isbn of the book: ")
        book_to_add = book(title, author, isbn)
        my_library.add_books(book_to_add)

    elif choice == "2":
        my_library.display_books()

    elif choice == "3":
        search_title = input(
            "Enter the title of the book that you want to borrow: ")
        found_book = my_library.find_book(search_title)
        if found_book:
            found_book.check_out()
        else:
            print("Book not found")

    elif choice == "4":
        search_title = input("Enter the book you want to return: ")
        found_book = my_library.find_book(search_title)
        if found_book:
            found_book.return_book()
        else:
            print("Book not found in library")
    elif choice == "5":
        print("Goodbye")
        my_library.save_to_json()
        break
    else:
        print("Invalid choice")
