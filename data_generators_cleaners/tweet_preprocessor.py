#This script preproccesses tweets by doing the following
# 1. Removes URLs
# 2. Changes mentions to USER
# 3. Removes stop words 'a', 'is', 'with', 'in', 'the'
# 4. Keeps only the word after the # symbol if the word after the # symbol appears in the nltk dictionary 
# 5. Removes punctuation

#import
import pandas as pd
import nltk
from nltk import word_tokenize, sent_tokenize, FreqDist
from nltk.corpus import stopwords
from nltk.corpus import words
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.tokenize import TweetTokenizer
import re
import threading
import langdetect as ld
from nltk.corpus import words
import numpy as np
from multiprocessing import Process
import glob
import shutil
from multiprocessing import Manager
import multiprocessing
import os

lemmatizer = nltk.stem.WordNetLemmatizer()
tokenizer = TweetTokenizer()
detokeniser = TreebankWordDetokenizer()

def remove_punctuation(words):
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', (word))
        if new_word != '':
           new_words.append(new_word)
    return new_words

def lemmatize_text(text):
    return [(lemmatizer.lemmatize(w)) for w in tokenizer.tokenize((text))]

def detokenise_text(tokenised):
    return detokeniser.detokenize(tokenised)

def remove_URL(sample):
    return re.sub("(?P<url>https?://[^\s]+)", "", sample)
    
word_set = set(words.words())
def get_hashtag_text(word):
    global word_set
    #if not a hahstag return the word
    if(not word.startswith("#")):
        return word
    
    #remove hashtag
    word = word[1:]
    return word if (word in word_set) else ""

def preprocess_tweet(tweet):      
    #remove url
    tweet = remove_URL(tweet)
    #lemmatize
    tokenised = lemmatize_text(tweet)
    #keep only hashtags in english dictionary
    tokenised = [get_hashtag_text(word) for word in tokenised if get_hashtag_text(word) != ''] 
    #remove stop words
    stop_words = ["a", "the", "in", "with", "is"]
    tokenised = [word for word in tokenised if word not in stop_words] 

    #for each token
    for index, word in enumerate(tokenised):
        #if mentions
        if(word.startswith("@")):
            tokenised[index] = "USER"
            
    #remove tweets
    tokenised = remove_punctuation(tokenised)
            
    return detokenise_text(tokenised)
    

def thread_func(start_index, end_index, i):
    print("Starting process", i, ": start index", start_index, "end index", end_index)
    
    nrows = end_index-start_index
        
    tweets = pd.read_csv("./../datasets/general/BTCTWEETS_english_no_duplicates.csv", skiprows=[i for i in range(1,start_index+1)], nrows=nrows) if(start_index > 0) else pd.read_csv("./../datasets/general/BTCTWEETS_english_no_duplicates.csv", nrows=nrows)
    
    tweets['text'] = tweets['text'].apply(preprocess_tweet)
    
    print("Saving", len(tweets), "from proc", i);
    
    tweets.to_csv("./../datasets/cleaned_tweets/cleaned_tweets"+str(i)+".csv")

if __name__ == "__main__":  # confirms that the code is under main function

    tweets = pd.read_csv("./../datasets/general/BTCTWEETS_english_no_duplicates.csv");
    data_len = len(tweets)
    del tweets;
    
    #if storing directory does not exist, create it
    if not os.path.exists("./../datasets/cleaned_tweets"):
        os.makedirs("./../datasets/cleaned_tweets")

    
    pool = multiprocessing.Pool()
       
    print(data_len)
    procs_len= 1000
    procs = []

    for i in range(0,procs_len):
        length = data_len / procs_len
        start_index = int(i * length)
        end_index = int(start_index + length)
        pool.apply_async(thread_func, args=(start_index, end_index, i))
    pool.close()
    pool.join()
        
    print("Merging files")
    
    with open('./../datasets/general/preprocessed_tweets.csv', 'wb') as outfile:
        for i, filename in enumerate(glob.glob('./../datasets/cleaned_tweets/*.{}'.format('csv'))):
            with open(filename, 'rb') as readfile:
                if i !=0:
                    readfile.readline()
                shutil.copyfileobj(readfile, outfile)
        
