from fastapi import FastAPI
import uvicorn
from api.books import books

app = FastAPI(openapi_url="/api/books/openapi.json", docs_url="/api/books/docs")

app.include_router(books)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
