from flask import Flask, render_template, request, jsonify, redirect, url_for
from searchMovie import searchByCategory, searchByYear, searchByWinner, searchByName, data
from imdbURL import giveURL
import json

app = Flask(__name__)


@app.route('/apiHelp', methods=['GET', 'POST'])
def apiHelp():
    return render_template('api.html')

@app.route('/about', methods=['GET', 'POST'])
def aboutPage():
    return render_template('about.html')
    
@app.route('/imbdbURL', methods=['GET', 'POST'])
def imdb():
    print("getting url")
    if request.method == "GET":
        mname=request.args['mname']
        year=request.args['year']
        print(mname, year)
        return giveURL(mname, str(year))
        
@app.route('/', methods=['GET', 'POST'])
def home():
        print("asdsasda")
        redirect(url_for('home'))
        return render_template('home.html')
        
@app.route('/display', methods=['GET', 'POST'])
def display():
    arr=False
    if request.method == "POST":
        return render_template('home.html')
    elif request.method =="GET":
        
        category=False
        year=False
        winner=False
        name=False
        
        if not request.args['mname'] == "":
            name=str(request.args['mname'])
        if not request.args['category'] == "":
            category=str(request.args['category'])
        if not request.args['year'] == "":
            year=int(request.args['year'])
        if not request.args['winner'] == "":
            winner=True
        
        if name and category and year and winner:
            arr=searchByWinner( winner, searchByYear(year, searchByCategory(category, searchByName(name, data))) )
        elif name and category and year:
            arr=searchByYear(year, searchByCategory(category, searchByName(name, data)))
        elif name and category and winner:
            arr=searchByWinner(winner, searchByCategory(category, searchByName(name, data)))
        elif name and year and winner:
            arr=searchByWinner(winner, searchByYear(year, searchByName(name, data)))
        elif name and category:
            arr=searchByCategory(category, searchByName(name, data))
        elif name and year:
            arr=searchByYear(year, searchByName(name, data))
        elif name and winner:
            arr=searchByWinner(winner, searchByName(name, data))
        elif name:
            arr=searchByName(name, data)
        elif category and year and winner:
            arr=searchByWinner(winner, searchByYear(year, searchByCategory(category, data)))
        elif category and winner:
            arr=searchByWinner(winner, searchByCategory(category, data))
        elif category and year:
            arr=searchByYear(year, searchByCategory(category, data)) 
        elif year and winner:
            arr=searchByWinner(winner, searchByYear(year, data)) 
        elif category:
            arr=searchByCategory(category, data)
        elif year:
            arr=searchByYear(year, data)
        else:
            return redirect(url_for('home'))
            
        return render_template('display.html', movies=arr)
        
@app.route('/search', methods=['GET'])
# how to test: type 'http://127.0.0.1:5000/search?category=direction&winner=True&year=1987' into url
def search():
    arr=False
    category=False
    year=False
    winner=False
    name=False
    
    def noMovies(a):
        if len(a) == 0:
            print(len(a))
            b={"error":"no movies found"}
            return jsonify(b)
    
    if 'category' in request.args:
        category = str(request.args["category"])
    if 'year' in request.args:
        year = int(request.args["year"])
    if 'winner' in request.args:
        winner = bool(request.args["winner"])
    if 'name' in request.args:
        name = str(request.args["name"])
    
    if name and category and year:
        arr=searchByYear(year, searchByCategory(category, searchByName(name, data)))
        noMovies(arr)
        return jsonify(arr)
    if name and category:
        arr=searchByCategory(category, searchByName(name, data))
        return noMovies(arr)
        return jsonify(arr)
    elif name and year:
        arr=searchByYear(year, searchByName(name, data))
        noMovies(arr)
        return jsonify(arr)
    elif name and winner:
        arr=searchByYear(winner, searchByName(name, data))
        noMovies(arr)
        return jsonify(arr)
    elif name:
        arr=searchByName(name, data)
        noMovies(arr)
        return jsonify(arr)
    elif category and year and winner:
        arr=searchByWinner(winner, searchByYear(year, searchByCategory(category, data)))
        noMovies(arr)
        return jsonify(arr)
    elif category and winner:
        arr=searchByWinner(winner, searchByCategory(category, data))
        noMovies(arr)
        return jsonify(arr)
    elif category and year:
        arr=searchByYear(year, searchByCategory(category, data))
        noMovies(arr)
        return jsonify(arr)
    elif year and winner:
        arr=searchByWinner(winner, searchByYear(year, data))
        noMovies(arr)
        return jsonify(arr)
    elif category:
        arr=searchByCategory(category, data)
        noMovies(arr)
        return jsonify(arr)
    elif year:
        arr=searchByYear(year, data)
        noMovies(arr)
        return jsonify(arr)
    else:
        return jsonify({"error":"cannot search, end of filter statements"})
    
        
# 1st endpoint for returning collection reasource
@app.route('/movies/categories/bestpicture/1997', methods=['GET'])
def getColletion1():
    year = 1997
    category = "BEST PICTURE"
    # search function goes here
    return jsonify( searchByCategory(category, searchByYear(year, data)) )

# 2nd endpoint for returning collection reasource
@app.route('/movies/categories/actor/1997', methods=['GET'])
def getColletion2():
    year = 1997
    category = "ACTOR"
    # search function goes here
    return jsonify( searchByCategory(category, searchByYear(year, data)) )

# 1st endpoint for returning singleton reasource
@app.route('/movies/categories/bestpicture/1997/winner', methods=['GET'])
def getSingleton1():
    category="BEST PICTURE"
    year = 1997
    winner = True
    # search function goes here
    return jsonify( searchByWinner(True, searchByYear(year, searchByCategory(category, data))) )

# 2nd endpoint for returning singleton reasource
@app.route('/movies/categories/actor/1970/winner', methods=['GET'])
def getSingleton2():
    category="ACTOR"
    year = 1970
    winner = True
    # search function goes here
    return jsonify( searchByWinner(True, searchByYear(year, searchByCategory(category, data))) )

if __name__ == '__main__':
    app.run(debug=True)