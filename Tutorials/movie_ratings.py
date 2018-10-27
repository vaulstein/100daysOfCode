import numpy as np

movie_ratings = np.array([[63.0, 54.0, 70.0, 50.0],
                          [94.0, 85.0, 89.0, 95.0],
                          [64.0, 90.0, 73.0, 85.0]])

movie_ratings_stars = movie_ratings / 20

tori_ratings = movie_ratings[:, 2]
print(tori_ratings)

marty_ratings = movie_ratings[:, 1]
print(marty_ratings[marty_ratings > 80])
