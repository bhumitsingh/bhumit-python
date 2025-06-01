### Building a Jinja Template
# Jinja is a templating engine which allows us to write Python code inside of HTML files.
# This is useful when we want to dynamically generate HTML content.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to my Flask app</h1></html>"

@app.route("/index", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return f'Hello {name}'
    return render_template("form.html")

@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method == "Post":
        name = request.form["name"]
        return f'Hello {name}'
    return render_template("form.html")

# Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "Pass"
    else:
        res = "Fail"
    return render_template('result.html', result=res)

@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score >= 50:
        res = "Pass"
    else:
        res = "Fail"

    exp = {'score': score, 'res': res}
    return render_template('result1.html', result=exp)

if __name__ == "__main__":
    app.run(debug=True)