'''
Name: Korey Dillon
Date: 06/3/24
Class: ISTA 130
Section Leader: N/A

Functions and Loops!!!
Building 8 functions where this function2.py file will successfully execute each function to test within the test_functions2.py file.
'''
#Input Statements
import math

#Defining a function called print_word with two parameters (int-integer, str-string).
def print_word(int, str):
    #i is my variable in range of the 'int' which will be changed each time in the arguments within the main function
    for i in range(int):
        #Below is the count for each time the loop cycles, i=i+1 so each time i will increase by 1 until it reaches the 'int' range
        i=i+1
        print(i,'-->',str)

#Function called bacteria with two integer parameters
def bacteria(min,bac):
    number=min
    cells=2
    #i is my variable in range of 5
    for i in range(bac):
        #i will count each cycle by 1 until it reaches 5
        i=i+1
        #First print executes given arguments before addition below
        print('after',min,'minutes: ',cells,'bacteria')
        #Addition to min and cells
        min=number+min
        cells=cells+cells

#Function called convert_to_copper with three integer parameters
def convert_to_copper(gold,silver,copper):
    #Equation I will use to calculate copper pieces from given silver, gold, and copper values
    total=(silver*5)+(gold*10*5)+copper
    print(gold,'gp,',silver,'sp,',copper,'cp','converted to copper is:',total,'cp')

#Function called convert_from_copper with a single parameter
def convert_from_copper(int):
    #Equation I will use to calculate my gold, silver, and copper pieces
    sp=0
    cp=0
    #math.floor is used to round down my answer
    gp=math.floor(int/50)
    #int%50 is saying int/50 and keeping my remainder
    remainder=int%50
    if remainder > 0:
        while remainder > 0:
            #5 copper pieces is equal to 1 silver piece 
            if remainder >= 5:
                remainder=remainder-5
                sp=sp+1
            else:
                #copper pieces left from remainder
                cp=remainder
                break
    print(int,'copper pieces is:',gp,'gp,',sp,'sp,',cp,'cp')

#Function called repeat_word with three parameters one string and two integers
def repeat_word(str,rows,columns):
    #i will be my variable in range of 'rows' which is given in the argument within main function
        for i in range(rows):
            #i will add by 1 each cycle until set range in 'rows'
            i=i+1
            print(str*columns)

#Function called text_triangle with an integer parameter
def text_triangle(int):
    #if the int = to 0 then print blank
    if int == 0:
        print('')
    for i in range(int):
        #if i = to 0
        if i == 0:
            #First line don't include a newline character with end parameter set to empty space
            print('x', end='')
        else:
            #For additional lines include the newline character
            print('\n' + 'x' * (i + 1), end='')
    print('')

#Function called surface_area_of_cylinder with two parameters radius and height of a cylinder
def surface_area_of_cylinder(radius,height):
    #surface area equation used in function
    sa=(2*math.pi*radius**2)+(2*math.pi*radius*height)
    print('The surface area of a cylinder with radius',radius,'and height',height,'is',sa)

#Function called tree_height with two parameters distance and length. 
#This function is used to evaluate myself from the tree as well as the kite string length.
def tree_height(distance,length):
    #pythagorean theorem equation used to provide height
    height=length**2-distance**2
    print(f'Kite string: {length}\nDistance: {distance}\nHeight: {math.sqrt(height)}')


#====================================================================================
def main():
    '''
    Main function that will call the above defined functions using arguments. 
    This main function is not needed for the assignment, this is to make the code a little more uniform.
    '''
    print_word(3,'banana')
    print_word(4,'mississippi')
    bacteria(10, 5)
    bacteria(21,3)
    convert_to_copper(5,10,7)
    convert_to_copper(15,23,12)
    convert_from_copper(200)
    convert_from_copper(1107)
    convert_from_copper(3242)
    repeat_word('Goblin',3,5)
    repeat_word('Kobold',5,3)
    text_triangle(3)
    text_triangle(10)
    text_triangle(0)
    surface_area_of_cylinder(10.0,10.0)
    surface_area_of_cylinder(0.0,1.0)
    tree_height(300, 500)
    tree_height(100, 141.421356)


if __name__ == '__main__':
    main()