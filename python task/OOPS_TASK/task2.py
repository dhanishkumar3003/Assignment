class BookStore:
    NoOfBooks = 0
    
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks += 1
    
    def Display(self):
        print(f"Book Name: {self.Name}")
        print(f"Author: {self.Author}")
        print(f"Number of Books: {BookStore.NoOfBooks}")

Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()


Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()
