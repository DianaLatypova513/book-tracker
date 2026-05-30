from typing import List, Dict
from models import Book

def average_rating(books: List[Book]) -> float:
    if not books:
        return 0.0
    total = sum(b.rating for b in books)
    return round(total / len(books), 2)

def stats_by_author(books: List[Book]) -> Dict[str, dict]:
    stats = {}
    for book in books:
        author = book.author
        if author not in stats:
            stats[author] = {"count": 0, "total_rating": 0}
        stats[author]["count"] += 1
        stats[author]["total_rating"] += book.rating
    for author in stats:
        stats[author]["avg_rating"] = round(stats[author]["total_rating"] / stats[author]["count"], 2)
        del stats[author]["total_rating"]
    return stats