## I. What Does This Project Do?
Upon enterring any movie belonging to this [huge dataset](https://raw.githubusercontent.com/tusharnandy/MLProjects/master/RecEng/movie_dataset.csv) from IMDB, the code returns a list of 50 similar movies based on a technique called **word to word cosine similarity**. 

## II. Why is this project useful?
1. People are more likely to watch movies that have been directed by the same director, have similar cast, or perhaps belongs to the same genre.
2. *Cosine similarity* is most useful when an online movie app is in its intial stage. This makes use of the data of the movies rather than relying on the scarce user data that the app may have collected.
3. There was a lot to learn while implementing it.

Of course, there are far more sophisticated techniques such as collaborative filtering that can map and classify user behaviour to recommend a movie that a user is more likely to watch.

## III. How can YOU get started with this project?

### First, Cosine Similarity
1. Let's say that we have to find the similarity between "Tushar Nandy" and "Harshit Nandy"
2. There are 3 unique words here: "Tushar", "Harshit" and "Nandy". This means that our vector space is 3-dimensional
3. The three axes are: (Tushar, Harshit, Nandy)
4. Now, the number of repitions of a word in a string decides the value/coordinate on that particular axis
5. In this example,
  - The coordinates of "Tushar Nandy" are: (1,0,1)
  - The coordinates of "Harshit Nandy" are: (0,1,1)
  - The coordinates of "Tushar Nandy Harshit Nandy" would have been: (1,1,2)
6. The similarity index of this pair is the cosine of the angle between them.

And we're done!!

### Next, begin by applying this concept in Python
- File: **cosine_similarity_self.py**

### Coming to the main project, have a look at this step by step implementation
- File: **CosSimRecEngg.ipynb**

## IV. References
- Code Heroku's [video](https://www.youtube.com/watch?v=XoTwndOgXBM)
- Count Vectorizer [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer)
- Cosine Similarity [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html#)
