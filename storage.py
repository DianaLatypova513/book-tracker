import json
import os
from typing import List
from models import Book

DATA_FILE = "books.json"

def _load_books() -> List[Book]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Book.from_dict(item) for item in data]

def _save_books(books: List[Book]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([b.to_dict() for b in books], f, ensure_ascii=False, indent=2)

def add_book(book: Book) -> bool:
    books = _load_books()
    for existing in books:
        if existing.author.lower() == book.author.lower() and existing.title.lower() == book.title.lower():
            return False
    books.append(book)
    _save_books(books)
    return True

def get_all_books() -> List[Book]:
    return _load_books()

def delete_book(author: str, title: str) -> bool:
    books = _load_books()
    original_count = len(books)
    books = [b for b in books if not (b.author.lower() == author.lower() and b.title.lower() == title.lower())]
    if len(books) < original_count:
        _save_books(books)
        return True
    return False 
