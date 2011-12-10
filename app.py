import urllib
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<path:in_url>")
def index_with_url(in_url):
    url = urllib.unquote(in_url)
    if not url.startswith("https://") or not url.startswith("http://"):
        url = "http://" + url
    return render_template("index.html", source=url, text=in_url)

@app.route("/")
def index():
    return render_template("index.html", source=None, text=None)


if __name__ == "__main__":
    app.run(debug=True)

