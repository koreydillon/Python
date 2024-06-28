'''
Name: Korey Dillon
Date: 06/15/24
Class: ISTA 130
Section Leader: N/A

While loops and if statements!!!
Building functions where this pig.py file will successfully execute each function to test within the test_pig.py file.
'''

#input statements
import random



def print_scores(player1_name, player1_score, player2_name, player2_score):
  """
  function prints the scores of two players
  player1_name the name of the first player (string)
  player1_score the score of the first player (integer)
  player2_name the name of the second player (string)
  player2_score the score of the second player (integer)
  """
  print('\n--- SCORES'f"\t{player1_name}: {player1_score}\t{player2_name}: {player2_score} ---")

def check_for_winner(name, score):
  """
  function checks if the player has a winning score and returns a boolean
  """
  #True if equal or greater than 50
  if score >= 50:
    print(f'THE WINNER IS: {name}!!!!!')
    return True
  else:
    return False
  
def roll_again(name):
  """
  function prompts the player to roll again and returns True if they want to or False if not
  """
  while True:
    answer = input(f'Roll again, {name}? (Y/N) ')
    if answer in ['Y','y']:
      #True if answer is 'Y' False if not
      return True
    elif answer in ['N','n']:
      break
    else:
      print(f'''I don't understand: "{answer}". Please enter either \"Y\" or \"N\".''')

def play_turn(name):
  """
  function will simulate a players turn by rolling a die and keeping track of the points
  
  """

  # print players turn with 10 hyphens each side
  print(f"{'-' * 10} {name}'s turn {'-' * 10}")

  #initialize points earned and rolls taken this turn
  points = 0
  num_rolls=1

  while True:
    #roll the die (1-6)
    roll = random.randint(1, 6)
    #print the roll result with arrows
    print(f'\t<<< {name} rolls a {roll} >>>')
     
    #update points for first roll and additional rolls
    if num_rolls == 1:
      #set points to the first roll value
      points = roll
      #print points after first roll
      print(f"\tPoints: {points}")
    elif roll == 1:
      print(f"\t!!! PIG! No points earned, sorry {name} !!!")
      points=0
      input('(enter to continue)')
      #exit the loop after Pig roll
      break
    else:
      #print points from each additional roll
      points = points + roll
      print(f"\tPoints: {points}")
    #ask to roll again using roll_again function
    if not roll_again(name):
      #exit the loop if player doesn't want to roll again
      break
    num_rolls = num_rolls + 1
  #return the total points earned this turn
  return points
#===============================================================
def main():
  """
  Main function for Pig Dice game.
  """

  #print title with two blank lines
  print("\n\nPig Dice")

  #get player names
  player1_name = input("Enter name for player 1: ")
  player2_name = input("Enter name for player 2: ")

  #welcome message with tab
  print(f"\tHello {player1_name} and {player2_name}, welcome to Pig Dice!")

  #initialize player scores
  player1_score = 0
  player2_score = 0

  #print initial scores
  print_scores(player1_name, player1_score, player2_name, player2_score)

  #while loop
  while True:
    #player 1 turn
    player1_score += play_turn(player1_name)
    print_scores(player1_name, player1_score, player2_name, player2_score)
    
    #check if player 1 won
    if check_for_winner(player1_name, player1_score):
      break

    #player 2 turn
    player2_score += play_turn(player2_name)
    print_scores(player1_name, player1_score, player2_name, player2_score)

    #check if player 2 won
    if check_for_winner(player2_name,player2_score):
      break

if __name__ == "__main__":
  main()


