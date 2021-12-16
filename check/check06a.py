"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Checkpoint 6 (a)
"""
class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.publication_year = 1

    def prompt_book_info(self):
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication_year = int(input("Publication Year: "))

    def display_book_info(self):
        print(f"\n{self.title} ({self.publication_year}) by {self.author}")

class TextBook(Book):
    def __init__(self):
        super().__init__()

        self.subject = ""

    def prompt_subject(self):
        self.subject = input("Subject: ")

    def display_subject(self):
        print(f"\nSubject: {self.subject}")

class PictureBook(Book):
    def __init__(self):
        super().__init__()

        self.illustrator = ""

    def prompt_illustrator(self):
        self.illustrator = input("Illustrator: ")

    def display_illustrator(self):
        print(f"\nIllustrated by {self.illustrator}")

def main():
    book = Book()
    book.prompt_book_info()
    book.display_book_info()
    print()

    textBook = TextBook()
    textBook.prompt_book_info()
    textBook.prompt_subject()
    textBook.display_book_info()
    textBook.display_subject()
    print()

    pictureBook = PictureBook()
    pictureBook.prompt_book_info()
    pictureBook.prompt_illustrator()
    pictureBook.display_book_info()
    pictureBook.display_illustrator()

if __name__ == "__main__":
    main()
