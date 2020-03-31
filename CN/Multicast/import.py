import os
from flask import Flask, request, render_template
from models import *
from datetime import datetime
from models import User
from logging.config import fileConfig
import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)

# Configuring the file for logging.
fileConfig('logging.cfg')

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    books = []
    for isbn, title, author, year in reader:
        books.append(Book(isbn=isbn, title=title, author=author,year=year))
        app.logger.info("Adding: ", )
        if len(books) == 100:
            db.session.add(book)
            db.session.commit()
            books = []    

if __name__ == "__main__":
    with app.app_context():
        main()