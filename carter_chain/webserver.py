from carter_chain.crypto import hash_this

from flask import Flask, request
app = Flask (__name__)



@app.route("/") 
def home():
    return "blockchain"

@app.route("/hash")
def hash():
    contents = request.args.get('contents')
    hash_result = hash_this(contents)
    return hash_result

