from flask import Flask
from .user import User
from .category import Category

from pprint import pp

app = Flask(__name__)


@app.route("/")
def main():
    response = {
        'message': 'Welcome to the BEON Python/Django Challenge'
    }
    return response, 200


@app.route("/users")
def users():
    users_ = User.get_all()
    response = {
        'data': users_
    }
    return response, 200


@app.route("/categories")
def categories():
    categories_ = Category.get_all()
    response = {
        'data': categories_
    }
    return response, 200


if __name__ == "main":
    app.run(host="0.0.0.0", port=5000)
