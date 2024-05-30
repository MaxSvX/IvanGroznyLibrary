class Book:
    def __init__(self, author:str,name:str, preface:str, text:str,  age_restrictrictions:int, rating:float):
        if age_restrictrictions <= 0:
            raise Exception("ОШИБКА! ВОЗРАСТ")
        self.author = author
        self.preface = preface
        self.text = text
        self.name = name
        self.age_restrictrictions = age_restrictrictions
        self.rating = rating
    def get_text(self):
        return self.text
    
def find_book_by_name(books:list[Book], name:str)->Book:
    for book in books:
        if book.name == name:
            return book
def print_book(book:Book):
    if book:
        print((f"Автор: {book.author}\n" 
                f"Название книги: {book.name}\n" 
                f" Предисловие: {book.preface}\n" 
                f"Текст: {book.text}\n" 
                f"Возраст: {book.age_restrictrictions}\n" 
                f"Рэйтинг: {book.rating}\n"))       
def find_book_by_author(books:list[Book],authors:str)->list[Book]:
    massive = []
    for book in books:
        if book.author == authors:
            massive.append(book)
    return massive
def sort_by_rating(books:list[Book], high_rating:float)->list[Book]:
    if high_rating > Book:
        print(Book)
def main():
    array = [Book("Чехов","Лошадинная фамилия","","",12,4.8),
             Book("Эдвард Радзинский","Тайны фpанцузской империи","","",12,4.5),
             Book("Лермантов","Странный человек","","",12,4.0),
             Book("Чехов", "Дядя Ваня","","",12,5.0)]
    print_book(find_book_by_name(array,"Дядя Ваня"))        
main()