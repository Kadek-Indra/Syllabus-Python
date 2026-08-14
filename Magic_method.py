class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

    def __len__(self):
        return len(self.title)

    def __eq__(self, other):
            return self.title == other.title and self.author == other.author and self.year == other.year

    def __add__(self, other):
            return self.year + other.year

    def __lt__(self, other):
        return self.year < other.year

book1 = Book("Avengers", "Stan Lee", 1963)
book2 = Book("Batman", "Bob Kane", 1939)
book3 = Book("Avengers", "Stan Lee", 1963)

print(book1)
print(len(book1))
print(book1 == book3)
print(book1 + book2)
print(book1 < book2)