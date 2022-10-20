from flask import Blueprint

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