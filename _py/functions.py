# Libraries
import re
import nltk
import unicodedata

from bs4 import BeautifulSoup 
from nltk.stem.porter import *
from nltk.stem import RSLPStemmer
from nltk.corpus import stopwords

nltk.download('rslp')

def Tokenize(sentence):
    """Tokenize Function"""
    #sentence = sentence.lower()
    sentence = nltk.word_tokenize(sentence)

    return sentence

def Stemming(sentence):
    """Stemming Function"""
    stemmer = RSLPStemmer()
    phrase = []
    for word in sentence:
        phrase.append(stemmer.stem(word.lower()))

    return phrase

def remove_URL(sentence):
    """Remove URLs Function"""
    url = re.compile(r'https?://\S+|www\.\S+')

    return url.sub(r'', sentence)

def remove_emoji(sentence):
    """Remove Emojis Function"""
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)

    return emoji_pattern.sub(r'', sentence)


def strip_accents(sentence):
    """Remove Accents Function"""
    try:
        sentence = unicode(sentence, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass
    
    sentence = unicodedata.normalize('NFD', sentence)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")
    
    return str(sentence)


# fç to remove numbers
def drop_numbers(sentence):
    sentence_new = []
    for i in sentence:
        if not re.search('\d', i):
            sentence_new.append(i)
    return ''.join(sentence_new)