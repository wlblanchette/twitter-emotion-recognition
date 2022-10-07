import os;
os.environ['KERAS_BACKEND'] = 'theano'

import pandas as pd
import json

from emotion_predictor import EmotionPredictor

# Pandas presentation options
pd.options.display.max_colwidth = 150   # show whole tweet's content
# pd.options.display.width = 200          # don't break columns
# pd.options.display.max_columns = 7      # maximal number of columns

PROJECT_ROOT = os.path.join(os.getcwd(), '../../..')
TWEETS_LOCATION = os.path.join(PROJECT_ROOT, 'state_tweets')

def load_tweets(state_name: str):
  file_name = os.path.join(TWEETS_LOCATION, f'{state_name.lower()}.json')
  with open(file_name) as f:
    tweets = json.load(f)
  return tweets

def get_model() -> EmotionPredictor:
  return EmotionPredictor(classification='ekman', setting='mc', use_unison_model=True)


# Data Science Questions:
#   * Should I filter out tweets that the model isn't confident about
#     classifying or just have an algorithm that weighs them less than tweets
#     it is more confident in?
#      * In a way this is playing into the biases of the model, whatever they
#        may be
#   * How many tweets do we need until the answer seems fair?
#   * How do we evaluate whether the answer is fair? Perhaps a correlation
#     score across users in the geographic area?

def process_tweets(model: EmotionPredictor):
  tweets = load_tweets('alabama')
  probabilities = model.predict_probabilities(tweets)
  print('probabilities')
  print(probabilities, '\n')
