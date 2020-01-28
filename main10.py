#!/usr/bin/env python3
import sys, random #systems needed for function use

assert sys.version_info >= (3,7), "This script requires at least Python 3.7" #code version information


print('Greetings!') #prints a greeting on the screen for the user
colors = ['red','orange','yellow','green','blue','violet','purple'] # creates a list colors that contains strings that are colors
play_again = '' #creates the empty string variable play_again
best_count = sys.maxsize            # the biggest number on the system

while (play_again != 'n' and play_again != 'no'): #loop is active when the play_again varibale is not n or no
    match_color = random.choice(colors) #picks a radom color string from the colors list and assigns it to match_color
    count = 0 # sets a count varibale to 0
    color = '' #creates an empty string color variable
    while (color != match_color): # loops when color and match_color are not the same
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        #the above line asks the user to type in a color string
        color = color.lower().strip() #Color does need to worry about capitalization or spaces before and after the string
        count += 1 # increments the count variable
        if (color == match_color): # checks if color now matches with match_color
            print('Correct!') #prints if the if statement is true
        else: # happens when the if condition is not met
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) # if the if statement is false this prints
            #guesses used above is put in the format brackets and assigned as count in the format function to follow
    
    print('\nYou guessed it in {} tries!'.format(count))#once the color matches this statement prints

    if (count < best_count): #Checks if your count beat the current best guess
        print('This was your best guess so far!')#prints if the if statement is tru
        best_count = count#sets the new best guess number to how many guesses it took the user to win

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip() #asks the user to input a string to restart or end the loop

print('Thanks for playing!') #once the loop ends, this statement is printed to thank the user for playing the game