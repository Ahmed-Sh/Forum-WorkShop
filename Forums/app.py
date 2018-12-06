from flask import Flask, render_template
from dummy_data import post_store

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def home():
    posts = post_store.get_all()
    return render_template("index.html", posts=posts)


app.run()
