import datetime
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename="magic library.log", level=logging.INFO
)

BOOKS = [
    {
        "name": "Dune",
        "author": "Frank Herbert",
        "genre": "Science fiction",
        "pages": 896,
        "entry_added": datetime.datetime(2023, 11, 15, 12, 13, 14),
    },
    {
        "name": "Dune Messiah",
        "author": "Frank Herbert",
        "genre": "Science fiction",
        "pages": 256,
        "entry_added": datetime.datetime(2023, 12, 16, 20, 0, 11),
    },
    {
        "name": "Murder on the Orient Express",
        "author": " Agatha Christie",
        "genre": "Crime novel",
        "pages": 256,
        "entry_added": datetime.datetime(2021, 10, 30, 7, 43, 28),
    },
]

def list_of_all_books():
    for each_book in BOOKS:
        print(
            f"'{each_book['name']}' by {each_book['author']} is ",
            f"'{each_book['genre']} and has {each_book['pages']} pages")
        print('=' * 85)
    logger.info("user has viewed a list of all books")


def add_new_book():
    new_book_name = input("Enter a book name (required field): ")
    logger.info("User entered a book name ")
    author_new_book = input("Enter author book (required field): ")
    logger.info("User entered author book ")
    genre_new_book = input("Enter genre book (required field): ")
    logger.info("User entered genre book ")
    pages_new_book = input("Number of pages in the book (optional field): ")
    logger.info("User entered number of pages in the book ")
    pages_new_book = int(pages_new_book) if pages_new_book.isdigit() else None
    entry_added = datetime.datetime.now()

    new_book = {
        "name": new_book_name,
        "author": author_new_book,
        "genre": genre_new_book,
        "pages": pages_new_book,
        "entry_added": entry_added
    }

    BOOKS.append(new_book)
    print("New book added successfully")



