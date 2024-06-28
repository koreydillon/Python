'''

Returning Values and Simple Conditions!!!
Building 10 functions where this conditions.py file will successfully execute each function to test within the test_conditions.py file.
'''

def word_length(str, int):
  """
  Function that prints a message about the relationship between the length of the string and the integer.
  The str=string to compare with the integer.
  The int=integer to compare with the length of the word.
  """
  if len(str) == int:
    print('Exactly',int,'characters:',str)
  elif len(str) > int:
    print('Longer than',int,'characters:',str)
  else:
    print('Shorter than',int,'characters:',str)


def stop_light(color, sec):
  """
    Function determines the next color of a stop light based on color and seconds elapsed.
    The current color of the stop light (green, yellow, or red).
    The seconds the light has been showing its current color.
    Return the next color the stop light should change to.
  """
  if color == 'green' and sec > 60:
    return 'yellow'
  elif color == 'yellow' and sec > 5:
    return 'red'
  elif color == 'red' and sec > 55:
    return 'green'
  else:
    return color


def is_normal_blood_pressure(systolic, diastolic):
  """
    Function that checks if the given blood pressure readings are normal.
    Returns True if the blood pressure is normal, False if not.
  """

  print(systolic < 120 and diastolic < 80)


def is_normal_blood_pressure(systolic, diastolic):
  """
  Checks if the given blood pressure readings are normal.
  systolic: The systolic blood pressure reading.
  diastolic: The diastolic blood pressure reading.
  Returns True if the blood pressure is normal, False otherwise.
  """

  return systolic < 120 and diastolic < 80


def doctor():
  """
    Function will ask the user for blood pressure readings and provide feedback.
  """

  while True:
      systolic = int(input('Enter your systolic blood pressure reading: '))
      diastolic = int(input('Enter your diastolic blood pressure reading: '))
      break

  if is_normal_blood_pressure(systolic, diastolic):
    print('Your blood pressure is normal.')
  else:
    print('Your blood pressure is high.')


def pants_size(waist_size):
  """
  This function takes a waist size in inches as input and returns a string representing the pants size (small, medium, or large).
  waist_size - an integer representing a person's waist size in inches.
  Returns a string representing the pants size (small, medium, or large).
  """

  if waist_size >= 34:
    return 'large'
  elif waist_size >= 30:
    return 'medium'
  else:
    return 'small'


def pants_fitter():
  """
  This function guides the user through buying pants, calculating the total cost based on type and quantity.
  """
  name = input("Enter your name: ")
  print('Greetings' ,name, 'welcome to Pants-R-Us')
  while True:
      waist_size = int(input("Enter your waist size in inches: "))
      if waist_size >=34:
        size='large'
        break
      elif waist_size >=30:
        size='medium'
        break
      else:
        size='small'

  while True:
      num_pairs = int(input("How many pairs of pants would you like: "))
      if num_pairs > 0:
        break
      else:
        print("Number of pairs must be a positive integer. Please try again.")

  while True:
      pant_type = str(input("Would you like regular or fancy pants? "))
      if pant_type in ("regular", "fancy"):
        break
      else:
        print("Invalid input.")
  price_per_pair = 40 if pant_type == "regular" else 100
  total_cost = num_pairs * price_per_pair
  print(num_pairs, 'pairs of' ,size, pant_type, 'pants:', '$', total_cost)


def digdug(number):
  """
  This function prints "dig", "dug", or "digdug" for integers by 3, 5, or both up to a given number.
  number- a positive integer representing the upper limit.
  """

  for i in range(1, number):
    i=i+1
    if i % 3 == 0 and i % 5 == 0:
      print(i, ':', 'digdug')
    elif i % 3 == 0:
      print(i, ':', 'dig')
    elif i % 5 == 0:
      print(i, ':','dug')

def beef_type(percent_lean):
  """
  This function categorizes beef based on its lean percentage.
  percent_lean- a floating point number representing the lean percentage of the beef.
  Returns a string representing the type of beef ("Hamburger", "Chuck", "Round", "Sirloin", or "Unknown").
  """

  if percent_lean < 78:
    return "Hamburger"
  elif 78 <= percent_lean < 85:
    return "Chuck"
  elif 85 <= percent_lean < 90:
    return "Round"
  elif 90 <= percent_lean <= 95:
    return "Sirloin"
  else:
    return "Unknown"
def species_height(species, height):
    """
    This function compares a given height to the average height of a species and prints a message indicating if it's above, below, or at the average height.
    species- a string representing the species ("Human" or "Klingon").
    height- a positive float representing the height in inches.
    """

    average_height = {"Human": 67,"Klingon": 71}

    if species not in average_height:
      print('Average')
      return None

    average = average_height[species]
    if height > average:
      print('Above Average')
    elif height < average:
      print('Below Average')
    else:
      print('Average')

def sooner_date(month1, day1, month2, day2):
  """
  This function determines the sooner date of two given dates.
  month1 -an integer between 1 and 12 representing the first month.
  day1- an integer between 1 and 31 representing the first day.
  month2- an integer between 1 and 12 representing the second month.
  day2- aninteger between 1 and 31 representing the second day.

  Returns a string in the format "month / day" representing the sooner date.
  """

  if month1 == month2:
    print(month1, '/', min(day1, day2)) 
  elif month1 < month2:
    print(month1, '/', day1)
  else:
    print(month2, '/', day2)





#===============================================================
def main():

    word_length('liversnaps', 7)
    word_length('earwax', 5)
    word_length('chickenfat', 10)
    word_length('Gross!', 13)
    stop_light('green', 61)
    stop_light('yellow', 5)
    stop_light('yellow', 6)
    stop_light('red', 12)
    stop_light('red', 56)
    is_normal_blood_pressure(120,80)
    is_normal_blood_pressure(119, 80)
    is_normal_blood_pressure(119, 79)
    is_normal_blood_pressure(120, 79)
    doctor()
    doctor()
    pants_size(38)
    pants_size(34)
    pants_size(33)
    pants_size(29)
    pants_size(-20)
    pants_size(2000)
    pants_fitter()
    pants_fitter()
    pants_fitter()
    digdug(2)
    digdug(3)
    digdug(5)
    digdug(15)
    beef_type(91.2)
    beef_type(78)
    beef_type(87)
    beef_type(95.1)
    species_height("Human", 62.1)
    species_height("Klingon", 73)
    species_height("Klingon ", 71)
    sooner_date(1,1, 1, 2)
    sooner_date(2,5, 1, 3)
    sooner_date(8,25,7,30)

if __name__ == '__main__':
    main()
