from app import models  # noqa: F401  -- ensure models register on Base.metadata
from app.db import Base, engine


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully")


if __name__ == "__main__":
    create_tables()
