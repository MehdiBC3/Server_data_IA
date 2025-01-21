from flask import Flask, request, render_template

app = Flask(__name__)

books = [

    {"id": 1, "title": "Harry Plotter1", "author": "JK", "year" : 1997 },
    
    {"id": 2, "title": "Harry Plotter2", "author": "JK", "year" : 2001 },

    {"id": 3, "title": "Harry Plotter3", "author": "JK", "year" : 2006 },

    {"id": 4, "title": "Harry Plotter4", "author": "JK", "year" : 2010 },

    {"id": 5, "title": "Harry Plotter5", "author": "JK", "year" : 2019 }

]

@app.route('/', methods=("GET","POST"))
def index():
    return render_template("index.html")

@app.route('/search', methods=["GET"])
def search():
    query = request.args.get('query')
    date = request.args.get('date')
    return f'Recherche : {query}'


@app.route('/books', methods=["GET"])
def book():

    author = request.args.get('author')
    exist = False

    for livre in books:
        if livre['author'] == author:
            exist = True
            return f"livre {livre['title']} ( {livre['year']})"

    if exist == False:
        return "cherche mieux"


@app.route('/login', methods=["POST"])
def login():
    nom = request.form.get('username')
    motdepasse = request.form.get('motdepasse')
    return f'Nom : {nom} / Mot de passe = {motdepasse}'


@app.route('/add_book', methods=["POST"])
def addBook():
    titre = request.form.get('title')
    auteur = request.form.get('author')
    annee = request.form.get('year')

    books.append(
        {"id" : len(books) + 1, "title" : titre , "author" : auteur , "year" : annee}
    )

    return f"auteur: {titre} | auteur : {auteur} | annee : {annee}"



            
if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=80)