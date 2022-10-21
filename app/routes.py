

from flask import Blueprint, jsonify


class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Fellowship of the poop", "book 1: A fantasy novel set in an imaginary world."),
    Book(2, "The two scoops", "book 2: A fantasy novel set in an imaginary world."),
    Book(3, "return of the big poop", "book 3: A fantasy novel set in an imaginary world.")
] 

books_bp = Blueprint("books", __name__, url_prefix= "/books")

@books_bp.route("", methods = ["GET"])
def get_all_books():
    book_response = []
    for book in books:
        book_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(book_response)

#the following is how to make it with a specific link (try this for the pokemon program)
@books_bp.route("/<book_id>", methods = ["GET"])
def get_one_book(book_id):
    try:
        book_id = int(book_id)
    except:
        return {"message": f"book {book_id} invalid"}, 400
    book_id = int(book_id)
    for book in books:
        if book.id == book_id:
            return {
                "id" : book.id, 
                "title" : book.title,
                "description" : book.description
            }
        else:
            return {"message":f"book {book_id} not found"}, 404



##------------------Test blueprints--------------#

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route("/hello-world", methods = ["GET"])
def say_hello_world():
    my_response_body = "Hello World!"
    return my_response_body

hello_json = Blueprint("hello/JSON", __name__)

@hello_json.route("/hello/JSON", methods = ["GET"])
def say_hello_json():
    return {
        "name" : "Ada Lovelace",
        "message" : "Hello!",
        "hobbies" : ["Fishing", "Swimming", "Watching reality TV"]
    }

@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body
