import json
import requests
import nltk
import main_functions
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.probability import  FreqDist
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("stopwords")


api_key_dict = main_functions.read_from_file("JSON_Files/api_key.json")

api_key = api_key_dict["my_key"]

url = "https://api.nytimes.com/svc/topstories/v2/arts.json?api-key=" + api_key


#print(url)
response = requests.get(url).json()

main_functions.save_to_file(response,"JSON_Files/response.json")