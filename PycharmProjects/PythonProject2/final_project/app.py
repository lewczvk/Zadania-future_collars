from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from film_database import get_data_from_movie_api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///filmoteka.db'
db = SQLAlchemy(app)

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    actors = db.Column(db.String(100), nullable=False)
    writer = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    runtime = db.Column(db.String(100), nullable=False)
    plot = db.Column(db.String(100), nullable=False)
    awards = db.Column(db.String(100), nullable=False)
    # imdbRating = db.Column(db.Float(100), nullable=False)

@app.route('/', methods=['GET'])
def home():
    films = Film.query.all()
    return render_template('filmbase.html', films=films)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        query = request.args.get('query')
        return render_template('search.html', query=query)
    else:
        name = request.form['name']
        year = request.form['year']
        movie_info = get_data_from_movie_api(name, year)
        print(movie_info)
        film=Film(title=movie_info['Title'], year=movie_info['Year'], genre=movie_info['Genre'],
                  actors=movie_info['Actors'], writer=movie_info['Writer'], director=movie_info['Director'],
                  runtime=movie_info['Runtime'], plot=movie_info['Plot'],
                  awards=movie_info['Awards'])
        db.session.add(film)
        db.session.commit()
        return render_template('search2.html', movie_info=movie_info)

with app.app_context():
    db.create_all()

# @app.route('/ratings', methods=['GET', 'POST'])
# def ratings():
#     the_best = Film.query.filter(Film.imdbRating >= 7.0).all()
#
#     average = Film.query.filter(Film.imdbRating >= 5.0, Film.imdbRating < 7.0).all()
#
#     the_worst = Film.query.filter(Film.imdbRating < 5.0).all()
#
#     return render_template('ratings.html', the_best=the_best, average=average, the_worst=the_worst)

if __name__ == '__main__':
    app.run(debug=True)
