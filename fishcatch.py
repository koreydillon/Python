'''

Dictionaries with Lists as Values !!!
Building functions where this fishcatch.py file will successfully execute fish names and weights
'''


def fish_dict_from_file(fname):
  """
  defined function reads a fish catch data file and creates a dictionary with fish names and weights
  fname- the name of the file to read
  returns the dictionary that contain the fish names and weights
  """
  #dictionary mapping numbers to fish names
  fishmap = {3:'Roach', 4:'?', 2:'Whitefish', 5:'Smelt', 6:'Pike', 1:'Bream', 7:'Perch'}

  #empty dictionary for fish weights
  fish_data = {}

  with open("fishcatch.dat", "r", encoding="UTF-8") as f:

    #read each line in the file
    for line in f:
      #split the line by empty space 
      data = line.strip().split()

      #extract fish code and weight
      fish_code = int(data[1])
      weight = data[2]

      #skip lines with missing weight 'NA'
      if weight != 'NA':
          
        #get fish name from code using fishmap
        fish_name = fishmap.get(fish_code)

        #if fish name exists add weight to its list
        if fish_name:
          if fish_name in fish_data:
            fish_data[fish_name].append(float(weight))
          else:
            fish_data[fish_name] = [float(weight)]
  return fish_data

def fish_report(fish_data):
  """
  function will print a report showing fish in alphabetical order and mean weight in grams
  """
  print('   # NAME          MEAN WT')
  for fish_name, weight in sorted(fish_data.items()):
    #total weight and number of fish
    tot_weight = sum(weight)
    num_fish = len(weight)
    tot_weight2=(f"{(tot_weight/num_fish):.1f}")


    #format and print fish statistics with right and left justification
    print(f"{num_fish:4} {fish_name:10}{tot_weight2.rjust(10)}g")



#==================================================================
def main():
  #calling above function
  fish_weights = fish_dict_from_file('fishcatch.dat')
  if fish_weights:
    fish_report(fish_weights)
  else:
    print('No fish data found in file.')

if __name__ == '__main__':
  main()
