#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 20:16:11 2024

@author: shirley
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file = pd.read_csv("movie_dataset.csv")
print(file)


file['Revenue (Millions)'].fillna(file['Revenue (Millions)'].mode()[0], inplace =True)
print(file)

# file['Metascore'].fillna(file['Metascore'].mode()[0], inplace =True)


#Movies Directed by Christian Nolan and mean of his rating
df = pd.read_csv("movie_dataset.csv")
nolan_counts = df[df["Director"] == "Christopher Nolan"]
print("Movies Directed by Christopher is:", nolan_counts)

median_rating_nolan_movies = nolan_counts['Rating'].median()
print("The median rating of movies directed by Christopher Nolan is:", median_rating_nolan_movies)

#Highestrated movie
highest_rated_movie = df[df['Rating'] == df['Rating'].max()]
highest_rated_movie_title = highest_rated_movie['Title'].iloc[0]
print("Highest rated movie title is:", highest_rated_movie_title)


#Movies released in 2016
M_2016_counts = (df["Year"] == 2016).sum()
print("The number of movies released in 2016 is:", M_2016_counts)


#Movies with at least rating above 8.0
rating_above_8 = (df['Rating'] >= 8.0).sum()
print("The number of movies with a rating of at least 8.0 is:", rating_above_8)


#The average rating for each year
avg_rating_by_year = df.groupby('Year')['Rating'].mean()
year_highest_avg_rating = avg_rating_by_year.idxmax()
print("Highest rating is:",year_highest_avg_rating)


movies_2015_to_2017 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
avg_rev_2015_to_2017 = movies_2015_to_2017['Revenue (Millions)'].mean()
print("The average revenue of movies from 2015 to 2017 is:", avg_rev_2015_to_2017)


#The percentage increase in number of movies made between 2006 and 2016
movies_release_2006 = df[df['Year'] == 2006]
movies_release_2016 = df[df['Year'] == 2016]

movies_release_2006  = df[df['Year'] == 2006]
movies_release_2016 = df[df['Year'] == 2016]
count_movies_2006 = len(movies_release_2006)
count_movies_2016 = len(movies_release_2016)
percentage_increase = ((count_movies_2016- count_movies_2006) / count_movies_2006) * 100
print(percentage_increase,"%")

Actors = df['Actors'].str.split(', ').explode()

# Finding the most common actor
most_common_actor = Actors.mode().iloc[0]
print("The most common actor in all movies is:", most_common_actor)


# Calculating the unique genres
df["Genre"] = df["Genre"].apply(lambda x: [genre.strip() for genre in x.split(",")])
general_genre = [genre for genre_list in df['Genre'] for genre in genre_list]
unique_genres = len(set(general_genre))
print("The number of unique genres in the dataset is:", unique_genres)


# Movie Correlation Matrix
df = df.select_dtypes(include =["float", "int"])
movie_correlation = df.corr()
sns.heatmap(movie_correlation, annot=True, cmap="coolwarm", fmt = ".2f")
plt.title("Correlation Heatmap")
plt.show()
