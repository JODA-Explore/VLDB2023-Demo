# pip install vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Create a SentimentIntensityAnalyzer object.
sid_obj = SentimentIntensityAnalyzer()

def detect_text_sentiment(text):
    

    sentiment_dict = sid_obj.polarity_scores(text)
    compound = sentiment_dict['compound']

    if compound >= 0.05:
        overall_sentiment = "Positive"

    elif compound <= - 0.05:
        overall_sentiment = "Negative"

    else:
        overall_sentiment = "Neutral"

    return  overall_sentiment

# Number of arguments for main function (get_value)
num_args = 1
# Return Type
ret_type = "STRING"
# Given a number of arguments, returns an arbitrary value
def get_value(arg1):
  overall_sentiment = detect_text_sentiment(arg1)
  return overall_sentiment
       