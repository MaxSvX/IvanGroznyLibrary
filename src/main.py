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
    pass
def find_book_by_author(books:list[Book],authors:str)->list[Book]:
    pass
def sort_by_rating(books:list[Book], increse:bool = True)->list[Book]:
    pass
def main():
    array = [Book("Чехов","Лошадинная фамилия","","",12,4.8),
             Book("Эдвард Радзинский","Тайны фpанцузской империи","","",12,4.5),
             Book("Лермантов","Странный человек","","",12,4.0)]
main()