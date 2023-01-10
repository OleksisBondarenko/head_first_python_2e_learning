from flask import Flask, render_template, request
from vsearch import search_for_letters

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("search.html")

@app.route('/result',  methods=["post"])
def result():
  phrase = request.form["phrase"]
  letters = request.form["letters"]

  found_letters = search_for_letters(phrase, letters)
  return render_template("result.html", phrase = phrase, letters = letters, found_letters = found_letters)

app.run(debug=True)