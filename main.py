from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("Home.HTML")

@app.route("/about")
def about():
    return render_template("About.HTML")

@app.route("/csignup")
def signup():
    return render_template("signup.HTML")

@app.route("/login")
def login():
    return render_template("LOGIN.HTML")

if _name_ == "_main_":
    app.run(debug=True,host="0.0.0.0",port=5000)

