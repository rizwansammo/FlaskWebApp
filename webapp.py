from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def homePage():
    return render_template('home.html')

@app.route("/about")
def aboutPage():
    return render_template('about.html')
