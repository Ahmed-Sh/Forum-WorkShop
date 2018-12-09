from flask import Flask, render_template, request, redirect, url_for
from dummy_data import *


app = Flask(__name__)


@app.route("/")
@app.route("/index")
def home():
    topics = post_store.get_all()
    return render_template("index.html", posts=topics)
#    red posts is the one we handle in html


@app.route("/topic/add", methods=["GET", "POST"])
def topic_add():
    if request.method == "POST":
        # Note "title and "content" should be same "name" as in  html form
        new_post = models.Post(request.form["title"], request.form["content"])
        post_store.add(new_post)
        return redirect(url_for("home"))
    else:
        return render_template("topic_add.html")


app.run(debug=True)
