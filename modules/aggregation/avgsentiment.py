

# Number of arguments for main function (aggregate)
num_args = 1

# Initial state
def init_state():
  # [#SentimentValue, #SentimentCount]
  return [0.0, 0]

# Aggregate function, takes a state and the specified number of arguments and returns a new state
def aggregate(state, arg1):
  if arg1 == "Positive":
    state[0] += 1
  elif arg1 == "Negative":
    state[0] -= 1

  # Count
  state[1] += 1
  return state

# Merges the own state with another state
def merge(state, other):
  state[0] += other[0]
  state[1] += other[1]
  return state

# Returns the aggregation result based on the state
def finalize(state):
  # Sentiment score between -1.0 and 1.0
  sentiment_score = state[0] / state[1]
  if sentiment_score > 0.9:
    return "Very Positive"
  elif sentiment_score > 0.5:
    return "Positive"
  elif sentiment_score > 0.1:
    return "Somewhat Positive"
  elif sentiment_score > -0.1:
    return "Neutral"
  elif sentiment_score > -0.5:
    return "Somewhat Negative"
  elif sentiment_score > -0.9:
    return "Negative"
  else:
    return "Very Negative"

