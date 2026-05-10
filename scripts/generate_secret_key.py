import secrets

if __name__ == "__main__":
    SECRET_KEY = secrets.token_urlsafe(32)
    print(f"Generated SECRET_KEY: {SECRET_KEY}")
