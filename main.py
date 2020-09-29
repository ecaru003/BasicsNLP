import json
import requests
import nltk
import main_functions
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from pprint import pprint
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#nltk.download("punkt")
#nltk.download("stopwords")


api_key_dict = main_functions.read_from_file("JSON_Files/api_key.json")

api_key = api_key_dict["my_key"]

url = "https://api.nytimes.com/svc/topstories/v2/arts.json?api-key=" + api_key


#print(url)
#response = requests.get(url).json()

#main_functions.save_to_file(response,"JSON_Files/response.json")


my_articles = main_functions.read_from_file("JSON_Files/response.json")

str1 = ""

for i in my_articles["results"]:
    str1 = str1 + i["abstract"]

#print(str1)
sentences = sent_tokenize(str1)

words = word_tokenize(str1)

#print(words)

#fdist = FreqDist(words)

#pprint(fdist.most_common(10))

words_no_punc= []

for w in words:
    if w.isalpha():
        words_no_punc.append(w.lower())

#pprint(words_no_punc)

fdist2 = FreqDist(words_no_punc)

#pprint(fdist2.most_common(10))

stopwords = stopwords.words("english")

#print(stopwords)

clean_words = []

for w in words_no_punc:
    if w not in stopwords:
        clean_words.append(w)

pprint(len(clean_words))

fdist3 = FreqDist(clean_words)

pprint(fdist3.most_common(10))

wordcloud = WordCloud().generate(str1)


plt.figure(figsize=(12,12))
plt.imshow(wordcloud)

plt.axis("off")
plt.show()