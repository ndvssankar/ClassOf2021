import os
from flask import Flask, request, render_template
from models import *
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://tgsemzadyezlgh:858baa7b0d8b5ce3cb37d6481e187d508a119f33d2f26a2addac896f186eb633@ec2-18-233-137-77.compute-1.amazonaws.com:5432/d389gkjdhv6oa2"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

class User():
    def __init__(self, username, password, user_created_on=None):
        __tablename__ = "users"
        self.username = username
        self.password = password
        self.user_created_on = datetime.now()
        
    # def add_user(self):
    #     if len(self.get_user(self.username)) == 1:
    #         return False
    #     else:
    #         user = User(username=self.username, password=self.password, user_created_on=datetime.now())
    #         db.session.add(user)
    #         db.session.commit()
    #         return True

    # def get_user(self, username):
    #     return User.query.filter(username = self.username)

    def print_info(self):
        print(f"User name: {self.username}")
        print(f"User pwd : {self.password}")
        print(f"User c on: {self.user_created_on}")

def main():
    user = User("one", "two")
    user.print_info()

if __name__ == "__main__":
    main()