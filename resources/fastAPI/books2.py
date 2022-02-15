from email import header
from fastapi import FastAPI, HTTPException, Request, status, Form, Header
from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional
from starlette.responses import JSONResponse

app = FastAPI()


class NegativeNumberException(Exception):
    def __init__(self, books_to_return):
        self.books_to_return = books_to_return
        
        
@app.exception_handler(NegativeNumberException)
async def negative_number_exception_handler(request: Request, 
                                            exception: NegativeNumberException):
    return JSONResponse( status_code= 418, 
                        content={"message": "Invalid value"})
    
    


class Book(BaseModel):
    """
    Book with BaseModel
    """
    id: UUID
    title: str  = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Description of the book", 
                             max_length=100,
                             min_lenght=1)
    rating: int = Field(gt=-1, lt=101)
    
    class Config:
        schema_extra = {
            "example": {
                "id": "110d791f-407a-420d-8ffc-b4bc1564c02b",
                "title": "SJ book",
                "author": "Shreyas",
                "description": "A very nice description",
                "rating": 100
            }
        }
    


class BooksNoRating(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str
    description: Optional[str] = Field(None, title="description of the book", max_lenght=100, min_length=1)
    
    
books = []

@app.post("/books/login")
async def book_login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password}


@app.get("/header")
async def read_header(random_header: Optional[str] = Header(None)):
    return {"Random-Header": random_header}
    

@app.get("/")
async def read_all_books(books_to_return: Optional[int] = None):
    if books_to_return and books_to_return < 0:
        raise NegativeNumberException(books_to_return)
    
    if len(books) < 1:
        create_books_no_api()
    return books

@app.get("/book/{book_id}")
async def read_book(book_id: UUID):
    for x in books:
        if x.id == book_id:
            return x 

@app.get("/book/rating/{book_id}", response_model=BooksNoRating)
async def read_book_no_rating(book_id: UUID):
    for x in books:
        if x.id == book_id:
            return x 
    raise HTTPException(status_code=402, detail="Not found")


@app.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    books.append(book)
    return books


@app.put("/{book_id}")
async def update_book(book_id: UUID, book: Book):
    for idx, x in enumerate(books):
        if x.id == book_id:
            books[idx] = book
            return books[idx]
        
        
@app.delete("/{book_id}")
async def delete_book(book_id: UUID):
    for idx, x in enumerate(books):
        if x.id == book_id:
            del books[idx]
            return f'ID:{book_id} deleted'
    raise HTTPException(status_code=404, detail="Book ID not found",
                        headers={"X-Header-Error": "Nothing to be seen at UUID"})


def create_books_no_api():
    book_1 = Book(id="370d791f-407a-420d-8ffc-b4bc1564c02b",
                  title="title_1",
                  author="Author_1",
                  description="book 1",
                  rating=60)
    book_2 = Book(id="470d791f-407a-420d-8ffc-b4bc1564c02b",
                  title="title_2",
                  author="Author_2",
                  description="book 2",
                  rating=10)
    book_3 = Book(id="590d791f-407a-420d-8ffc-b4bc1564c02b",
                  title="title_3",
                  author="Author_3",
                   description="book 3",
                  rating=80)
    book_4 = Book(id="890d791f-407a-420d-8ffc-b4bc1564c02b",
                  title="title_4",
                  author="Author_4",
                  description="book 4",
                  rating=40)
    
    books.append(book_1)
    books.append(book_2)
    books.append(book_3)
    books.append(book_4)
    