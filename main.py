from flask import Flask, render_template, url_for
from data import queries

app = Flask('codecool_series')
table_header = ('Title', 'Release Year', 'Runtime Length', 'Rating', 'Genre', 'Trailer', 'Homepage')


@app.route('/')
def index():
    shows = queries.get_shows()

    return render_template('index.html', shows=shows, header=table_header)


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()