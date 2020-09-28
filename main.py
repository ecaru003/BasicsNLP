import json
import requests
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.probability import  FreqDist
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("stopwords")



url = "https://api.nytimes.com/svc/topstories/v2/arts.json?api-key="