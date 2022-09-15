from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_actors():
    return data_manager.execute_select('''
    SELECT actors.id,
       actors.name,
       EXTRACT (YEAR FROM actors.death)::int AS death,
       COUNT(show_characters.show_id) AS roles,
        CASE
            WHEN (actors.death IS NOT NULL) THEN CAST(EXTRACT(year FROM actors.death) - EXTRACT(year FROM actors.birthday) AS INTEGER )
            WHEN (actors.death IS NULL) THEN CAST(EXTRACT(year FROM CURRENT_DATE) - EXTRACT(year FROM actors.birthday) AS INTEGER)
            ELSE NULL
        END AS age
    FROM actors
    INNER JOIN show_characters on actors.id = show_characters.actor_id
    GROUP BY actors.id
    ORDER BY roles DESC''')
