from flask import Flask, render_template, url_for, request, redirect
from data import queries

app = Flask('codecool_series')
table_header = ('Title', 'Release Year', 'Runtime Length', 'Rating', 'Genre', 'Trailer', 'Homepage')


@app.route('/')
def index():
    page_num = 0
    order = 'desc'
    shows = queries.get_shows(page_num)
    return render_template('index.html', shows=shows, header=table_header, page_num=page_num, order=order)


@app.route('/next-page/<this_page>/<order>', methods=['GET', 'POST'])
def next_page(this_page, order):
    page_num = int(this_page) + 15
    shows = queries.get_shows(page_num)
    return render_template('index.html', shows=shows, header=table_header, page_num=page_num, order=order)


def change_order(order_by, order):
    if order_by == 'Title':
        order_by = 'title'
    elif order_by == 'Release Year':
        order_by = 'year'
    elif order_by == 'Runtime Length':
        order_by = 'runtime'
    elif order_by == 'Rating':
        order_by = 'rating'
    elif order_by == 'Genre':
        order_by = 'genre'
    elif order_by == 'Trailer':
        order_by = 'trailer'
    elif order_by == 'Homepage':
        order_by = 'homepage'
    if order == 'desc':
        order = 'asc'
    elif order == 'asc':
        order = 'desc'
    return order, order_by


@app.route('/order-list')
def order_list():
    order = request.args['order']
    order_by = request.args['order_by']
    page_num = int(request.args['page_num'])
    order, order_by = change_order(order_by, order)
    shows = queries.order_list(page_num, order_by, order)
    return render_template('index.html', shows=shows, header=table_header, page_num=page_num, order=order)


@app.route('/detailed/<int:id>', methods=['GET', 'POST'])
def detailed(id):
    show = queries.detailed_series(id)
    return render_template('details.html', show=show)


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
