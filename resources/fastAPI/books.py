'''
Fast API example
'''

from tokenize import Number
from typing import Optional
from unicodedata import numeric
from fastapi import FastAPI
from enum import Enum

app = FastAPI()


# @app.get("/")
# async def first_api():
#     """
#     Get Books
#     """
#     return {"message": "Shreyas"}


books = {
    'book_1' : {'title': 'Title One', 'author': 'Author One'},
    'book_2' : {'title': 'Title Two', 'author': 'Author Two'},
    'book_3' : {'title': 'Title Three', 'author': 'Author Three'},
    'book_4' : {'title': 'Title Four', 'author': 'Author Four'},
    'book_5' : {'title': 'Title Five', 'author': 'Author Five'}
}


class DirectionName(str, Enum):
    '''
    Dirction Name
    '''
    north = "North"
    south = "South"
    east = "East"
    west = "West"

#  = 'book_3'
@app.get("/")
async def read_all_books(skip_book: Optional[str] = None):
    """
    Read all books
    """
    if skip_book:
        new_books = books.copy()
        del new_books[skip_book]
        return new_books
    return books

@app.get("/{book_name}")
async def read_book(book_name: str):
    '''
    read book 
    '''
    return books[book_name]


@app.get("/books/mybook")
async def read_favourite_book():
    """
    My Favourite
    """
    return {"book_title" : "My favourite"}


# @app.get("/books/{books_id}")
# async def read_book(book_id: int):
#     """
#     Read book
#     """
#     return {'book_title': book_id}

@app.get("/directions/{direction_name}")
async def read_direction(directon_name: DirectionName):
    '''
    Get directions --
    '''
    if directon_name == DirectionName.north:
        return {"Direction": directon_name, "sub": "up"}
    if directon_name == DirectionName.south:
        return {"Direction": directon_name, "sub": "down"}
    if directon_name == DirectionName.east:
        return {"Direction": directon_name, "sub": "right"}
    if directon_name == DirectionName.west:
        return {"Direction": directon_name, "sub": "left"}


    
@app.get('/api/v1/bluetooth/settings')
async def bluetooth_settings():
    """
    Get bluetooth status
    """

    val = {
            "enabled": True,
            "displayName": "Test"
        }

    return val

class GpioMode(str, Enum):
    '''
    GPIO Modes
    '''
    IPU = "INPUT_PULL_UP"
    IPD = "INPUT_PULL_DOWN"
    OPP = "OUTPUT_PUSH_PULL"
    
    

@app.post("/set_gpio_mode/{gpio_mode}")
async def set_gpio_mode(gpio_mode : GpioMode):
    '''
    Sets gpio mode
    '''
    return gpio_mode.IPU


@app.post("/")
async def create_book(book_title, book_author):
    '''
    create a book
    '''
    id = len(books)
    books[f'book_{id+1}'] = {'title': book_title, 'author': book_author}
    
 
@app.put('/{book_name}')   
async def update_book(book_name : str, book_title : str, book_author : str):
    '''
    update book
    '''
    information = {'title': book_title, 'author': book_author}
    books[book_name] = information
    return information

