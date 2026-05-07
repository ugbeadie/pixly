from app.db import engine, Base
from app import schemas  # IMPORTANT: registers tables

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully")

if __name__ == "__main__":
    create_tables()