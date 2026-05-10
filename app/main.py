from fastapi import FastAPI

from app.routers import auth, books

app = FastAPI(title="Pixly")

app.include_router(books.router)
app.include_router(auth.router)


@app.get("/")
def read_root():
    return {"message": "Pixly API"}
