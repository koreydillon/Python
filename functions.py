'''
Learning how built-in print functions work!
'''


"""   *********************************
    Answers to questions:
    1) The sum of the arguments is: 11112142
    2) Chance of rain today: 14 %
    3) Chance of rain today: 94 %
    4) The angle in radians is: 1.571
    5) The angle in radians is: 3.142
    6) Result: 2.293
    7) Result: 3.902
    8) Result: 9.626
    ********************************* 
"""

import math, random

# Put your function definitions below this line:
def chases(predator, prey):
    print('The', predator,'chases the', prey)
def sum3(x, y, z):
    sum = x + y + z
    print('The sum of the arguments is:', + sum)
def forecast():
    sum=random.randrange(101)
    print('Chance of rain today:', + sum,'%')
def radians(degrees):
    radians = degrees * math.pi/180
    print('The angle in radians is:', + round(radians, ndigits=3))
def decimal(number):
    sum = number - math.floor(number)
    print('Decimal part:', round(sum, ndigits=3))
def erf_plus_gamma(number):
    sum = math.erf(number) + math.gamma(number)
    print('Result:', round(sum, ndigits=3))

#====================================================
def main():
    chases('dragon', 'human')
    chases('coyote', 'roadrunner')
    sum3(1, 2, 3)
    sum3(4, 5, 6)
    forecast()
    forecast()
    radians(200)
    radians(30)
    decimal(5.983)
    decimal(5.9839)
    erf_plus_gamma(0.6)
    erf_plus_gamma(0.22)


if __name__ == '__main__':
    main()
