# Write your solution here


def find_movies(database: list, search_term: str):
    output = []
    for item in database:
        if search_term.lower() in item['name'].lower():
            output.append(item)

    return output



