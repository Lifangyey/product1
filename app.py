from flask import Flask, render_template
import urllib.parse

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
def search(query):
    encode_word = urllib.parse.quote(query, encoding="utf-8")
    url = "https://rtrp.jp/locations/38/?q=" + encode_word
    return url

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == "__main__": #最後に記述する
    app.run(debug=True)