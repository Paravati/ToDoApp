from flask import Flask, g
from flask import render_template
import os
import sqlite3

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY = 'bardzosekretnawartosc',   # wartość wykorzystywana do obsługi sesji
    DATABASE = os.path.join(app.root_path, 'db.sqlite'),  # scieżka do pliku bazy
    SITE_NAME = 'Moje zadania'  # nazwa aplikacji
))

def get_db():
    '''Tworzenie połączenia z bazą danych'''
    if not g.get('db'):  # jezeli brak połączenia to je tworzymy
        conn = sqlite3.connect(app.config['DATABASE'])
        conn.row_factory = sqlite3.Row
        g.db = conn  # zapisujemy połączenie w kontekście aplikacji
    return g.db  # zwracamy połączenie z bazą


@app.teardown_appcontext
def close_db(error):
    '''Zamykanie połączenia z bazą'''
    if g.get('db'):
        g.db.close()

@app.route('/zadania')
def zadania():
    db = get_db()  # utworzenie obiektu bazy danych
    kursor = db.execute('SELECT * FROM zadania ORDER BY data_dodania DESC;')
    zadania = kursor.fetchall()  #fetchall zwraca dane w formie listy
    return render_template('zadania.html', zadania=zadania)

@app.route('/')
def index():
    # return 'Cześć, tu Python!'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)