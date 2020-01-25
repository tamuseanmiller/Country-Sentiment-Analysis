import search
import sentiment
import logging
import coloredlogs
import news

coloredlogs.install("DEBUG")
search.work('en', '30.627768,-96.333205,50mi')
news.getNews('College Station')
opinion = sentiment.run_sentiment_analysis('tweets.txt')
opinion += sentiment.run_sentiment_analysis('news.txt')

if opinion > 0:
    opinion = "+" + str(opinion)
elif opinion < 0:
    opinion = "-" + str(opinion)
else:
    opinion = str(opinion)

logging.info("Opinion of city is: " + opinion)
