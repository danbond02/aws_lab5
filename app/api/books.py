from fastapi import APIRouter, HTTPException
from typing import List
from api.models import BookPut, BookPost
from api.db import db

books = APIRouter()


@books.get("/")
async def hello():
    return "Hello. This is Book-Service."


@books.get("/books", response_model=List[BookPost])
async def list_all():
    return db


@books.post('/books', status_code=201)
async def add_book(payload: BookPost):

    new_id = max((item["id"] for item in db), default=0) + 1
    new_book = {"id": new_id, **payload.dict()}
    db.append(new_book)
    return new_book


@books.put('/books/{id}')
async def update_book(id: int, payload: BookPut):

    for book in db:
        if book["id"] == id:

            update_data = payload.dict(exclude_unset=True)
            book.update(update_data)
            return book


    raise HTTPException(status_code=404, detail="Book not found")


@books.delete('/books/{id}')
async def delete_book(id: int):

    for index, book in enumerate(db):
        if book["id"] == id:
            deleted_book = db.pop(index)
            return {"message": f"Book with ID {id} deleted successfully", "book": deleted_book}


    raise HTTPException(status_code=404, detail="Book not found")
