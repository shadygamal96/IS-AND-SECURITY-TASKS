
import pandas as pd

metadata = pd.read_csv('movies_metadata.csv',
low_memory=False)

metadata.head(3)

metadata['overview'].head()

metadata.shape

C = metadata['vote_average'].mean()

print(C)

= metadata['vote_count'].quantile(0.90)

m = metadata['vote_count'].quantile(0.90)

print(m)

q_movies = metadata.copy().loc[metadata['vote_count'] >= m]

q_movies.shape

def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    # Calculation based on the IMDB formula
    return (v/(v+m) * R) + (m/(m+v) * C)

q_movies['score'] = q_movies.apply(weighted_rating, axis=1)

q_movies.shape

q_movies = q_movies.sort_values('score', ascending=False)

q_movies[['title', 'vote_count', 'vote_average', 'score']].head(20)


