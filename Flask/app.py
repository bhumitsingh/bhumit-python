from flask import Flask
'''
It creates an instance of a Flask class,
which will be your WSGI(Web Server Gateway Interface) application.
'''

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my Flask app"

@app.route("/index")
def index():
    return "This is the index page"

if __name__ =="__main__":
    app.run(debug=True)

