# 아래에 코드를 작성하시오.
movies = ['Inception', 'Interstellar', 'Dunkirk', 'Tenet']
ratings = [9, 8.5, 7.5, 6]

movies_list = []

def get_high_rated_movies(threshold):
    for movie in movies_list:
        if movie['rate'] >= threshold:
            good_movies_list.append(movie)

for movie, movie_rate in zip(movies, ratings):
    movie_info = dict(name=movie, rate=movie_rate)

    movies_list.append(movie_info)

print(movies_list)
print(f"Enter the rating threshold: ", end='')
user_threshold = float(input())
print(f"Movies with a rating of {user_threshold} or higher:")
good_movies_list = []

get_high_rated_movies(user_threshold)

for movie in good_movies_list:
    print(movie['name'])