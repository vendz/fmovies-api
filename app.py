from search import getMovies
from details import getDetails
from suggestions import getSuggestions
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "BE61D9E9B64AC871D85FD7C285F7D"
CORS(app)


@app.route('/')
def index():
    return "API is UP and running"

@app.route('/search')
def search():
    if request.method == 'GET':
        keyword = request.args.get('keyword')
        page = request.args.get('page')
        return jsonify(getMovies(keyword, page))


@app.route('/home')
def suggestions():
    if request.method == 'GET':
        suggest = request.args.get('suggest')
        return jsonify(getSuggestions(suggest))


@app.route('/details')
def details():
    if request.method =='GET':
        link = request.args.get('link')
        return jsonify(getDetails(link))

if __name__ == '__main__':
    app.run(debug=True)
