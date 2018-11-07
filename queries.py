from data import data_manager


def get_shows():
    return data_manager.execute_select('''
    SELECT title, year, runtime, string_agg(name, ',') as genre, rating, trailer,homepage FROM 
    (SELECT g2.name FROM shows LIMIT 3)
    shows
 left join  show_genres g on shows.id = g.show_id
 left Join genres g2 on g.genre_id = g2.id
GROUP BY title, year, runtime, rating, trailer, homepage
ORDER BY rating DESC LIMIT 15''')

