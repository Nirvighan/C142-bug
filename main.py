from flask import Flask,jsonify,request
import csv

allmovies = []

with open(r'D:\PythonProjects\C141\venv\movies.csv',encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    allmovies = data[1:]

liked_movies = []
not_liked_movies = []
not_watched_movies = []

app = Flask(__name__)
@app.route('/get-movie')

def get_movies():
    movie = allmovies[0]
    return jsonify({
        "data":movie,
        "status":"success"
    }),200

@app.route("/liked-movie",methods = ["POST"])

def liked_movie():
    global allmovies
    movie = allmovies[0]
    allmovies = allmovies[1:]
    liked_movies.append(movie)
    return jsonify({
        
        "status":"success"
    }),201

@app.route("/unliked-movie",methods = ["POST"])

def unliked_movie():
    global allmovies
    movie = allmovies[0]
    allmovies = allmovies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        
        "status":"success"
    }),201

@app.route("/did-not-watched-movie",methods = ["POST"])

def did_not_watched_movie():
    global allmovies
    movie = allmovies[0]
    allmovies = allmovies[1:]
    not_watched_movies.append(movie)
    return jsonify({
        
        "status":"success"
    }),201


if __name__ == "__main__":
    app.run(debug = True)
     
    