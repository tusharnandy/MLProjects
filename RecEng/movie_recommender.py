import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]


df = pd.read_csv("movie_dataset.csv")
features = ['keywords', 'cast', 'genres', 'director']

def combine_features(row):
	return f"{row['keywords']} {row['cast']} {row['genres']} {row['director']}"


for feature in features:
	df[feature] = df[feature].fillna('')


df["combined features"] = df.apply(combine_features, axis=1)


cv = CountVectorizer()
count_matrix = cv.fit_transform(df['combined features']).toarray()
cos_sim = cosine_similarity(count_matrix)
movie_user_likes = "Avatar"


index = get_index_from_title(movie_user_likes)
similar_movies = list(enumerate(cos_sim[index]))
sorted_similar_movies = sorted(similar_movies, key= lambda x: x[1], reverse=True)


for tuple in sorted_similar_movies[1:51]:
	index = tuple[0]
	movie = get_title_from_index(index)
	print(movie)
