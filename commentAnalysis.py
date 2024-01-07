# For Fetching Comments 
from googleapiclient.discovery import build 
# For filtering comments 
import re 
# For filtering comments with just emojis 
import emoji
# Analyze the sentiments of the comment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

API_KEY = 'AIzaSyDIdrPdFFWtnnd1e8sMY2Kf5GrzVa2LEYk'