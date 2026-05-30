from dataclasses import dataclass

@dataclass
class Book:
    author: str
    title: str
    rating: int
    date_read: str

    def to_dict(self) -> dict:
        return {
            "author": self.author,
            "title": self.title,
            "rating": self.rating,
            "date_read": self.date_read
        }

    @staticmethod
    def from_dict(data: dict) -> "Book":
        return Book(
            author=data["author"],
            title=data["title"],
            rating=data["rating"],
            date_read=data["date_read"]
        )