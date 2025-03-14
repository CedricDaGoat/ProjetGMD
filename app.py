from flask import Flask, render_template, request
from data import Seeker  # Importer la fonction depuis data.py

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    user_query = request.form.get('query')  # Récupérer la recherche utilisateur
    if user_query:
        query_list = list(user_query)  # Transformer la chaîne en liste de caractères
        resultats = Seeker(query_list)  # Appeler la fonction pour obtenir les résultats
        return render_template('results.html', resultats=resultats)  # Envoyer les résultats au HTML
    return "Veuillez entrer une recherche valide."


if __name__ == '__main__':
    app.run(debug=True)
