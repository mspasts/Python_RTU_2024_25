# Main idea behind OOP is to have blueprint for creating objects
# We have classes that create blueprints/templates for objects
# In those templates we define the kind of data that the object can hold
# also we defien what type of operations can be performed on the object, so called methods - 
# essentially functions that are part of the class
# Objects are instances of classes

# let's see how life is without classes and objects

# let's say we have a program that manages a library
# we have books and we want to keep track of them
# we could do it like this
# we have a list of books
books = []
# and we have functions that operate on the list
def add_book(title, author, year):
    # we add dictionary to the list
    books.append({
        'title': title,
        'author': author,
        'year': year
    })

def list_books():
    for book in books:
        print(f"{book['title']} by {book['author']} ({book['year']})")

# we can add books
add_book('The Great Gatsby', 'F. Scott Fitzgerald', 1925)
add_book('To Kill a Mockingbird', 'Harper Lee', 1960)
add_book('1984', 'George Orwell', 1949)

# and list them
list_books()