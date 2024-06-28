'''

Dictionaries with Lists as Values !!!
Building functions where this emoticons.py file will successfully execute each function to test with test_fimoticon.py
'''

def load_twitter_dicts_from_file(filename, emoticons_to_ids, ids_to_emoticons):
  """
  function reads a twitter data file and populates two dictionaries
  filename- the name of the file to read, emoticons_to_ids- an empty dictionary to store emoticons and their user IDs
  ids_to_emoticons- an empty dictionary to store user IDs and their emoticons.
  """
  with open(filename, 'r') as file:
    for line in file:
      #split the line by whitespace
      emoticon, tweet_id, user_id, timestamp = line.strip().split()

      #remove quotes from emoticon and user_id
      emoticon = emoticon.strip('"')
      user_id = user_id.strip('"')

      #update dictionaries
      if emoticon not in emoticons_to_ids:
        emoticons_to_ids[emoticon] = []
      emoticons_to_ids[emoticon].append(user_id)

      if user_id not in ids_to_emoticons:
        ids_to_emoticons[user_id] = []
      ids_to_emoticons[user_id].append(emoticon)
  return None


def find_most_common(dict):
  """
  function finds the most common key in a dictionary
  data_dict- dictionary with strings as keys and lists as values
  returns the key with the longest list as its value
  """
  most_common_key = max(dict, key=lambda key: len(dict[key]))
  count = len(dict[most_common_key])
  print(f"{most_common_key:<21}occurs{count:>9} times")
  return most_common_key

#======================================================================

def main():
  """
  main function that reads data, analyzes the emoticons and prints the results
  """
  emoticons_to_ids = {}
  ids_to_emoticons = {}
  #call function above with file and empty dictionaries
  load_twitter_dicts_from_file("twitter_emoticons.dat", emoticons_to_ids, ids_to_emoticons)

  #print number of emoticons and user ids
  print(f"Emoticons: {len(emoticons_to_ids)}")
  print(f"UserIDs:   {len(ids_to_emoticons)}\n")

  #find most common emoticons 5 times
  for _ in range(5):
    most_common = find_most_common(emoticons_to_ids)
    emoticons_to_ids.pop(most_common)


if __name__ == "__main__":
  main()
