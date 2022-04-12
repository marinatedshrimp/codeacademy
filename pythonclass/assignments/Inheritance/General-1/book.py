class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def view(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")

a = Book("The Great Tinfoil Massacre", "Elizabeth Olsen", 27.99)
a.view()