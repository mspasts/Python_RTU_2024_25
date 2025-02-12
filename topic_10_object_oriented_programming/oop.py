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
# books = []
# # and we have functions that operate on the list
# def add_book(title, author, year):
#     # we add dictionary to the list
#     books.append({
#         'title': title,
#         'author': author,
#         'year': year
#     })

# def list_books():
#     for book in books:
#         print(f"{book['title']} by {book['author']} ({book['year']})")

# # we can add books
# add_book('The Great Gatsby', 'F. Scott Fitzgerald', 1925)
# add_book('To Kill a Mockingbird', 'Harper Lee', 1960)
# add_book('1984', 'George Orwell', 1949)

# # and list them
# list_books()

# two negatives to above approach 
# we have global variable books
# also our functions are not really related to the data they operate on
# this means to use the functions we need to know how the data is structured

# we can fix the global variable problem even with functions that take data as parameter
# but we still have the problem of functions not being related to the data they operate on
# as we get more functions that work on data this becomes more and more of a problem

# let's make a class Book that will represent a book
# what properties should a book have?
# title, author, year, review, rating, borrowed, due_date, IBAN, publisher, genre, pages, language, 
# price, ISBN, edition, format, cover, series, translator, illustrator, editor, proofreader,

# for now let's stick with title, author and year, price
# we define a class with class keyword
# class name should be capitalized
# class can have properties and methods

# this is not recommended way to define properties
# class Book:
#     # we could define properties here but that is not very common
#     title = ''
#     author = ''
#     year = 0
#     price = 0

# new_book = Book()
# print(new_book.title)
# print(new_book.author)
# print(new_book.year)
# print(new_book.price)
# # i could assign values to properties like this
# new_book.title = 'The Great Gatsby'
# new_book.author = 'F. Scott Fitzgerald'
# new_book.year = 1925
# new_book.price = 15.99
# print(new_book.title)
# print(new_book.author)
# print(new_book.year)
# print(new_book.price)

# instead we use so called __init__ method to initialize properties

class Book:
    # we have so called class variables
    # also they are sort of constants
    # also they are sort of hidden
    # we can access them only from within the class
    __MIN_PRICE = 0.0
    __MAX_PRICE = 1000.0
    
    # __init__ is special method that is called when object is created
    # it is used to initialize properties
    # self is reference to the object itself
    # we can think of it as this in other languages
    # it is similar to constructor in other languages but it is called after object is created
    # __init__ is called automatically when object is created this is special method
    def __init__(self, title, author, year, price):
        # we can assign values to properties like this
        # self is a reference to the object itself NOT class but the object we just created
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    # __init__ is so called dunder method (double underscore) there are many of them
    # full list: https://docs.python.org/3/reference/datamodel.html#special-method-names

    # it could be useful to define __str__ method
    # this lets us use print(my_object) and it will print whatever we return from this method
    # only requirement is that it returns a string
    def __str__(self):
        # note we are not printing anything here we are returning a string
        # this will be used by print function
        return f"MYBOOK {self.title} by {self.author} ({self.year}) - {self.price}"

    # we can have regular methods as well with any name
    # we can define methods that operate on the object
    def display(self): # display is just a random name for the method could be anything
        print(f"{self.title} by {self.author} ({self.year}) - {self.price}")
        # if function does not return anything
        # then it returns None
        # so you might want to return something else
        # here we could return self
        return self

    # typically in OOP we have getters and setters things that change properties of the object
    # we can define methods that change properties
    # let's have a method that adjusts price

    # I could have a private clamp function
    # this method can be used only within the class not from outside
    def __clamp_price(self, price):
        if price < Book.__MIN_PRICE:
            price = Book.__MIN_PRICE
        elif price > Book.__MAX_PRICE:
            price = Book.__MAX_PRICE
        return price # note it returns the  new price

    def adjust_price(self, new_price):
        # check price # here we CLAMP the price to be within MIN_PRICE and MAX_PRICE
        # we could use other logic here
        self.price = self.__clamp_price(new_price)

        # idea is that here we could have some logic that checks if new price is valid
        # maybe we don't want price to be negative
        # maybe there is a discount on the book
        # maybe there is a tax on the book
        # maybe there is upper limit on the price
        # again I add return self so I can chain methods
        return self


    # we could add increase price method
    def increase_price(self, amount):
        # we could also check whether amount is valid maybe it is not a number
        # again we could check whether we are truly increasing the price
        # maybe we don't want to increase the price by negative amount
        # let's use clamp here as well
        self.price = self.__clamp_price(self.price + amount)
        # again I add return self so I can chain methods
        return self


# we create a new Book object by calling the class and provide values for properties
new_book = Book('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 15.99)
# we can call methods on the object
new_book.display() # note that there is no need to call any arguments self is automatically passed

# we can use the same class template to create another book
another_book = Book('To Kill a Mockingbird', 'Harper Lee', 1960, 12.99)
another_book.display()
# i can change the price of the book
another_book.price = 14.99
another_book.display()

# one more book
third_book = Book('1984', 'George Orwell', 1949, 9.99)
third_book.display()
# let's try printing third_book
print(third_book) # this will print memory address of the object without __str__ method

# let's adjust price for third_book
third_book.adjust_price(8.99) # new price
print(third_book)
# let's increase price for third_book
third_book.increase_price(5) # increase by 1
print(third_book)
# now let's increase price by negative amount
third_book.increase_price(-10) # decrease by 10
print(third_book)
# now let's increase price by negative amount
third_book.increase_price(-10) # decrease by 10 again
print(third_book)
# now let's try putting 9000 price
third_book.increase_price(9000) # increase by 9000
print(third_book)

# let's try to access __MIN_PRICE
try:
    print(third_book.__MIN_PRICE)
except AttributeError as e:
    print(e)
# turns out Python is simply renaming the variable to _Book__MIN_PRICE
# if you REALLY REALLY want to get to it you still can - usually you do not want to do this
print("I found the actual min", third_book._Book__MIN_PRICE)

# now that I have added return self I can chain methods

third_book.adjust_price(8.99).display().increase_price(5).display().increase_price(-10).display()

# now we come to topic of inheritance
# the idea is that we have some more general class and we want to create more specific class
# we can reuse the general class and add some more specific properties and methods

# let's say we have a class FictionBook

# we can inherit from Book class by providing the class name in parentheses

class FictionBook(Book):
    # here at the moment we do not add anything new but we can use FictionBook just like Book
    # note that Book __init__ method is called automatically if we do not make our own __init__ method
    # let's add some custom method
    # we could override existing methods - that is allowed
    def display(self):
        print(f"Fiction: {self.title} by {self.author} ({self.year}) - {self.price}")
        return self
    
    # we could add some new methods specific to FictionBook
    # the parent class Book does not have this method
    def is_best_seller(self):
        return self.price > 20 # logic being that expensive books are best sellers.... okkkay


# let's create a FictionBook object
fiction_book = FictionBook("Old man and the sea", "Ernest Hemingway", 1952, 10.99)
fiction_book.display() #everything works from original PARENT class

# let's try is_best_seller method
print(f"Is {fiction_book.title} best seller? {fiction_book.is_best_seller()}")

# if I really want I can create a inherited book but with some extra properties
# then a custom __init__ method is needed

class RomanceBook(Book):
    def __init__(self, title, author, year, price, love_interest):
        # I can call parent class __init__ method
        super().__init__(title, author, year, price)
        # i usually want to call super().__init__ first because it initializes properties of the parent class
        # of course I could skip this call and do it over myself
        # self.title = title
        # self.author = author
        # self.year = year
        # self.price = price
        # but that kind of defeats the purpose of inheritance
        # I can add new properties
        self.love_interest = love_interest

    # override display method - this is optional
    def display(self):
        print(f"Romance: {self.title} by {self.author} ({self.year}) - {self.price} - {self.love_interest}")
        return self
    
    # change love interest - a new method for RomanceBook
    def change_love_interest(self, new_love_interest):
        self.love_interest = new_love_interest
        return self


# often times instead of inheritance we use composition
# instead of creating a class that is a subclass of another class
# we create a class that has an object of another class
# we could even store multiple objects of another class inside our class

# let's say we have a class Library

class Library:
    def __init__(self, name, city="Rīga", books=None): # import moment DO NOT USE MUTABLE DEFAULT ARGUMENTS SUCH AS LIST
        # we could have a list of books
        # we can pass in lists of books or None
        if books is None:
            books = []
        self.books = books
        # i need to bind all passed in values to properties
        self.name = name
        self.city = city
    
    # we could add a book to the library
    def add_book(self, book):
        self.books.append(book)
        return self

    # we could list all books in the library
    def list_books(self):
        for book in self.books:
            book.display()
        return self

    # we could find a book by title
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    # we could remove a book by title
    def remove_book(self, title):
        for i, book in enumerate(self.books):
            if book.title == title:
                self.books.pop(i)
                return self
        return self
    
# let's make central library
central_library = Library("Central Library")
# let's add some books
central_library.add_book(new_book).add_book(another_book).add_book(third_book).add_book(fiction_book)
# let's print name of the library
print(central_library.name)
# let's list books
central_library.list_books()
# let's find a book 1984
book_1984 = central_library.find_book("1984") # we do not have guarantee that book is found
# so here next line could fail
# we could check if it really is from Book class
if isinstance(book_1984, Book):
    book_1984.display()
else:
    print("Book not found")

# to conclude almost everything in Python is an object

# let's see our primite types again
print(type(5)) # <class 'int'>
print(type(5.0)) # <class 'float'>
print(type("hello")) # <class 'str'>
print(type(True)) # <class 'bool'>

# so when I do something like 
print("hello".upper()) # upper is an object method

