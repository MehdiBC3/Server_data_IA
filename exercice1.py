from flask import Flask, request, render_template

app = Flask(__name__)

books = [
    {"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "year": 1997},
    {"id": 2, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}, 
    {"id": 3, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 4, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 5, "title": "A Promised Land", "author": "Barack Obama", "year": 2020}
]

@app.route('/', methods=("GET", "POST"))
def index():
    return render_template("index.html")

@app.route('/search', methods=["GET"])
def search():
    query = request.args.get('query')
    return f'Recherche : {query}'

@app.route('/books', methods=["GET"])
def books_route():

    authorFromSearch = request.args.get("author")
    exist = False

    for livre in books:
        if livre['author'] == authorFromSearch : 
            exist = False
            return f"Livre : {livre['title']} ({livre['year']})"

    if exist == False: 
        return "Aucun livre trouvé!"
    
@app.route('/login', methods=["POST"])
def login():
    nom = request.form.get('username')
    motdepasse = request.form.get('motdepasse')

    return f'Nom : {nom} / Mot de passe : {motdepasse}'


# solution alternative

# @app.route('/books', methods=["GET"])
# def books_route():
#     query = request.args.get('query', '').lower()  # Récupérer la recherche en minuscule
#     # Rechercher les livres où l'auteur correspond à la requête
#     matching_books = [book for book in books if query in book['author'].lower()]
    
#     # Retourner un message ou les livres trouvés
#     if matching_books:
#         result = '<br>'.join([f"{book['title']} - {book['author']} ({book['year']})" for book in matching_books])
#     else:
#         result = f"Aucun livre trouvé pour l'auteur : {query}"
    
#     return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
