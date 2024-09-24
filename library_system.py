# Task 1: Library System Enhancement: Sharpen your skills in managing and modifying data within tuples 
# and lists.

#Problem Statement: You are maintaining a library system where each book is stored as a tuple within 
# a list. Your task is to update this system by adding new books and ensuring no duplicates.

#Existing Library Data:

# library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# - Add functionality to insert new books into `library`. 
# Ensure that adding a duplicate book is handled appropriately.

def add_books(library, book):
    if book in library:
        print(f"The book '{book[0]}' is already in the library. ")
    else:
        library.append(book)
        print(f"The book '{book[0]}' has been added to the library. ")

def display_books(library):
    for book in library:
        print(f"Title: {book[0]} - Author: {book[1]} ")

def main():
    library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
    while True:
        print("Menu")
        print("1: Add books")
        print("2: Display Library")
        print("3: Quit")

        choice = input("Choose an option 1-3: ")
        if choice == "1":
            title = input("Enter a new book: ")
            author = input("Enter author of the book: ")
            book = (title, author)
            add_books(library, book)
        elif choice == "2":
            display_books(library)
        elif choice == "3":
            print("Exiting system. ")
            break
        else:
            print("Invalid input. Try again. ")
if __name__ == "__main__":
    main()