# Number of arguments for main function (get_value)
num_args = 0

from datetime import datetime

# Given a number of arguments, returns an arbitrary value
def get_value():
  current_datetime = datetime.now()
  return current_datetime.strftime("%d.%m.%Y - %H:%M")