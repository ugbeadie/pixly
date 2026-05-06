from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str

class BookUpdate(BaseModel):
    title: str
    author: str    

books: list[Book] = [
    Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald"),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee"),
    Book(id=3, title="1984", author="George Orwell"),
    Book(id=4, title="Pride and Prejudice", author="Jane Austen"),
]

@app.get("/books", response_model=list[Book])
def get_books():
    return books

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
@app.post("/books", response_model=Book)
def create_book(book: Book):
    books.append(book)
    return book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_data: BookUpdate):
    for index, book in enumerate(books):
        if book.id == book_id:
            # We construct a full 'Book' using the URL's book_id and the incoming JSON data
            new_book = Book(
                id=book_id, 
                title=updated_data.title, 
                author=updated_data.author
            )
            
            books[index] = new_book
            return new_book
            
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            del books[index]
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")    