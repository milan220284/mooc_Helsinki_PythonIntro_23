# Write your solution here:
class Series:

    def __init__(self, title: str, number_seasons: int, genre: list):
        self.title = title
        self.number_seasons = number_seasons
        self.genre = genre
        self.number_of_rates = 0
        self.ratings_sum = 0
        self.avg_rating = 0
    
    def rate(self, mark):
        self.number_of_rates += 1
        self.ratings_sum += mark
        self.avg_rating = self.ratings_sum/self.number_of_rates

    def __str__(self):
        result = self.title + f" ({self.number_seasons} seasons)\n"
        genre_string = ", ".join(self.genre)
        result += "genres: " + genre_string + "\n"
        average = 0
        if self.number_of_rates > 0:
            average = self.ratings_sum/self.number_of_rates
            result += f"{self.number_of_rates} ratings, average {average:.1f} points"
        else:
            result +="no ratings"
        return result


def minimum_grade(rating: float, series_list: list):
    result = []
    for series in series_list:
        if not (series.avg_rating < rating):
            result.append(series)
    return result

def includes_genre(genre: str, series_list: list):
    result = []
    for series in series_list:
        if genre in series.genre:
            result.append(series)
    return result

