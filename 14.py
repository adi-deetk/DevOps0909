from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/whatismyname', methods=['GET', 'POST', 'DELETE'])
def hello():
    my_score = 1
    return "<h1>" + str(my_score) + "</h1>"

@app.route('/')
def my_func():
    return "hello and welcome to the world of games"


app.run(host="0.0.0.0", port=5001, debug=True)
