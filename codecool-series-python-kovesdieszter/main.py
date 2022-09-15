from flask import Flask, render_template, url_for, jsonify
from data import queries
import math
from dotenv import load_dotenv

load_dotenv()
app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/actors')
def show_actors():
    return render_template('actors.html')


@app.route('/api/actors')
def get_actors_data():
    actors_data = queries.get_actors()
    for item in actors_data:
        if item['death']:
            item['alive'] = False
        else:
            item['alive'] = True
    return jsonify(actors_data)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
