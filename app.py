import os
import signal
from flask import Flask
from generator import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    page = '<html><body><h1>Рецепт дня</h1><h4>'
    its, acts = generator.get_random_items_and_actions(5)
    page += generator.get_recepie(its, acts)
    page += '</h4></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))