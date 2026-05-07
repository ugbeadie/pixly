from fastapi import Depends, FastAPI, HTTPException
from app.db import get_db,engine
from sqlalchemy.orm import Session
from app import schemas, models
from pydantic import BaseModel

app = FastAPI()

@app.post("/books", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    new_book = models.Book(title=book.title, author=book.author)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book    

@app.get("/books", response_model=list[schemas.Book])
def get_books(db: Session = Depends(get_db)):
    books = db.query(models.Book).all()
    return books    

@app.get("/books/{book_id}", response_model=schemas.Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, updated_data: schemas.BookCreate, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    book.title = updated_data.title
    book.author = updated_data.author
    db.commit()
    db.refresh(book)
    return book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}

# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi import HTTPException

# app = FastAPI()

# class Book(BaseModel):
#     id: int
#     title: str
#     author: str

# class BookUpdate(BaseModel):
#     title: str
#     author: str    

# books: list[Book] = [
#     Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald"),
#     Book(id=2, title="To Kill a Mockingbird", author="Harper Lee"),
#     Book(id=3, title="1984", author="George Orwell"),
#     Book(id=4, title="Pride and Prejudice", author="Jane Austen"),
# ]

# @app.get("/books", response_model=list[Book])
# def get_books():
#     return books

# @app.get("/books/{book_id}", response_model=Book)
# def get_book(book_id: int):
#     for book in books:
#         if book.id == book_id:
#             return book
#     raise HTTPException(status_code=404, detail="Book not found")
# @app.post("/books", response_model=Book)
# def create_book(book: Book):
#     books.append(book)
#     return book

# @app.put("/books/{book_id}", response_model=Book)
# def update_book(book_id: int, updated_data: BookUpdate):
#     for index, book in enumerate(books):
#         if book.id == book_id:
#             new_book = Book(
#                 id=book_id, 
#                 title=updated_data.title, 
#                 author=updated_data.author
#             )
            
#             books[index] = new_book
#             return new_book
            
#     raise HTTPException(status_code=404, detail="Book not found")

# @app.delete("/books/{book_id}")
# def delete_book(book_id: int):
#     for index, book in enumerate(books):
#         if book.id == book_id:
#             del books[index]
#             return {"message": "Book deleted successfully"}
#     raise HTTPException(status_code=404, detail="Book not found")    
