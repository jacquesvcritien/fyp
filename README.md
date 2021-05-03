# Bitcoin Price Prediction Through Twitter Sentiment and Data Volume

This is the official repository for the the Bitcoin Price Prediction Through Twitter Sentiment and Data Volume Paper and Dissertation

<b>Author: Jacques Vella Critien</b>
<b>Supervisors: Dr Joshua Ellul, Prof Albert Gatt</b>

#### Structure

```
project
│   README.md  
│
└───data_generators_cleaners
│   │   BTCprices_cleaner.ipynb
│   │   data_grouper.ipynb
│   │   data_lag_creator.ipynb
│   │   english_tweets_extractor.ipynb
│   │   polarity_adder.ipynb
│   │   tweet_preprocessor.py
│   │   tweets_cleaner_finaliser.ipynb
│   │   
│   └───with_sentiment
│       │   
│       └───VADER
│            │   tweets.csv
│            └───cleaned
│                │   tweets.csv
│   
└───datasets
│   │
│   └───general
│   │   │   BTCDATAwithdate.csv
│   │   │   BTCTWEETS_english_no_duplicates.csv
│   │   │   preprocessed_tweets.csv
│   │   │   tweets_cleaned.csv
│   │
│   └───tweets_prices
│   │   │
│   │   └───vader
│   │       │   final_days_lag_days_1.csv
│   │       │   final_days_lag_days_3.csv
│   │       │   final_days_lag_days_7.csv
│   │       │   final_days_lag_hours_1.csv
│   │       │   final_days_lag_hours_3.csv
│   │       │   final_days_lag_hours_7.csv
│   │       │   
│   │       └───cleaned
│   │           │   final_days_lag_days_1.csv
│   │           │   final_days_lag_days_3.csv
│   │           │   final_days_lag_days_7.csv
│   │           │   final_days_lag_hours_1.csv
│   │           │   final_days_lag_hours_3.csv
│   │           │   final_days_lag_hours_7.csv
│   │
│   └───tweets_prices_volumes_sentiment
│       │
│       └───vader
│           │
│           └───day_datasets
│               │   final_days_lag_days_1.csv
│               │   final_days_lag_days_3.csv
│               │   final_days_lag_days_7.csv
│               │   final_days_lag_hours_1.csv
│               │   final_days_lag_hours_3.csv
│               │   final_days_lag_hours_7.csv
│               │   
│               └───cleaned
│                   │   final_days_lag_days_1.csv
│                   │   final_days_lag_days_3.csv
│                   │   final_days_lag_days_7.csv
│                   │   final_days_lag_hours_1.csv
│                   │   final_days_lag_hours_3.csv
│                   │   final_days_lag_hours_7.csv
│   
└───models
│   │
│   └───bilstm_multiclass
│   │   │   bilstm_multiclass.ipynb
│   │   │   bilstm_multiclass-tester.ipynb
│   │   │   model.png
│   │
│   └───bilstm_trend
│   │   │   bilstm_trend.ipynb
│   │   │   bilstm_trend-tester.ipynb
│   │   │   model.png
│   │
│   └───cnn_multiclass
│   │   │   cnn_multiclass.ipynb
│   │   │   cnn_multiclass-tester.ipynb
│   │   │   model.png
│   │
│   └───cnn_multiclass
│   │   │   cnn_multiclass.ipynb
│   │   │   cnn_multiclass-tester.ipynb
│   │   │   model.png
│   │
│   └───lstm_multiclass
│   │   │   lstm_multiclass.ipynb
│   │   │   lstm_multiclass-tester.ipynb
│   │   │   model.png
│   │
│   └───lstm_trend
│       │   lstm_trend.ipynb
│       │   lstm_trend-tester.ipynb
│       │   model.png
│   
└───papers
    │ ALL PAPERS USED   
```


##### data_generators_cleaners

This folder contains all the scripts required to clean and preprocess the data



1. <b>BTCprices_cleaner.ipynb</b> - Used to clean the prices dataset. More specifically, it sets the timestamp to UTC and removes the Open, Gigh and Low values.
2. <b>data_grouper.ipynb</b> - Used to group the lagged dataset hourly or daily
3. <b>data_lag_creator.ipynb</b> - Used to create lagged datasets
4. <b>english_tweets_extractor.ipynb</b> - Used to remove duplicates and non-English tweets
5. <b>polarity_adder.ipynb</b> - Used to add polarity and sentiment to tweets
6. <b>tweets_cleaner_finaliser.ipynb</b> - Used in the last step to remove tweets with less than 4 words after tweets being cleaned.
7. <b>tweet_processor.py</b> - Used to clean and preprocess tweets

##### datasets

This folder contains all the datasets


1. <b>general</b> - Contains the general datasets used to create lagged datasets including the original ones
    * <b>BTCDATAwithdate.csv</b> - This contains the cleaned BTC prices dataset
    * <b>BTCTWEETS_english_no_duplicates.csv</b> - This contains the dataset of tweets without duplicates and non-English tweets
    *  <b>preprocessed_tweets.csv</b> - This contains the tweets cleaned and preprocessed from the tweet_processor.py script
    *  <b>tweets_cleaned</b> - The final cleaned dataset

2. <b>tweets_prices</b> - Contains the datasets with each tweet together with the corresponding BTC price
   * <b>vader</b> - Datasets with VADER poalrity scores
        * <b>final_days_lag_days_1.csv</b> - Dataset containing uncleaned tweets and prices with 1 day lag
        * <b>final_days_lag_days_3.csv</b> - Dataset containing uncleaned tweets and prices with 3 days lag
        * <b>final_days_lag_days_7.csv</b> - Dataset containing uncleaned tweets and prices with 7 days lag
        * <b>final_days_lag_hours_1.csv</b> - Dataset containing uncleaned tweets and prices with 1 hour lag        
        * <b>final_days_lag_hours_3.csv</b> - Dataset containing uncleaned tweets and prices with 3 hours lag        
        * <b>final_days_lag_hours_7.csv</b> - Dataset containing uncleaned tweets and prices with 7 hours lag
        * <b>cleaned</b> - Contains cleaned datasets
            * <b>final_days_lag_days_1.csv</b> - Dataset containing cleaned tweets and prices with 1 day lag
            * <b>final_days_lag_days_3.csv</b> - Dataset containing cleaned tweets and prices with 3 days lag
            * <b>final_days_lag_days_7.csv</b> - Dataset containing cleaned tweets and prices with 7 days lag
            * <b>final_days_lag_hours_1.csv</b> - Dataset containing cleaned tweets and prices with 1 hour lag        
            * <b>final_days_lag_hours_3.csv</b> - Dataset containing cleaned tweets and prices with 3 hours lag        
            * <b>final_days_lag_hours_7.csv</b> - Dataset containing cleaned tweets and prices with 7 hours lag
3. <b>tweets_prices_volumes_sentiment</b> - Contains the grouped datasets with averaged polarity scores for that time interval with the corresponding BTC prices
   * <b>vader</b> - Datasets with VADER poalrity scores
        * <b>day_datasets</b> - Datasets grouped daily 
          * <b>final_days_lag_days_1.csv</b> - grouped uncleaned dataset with 1 day lag
          * <b>final_days_lag_days_3.csv</b> - grouped uncleaned dataset with 3 days lag
          * <b>final_days_lag_days_7.csv</b> - grouped uncleaned dataset with 7 days lag
          * <b>final_days_lag_hours_1.csv</b> - grouped uncleaned dataset with 1 hour lag        
          * <b>final_days_lag_hours_3.csv</b> - grouped uncleaned dataset with 3 hours lag        
          * <b>final_days_lag_hours_7.csv</b> - grouped uncleaned dataset with 7 hours lag
          * <b>cleaned</b> - Contains cleaned datasets
              * <b>final_days_lag_days_1.csv</b> - grouped cleaned dataset with 1 day lag
              * <b>final_days_lag_days_3.csv</b> - grouped cleaned dataset with 3 days lag
              * <b>final_days_lag_days_7.csv</b> - grouped cleaned dataset with 7 days lag
              * <b>final_days_lag_hours_1.csv</b> - grouped cleaned dataset with 1 hour lag        
              * <b>final_days_lag_hours_3.csv</b> - grouped cleaned dataset with 3 hours lag        
              * <b>final_days_lag_hours_7.csv</b> - grouped cleaned dataset with 7 hours lag

##### models

This folder contains all the models

1. <b>bilstm_multiclass</b> - Contains the implementation of the bilstm model which predicts the magnitude of the next day's closing price change
   * <b>bilstm_multiclass.ipynb</b> - The actual model implementation
   * <b>bilstm_multiclass-tester.ipynb</b> - Script which tests various combinations of hyperparameters to obtain comparable results
   * <b>model.png</b> - Model's figure
2. <b>bilstm_trend</b> - Contains the implementation of the bilstm model which predicts the direction of the next day's closing price
   * <b>bilstm_trend.ipynb</b> - The actual model implementation
   * <b>bilstm_trend-tester.ipynb</b> - Script which tests various combinations of hyperparameters to obtain comparable results
   * <b>model.png</b> - Model's figure
3. <b>cnn_multiclass</b> - Contains the implementation of the cnn model which predicts the magnitude of the next day's closing price change
   * <b>cnn_multiclass.ipynb</b> - The actual model implementation
   * <b>cnn_multiclass-tester.ipynb</b> - Script which tests various combinations of hyperparameters to obtain comparable results
   * <b>model.png</b> - Model's figure
4. <b>cnn_trend</b> - Contains the implementation of the cnn model which predicts the direction of the next day's closing price
   * <b>cnn_trend.ipynb</b> - The actual model implementation
   * <b>cnn_trend-tester.ipynb</b> - Script which tests various combinations of hyperparameters to obtain comparable results
   * <b>model.png</b> - Model's figure
1. <b>lstm_multiclass</b> - Contains the implementation of the lstm model which predicts the magnitude of the next day's closing price change
   * <b>lstm_multiclass.ipynb</b> - The actual model implementation
   * <b>lstm_multiclass-tester.ipynb</b> - Script which tests various combinations of hyperparameters to obtain comparable results
   * <b>model.png</b> - Model's figure
1. <b>lstm_trend</b> - Contains the implementation of the lstm model which predicts the direction of the next day's closing price
   * <b>lstm_trend.ipynb</b> - The actual model implementation
   * <b>lstm_trend-tester.ipynb</b> - Script which tests various combinations of hyperparameters to obtain comparable results
   * <b>model.png</b> - Model's figure

##### papers

This folder contains all the papers read to implement this study