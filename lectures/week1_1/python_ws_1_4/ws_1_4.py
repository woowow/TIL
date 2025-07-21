# 아래에 코드를 작성하시오.
def get_movie_recommendation(rating):
    if rating >= 9:
        return movies[0]
    elif rating >= 8 and rating < 9:
        return movies[1]
    elif rating >= 7 and rating < 8:
        return movies[2]
    else:
        return movies[3]


movies = ['Inception', 'Interstellar', 'Dunkirk', 'Tenet']

print("Enter your movie rating (0-10): ", end='')
rate = int(input())
print(f"Recommended Movie: {get_movie_recommendation(rate)}", end='')