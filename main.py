from datetime import datetime
from models import Book
from storage import add_book, get_all_books, delete_book
from stats import average_rating, stats_by_author

def input_book_data():
    print("\nДобавление новой книги")
    author = input("Автор: ").strip()
    title = input("Название: ").strip()
    while True:
        try:
            rating = int(input("Оценка (1-5): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Оценка должна быть от 1 до 5")
        except ValueError:
            print("Введите целое число")
    date_read = input("Дата прочтения (ГГГГ-ММ-ДД): ").strip()
    try:
        datetime.strptime(date_read, "%Y-%m-%d")
    except ValueError:
        print("Неверный формат, будет использована сегодняшняя дата")
        date_read = datetime.today().strftime("%Y-%m-%d")
    return Book(author, title, rating, date_read)

def show_all_books():
    books = get_all_books()
    if not books:
        print("\nСписок книг пуст.")
        return
    print("\nСписок книг:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book.author} — «{book.title}» | Оценка: {book.rating} | Прочитана: {book.date_read}")

def show_average_rating():
    books = get_all_books()
    avg = average_rating(books)
    print(f"\nСредняя оценка всех книг: {avg}")

def show_author_stats():
    books = get_all_books()
    if not books:
        print("\nНет книг для статистики.")
        return
    stats = stats_by_author(books)
    print("\nСтатистика по авторам:")
    for author, data in stats.items():
        print(f"{author}: {data['count']} книг, средняя оценка {data['avg_rating']}")

def delete_book_ui():
    author = input("Введите автора книги для удаления: ").strip()
    title = input("Введите название книги для удаления: ").strip()
    if delete_book(author, title):
        print("Книга удалена.")
    else:
        print("Книга не найдена.")

def main():
    while True:
        print("\n=== Трекер прочитанных книг ===")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            book = input_book_data()
            if add_book(book):
                print("Книга успешно добавлена!")
            else:
                print("Такая книга уже есть в списке (дубликат).")
        elif choice == "2":
            show_all_books()
        elif choice == "3":
            show_average_rating()
        elif choice == "4":
            show_author_stats()
        elif choice == "5":
            delete_book_ui()
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()