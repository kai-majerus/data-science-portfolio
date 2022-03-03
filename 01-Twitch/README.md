# Twitch Exploratory Analysis
This project is a part of my [Data Science Portfolio](https://github.com/kai-majerus/data-science-portfolio).

#### -- Project Status: [Active]

## Project Intro/Objective
The purpose of this project is to:
* Explore using an API to retrieve data from Twitch
* Conduct a basic exploratory data analysis of the data that is collected
* Plot some simple charts to visualize the data
* Investigate the relationships between variables in the dataset

### Methods Used
* Using an API
* Data Analysis
* Data Visualization

### Technologies
* Python
* Pandas, jupyter
* Requests

## Project Description
Data sources
* [Twitch API](https://dev.twitch.tv/docs/api)

Hypothesis
  1 There is a positive relationship between minutes streamed and followers
  2 Mature content is more popular
  3 What is the best time for a streamer to go live?
  4 What are the top games on Twitch?
  5 Who is the most popular streamer on Twitch in terms of followers/subscriptions/views?

Challenges
* The data needed to answer these questions is split across many different endpoints. Finding the right endpoints in order to gather the data to answer these questions will be a challenge. 
* Twitch API has the Get Streams endpoint which returns information about live streams. Unfortunately, it does not have an endpoint that returns all streams (live and offline). Therefore, one approach to creating the dataset would be to use the Get Streams endpoint multiple times over a given period and then combine the results into a dataset. An alternative would be to conduct the analysis using just the live streams.

## Scope of this project
- creating the dataset from the API
- data exploration/descriptive statistics
- data processing/cleaning
- data visualisation
- writeup/reporting of hypotheses and results.

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. For the moment, this project is entirely contained in [this notebook](https://github.com/kai-majerus/data-science-portfolio/blob/master/01-Twitch/Twitch%20Analysis.ipynb).
