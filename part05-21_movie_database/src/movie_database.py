# Write your solution here


def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    new = {}
    new['name'] = name
    new['director'] = director
    new['year'] = year
    new['runtime'] = runtime
    database.append(new)

