import pandas as pd
import numpy as np

df = pd.read_csv(r'D:\PythonProjects\C141\venv\main.csv',encoding="utf-8")

C = df['vote_average'].mean()
m = df['vote_count'].quantile(0.9)
q_movies = df.copy().loc[df['vote_count']>=m]

def weighted_rating(x,m = m,C = C):
  v = x['vote_count']
  R = x["vote_average"]
  return (v/(v+m)*R)+(m/(m+v)*C)

q_movies['score'] = q_movies.apply(weighted_rating,axis = 1)

# SORT THE DATA BASIS ON SCORE
q_movies = q_movies.sort_values('score',ascending = False)
q_movies[['title','vote_count','vote_average','poster_link']].head(20).values().tolist()
