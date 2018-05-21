# Movie Rating and Prediction Model
## Objective
The objective of this project is to utilize the IMDB data set to generate Meaningful and Interesting Insights and then create a movie rating model based on average IMDB ratings and a sentiment analysis score of user tweets. And also to create an accurate Machine Learning model to predict average movie ratings based on some key features and make the system scalable by using big data technologies for data processing and then host the system on Google Cloud.

## Technologies Used
- Spark
- Zeppelin
- Jupyter
- Twitter API
- Google Cloud Engine
- Sentiment Analysis (Text Blob)
- Python
- HTML5
- CSS3
- JavaScript

## Data Processing
The first step for this model is to utilize IMDB dataset and process it. Data preprocessing is done through a series of steps, namely:
- Cleaning
- Normalization
- Transformation
- Feature extraction
- Selection

For this model, IMDB dataset is used and the steps followed to extract the required data are:
1. Read the IMDB dataset.
2. Filter the data and extract only the movies. (Since the data contains series, and other sitcoms as well)
3. Now filter the movies on the basis of year. (Here we are taking 2000-2017)
4. Now read the data for directors.
5. Extract and flatten only the directors and then merge with the movies data set extracted above.
6. Now read the data for writers.
7. Extract and flatten only the writers and then merge with the movies data set extracted above.
8. Now arrange the dataset in descending order according to the movie year.

## Sentiment Analysis
Here we are ranking the top 10 movies for every year based on the tweets collected and performing sentiment analysis on them. Each movie received a score and then the scores were normalised and finally, the movies are ranked based on the scores received.

Data Processing is the initial step where we filter the movies for every year from 2010 till 2017. Next filter applied is getting movies with votes more than 10000 and then get the top 10 movies for every year. Then, we perform the sentiment analysis on the list of movies and rank them based on scores obtained.

All the sentiment analysis and script running is done on the Google Cloud Platform.

## Machine Learning
Here we are using Linear Regression Model and it is built using Spark ML library to predict the average rating of a movie based on some key features:
- Director name
- Writer Name
- Run Time of the Movie
- Genre of the Movie
- Year of Release

### Files:
1. The zeppelin notebook for Movie Rating Model is: Movie Rating Model.json
2. The zeppelin notebook for Sentiment Analysis is: Sentiment Analysis.json
3. The jupyter notebook for machine learning model is: Machine Learning - Movie Rating Prediction.ipynb
4. The python program to extract tweets and run sentiment analysis is: twittersearch.py
5. The output folder contains all the movies which are extracted using the Movie Rating Model.json

The datasets used are from the website: https://www.imdb.com/interfaces/
