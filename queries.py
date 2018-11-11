from data import data_manager
from psycopg2 import sql

def get_shows(page_num):
        return data_manager.execute_select('''
        SELECT shows.id, title, year, runtime, array_to_string((array_agg(name))[1:3], ', ') as genre, rating, trailer,homepage FROM shows
     left join  show_genres g on shows.id = g.show_id
     left Join genres g2 on g.genre_id = g2.id
    GROUP BY shows.id
    ORDER BY rating DESC LIMIT 15 OFFSET %(page_num)s''', {'page_num': page_num})


def order_list(page_num, order_by, order):
    if order == 'asc':
        return data_manager.execute_select(sql.SQL('''
        SELECT title, year, runtime, array_to_string((array_agg(name))[1:3], ', ') as genre, rating, trailer,homepage FROM shows
         left join  show_genres g on shows.id = g.show_id
         left Join genres g2 on g.genre_id = g2.id
        GROUP BY title, year, runtime, rating, trailer, homepage
        ORDER BY {order_by} ASC LIMIT 15 OFFSET %(page_num)s''', ).
                                         format(order_by=sql.Identifier(order_by)), {'page_num': page_num})
    else:
        return data_manager.execute_select(sql.SQL('''
                SELECT title, year, runtime, array_to_string((array_agg(name))[1:3], ', ') as genre, rating, trailer,homepage FROM shows
                 left join  show_genres g on shows.id = g.show_id
                 left Join genres g2 on g.genre_id = g2.id
                GROUP BY title, year, runtime, rating, trailer, homepage
                ORDER BY {order_by} DESC LIMIT 15 OFFSET %(page_num)s''', ).
                                           format(order_by=sql.Identifier(order_by)), {'page_num': page_num})


def detailed_series(id):
    return data_manager.execute_select_one('''
    SELECT title, year, runtime, string_agg(name, ', ') as genre, rating, trailer,homepage, overview FROM shows 
    left join show_genres g on shows.id = g.show_id 
    left Join genres g2 on g.genre_id = g2.id 
    WHERE shows.id = %(id)s
    GROUP BY title, year, runtime, rating, trailer, homepage, overview
    ''', {'id': id} )


#LINE 5:     WHERE title = "Planet Earth II"
