
# E02a-Control-Structures

- Open main01.py. Before running it, what do you expect this program to do? 
  - prints greetings and the imput statement. 

  - Now right click on the main1.py window and select “Run Python File in Terminal”. Click in the bottom panel, and answer the question. Describe what happened. 
  The program ended

  - What do you think the program did with what you typed in answer to the question?
  - it was saved in a randomly assigned memory location

- Open main02.py. Before running it, describe how this is different than main01.py.
- Assigned the input to a variable

  - What do you think the color = input() will do?
  - assigned the value that the user inputs to the variable color

  - Run the program in the terminal and answer the question. Did the program do what you expected?
  - yes it did

- Open main03.py. Before running it, describe how this is different than main02.py.
- The if statement will force the correct choice

  - What is happening on lines 9–12?
  - if the user inputs red they get the correct message otherwise they get the incorrect message

  - Why are lines 10 and 12 indented?
  - To designate what happens in the if and else statements

  - Run the program and answer the question. What happens if you don’t capitalize Red?
  - The incorrect is printed because the r is not capitalized

  - What does this tell you about "color"?
  - It must be the exact same string

- Open main04.py. Before running it, describe how this is different than main03.py.
- The if statement has two conditions for a correct color

  - What problem is this trying to solve?
  - That the R in red needs to be capitalized

  - Run the program and answer the question. What happens if you use some other capitalization scheme (i.e., “RED” or “reD“)?
  - The Incorrect message is displayed

- Open main05.py. What do you expect line 9 to do?
- Allows any capitalization scheme to be used to answer the question

  - What problem is it trying to solve?
  - The correct input color being given the wrong message

  - Run the program and answer the question. What happens if you add spaces before or after the word (i.e., “ RED “ or “ red”)?
  - The incorrect message is given again

 - Open main06.py. How is line 9 different than in main05.py?
 - It adds the strip() function
   
   - What would you guess .strip() is doing?
   - removing spaces on the front and end of a string
   
   - Run the program and answer the question. Is there another way of writing “red” that will break this logic?
   - Putting a space in between the letters of "red" such as "re d"
 
 - Open main07.py. Before running this program, how do you expect this to be different than main06.py?
 - There is an extra message that will be displayed if pink is input
   
   - What is happening on line 12?
   - an elif statement is used to give another option to the user besides red or nothing
   
   - Run the program and answer the question.
   - Displays pink or red. Still has the problem of a space in the middle breaking the logic
 
 - Open main08.py. What is the purpose of line 9?
 - Creates a loop that will continue to ask for input until the user gives the red input
   
   - Why are lines 10–17 indented?
   - The indentation is meant to include those lines inside the while loop
   
   - Run the program. What would happen if line 10 were moved before line 9 (and no longer indented)?
   - If the user input red correctly nothing would be run. If they input another color the program would loop infinitely because the user is never asked in the loop to give another answer
   
   - Make that change and run the program again. (To end any Python program, you can type ctrl-c)
   - Loops infinitely on wrong input and never loops on the right one

 - Open main09.py. What is happening on line 13?
 - We added a count variable and set it to 1 (default was 0)
   
   - What is the purpose of “count”?
   - Later in the program it will display how many tries we took to get the correct color
   
   - What is happening on line 22?
   - Prints the number of tries using the format funtion to add the count variable to the string in place
   of the parentheses

   - Run the program.
   - Ran the program and if red is input, the number correct statement and number of tries is displayed. If any other colors were used the Sorry message is seen then the input agian until the correct color and number of guesses are finally shown

 - *Extra credit:* open main10.py. Add a comment to each line describing what it is doing (a comment follows a pound sign [#]).
 - Commented all lines of main10.py

 - *Extra credit:* open main11.py. What is happening on lines 6-11?
 - Lines 6 - 11 define a function called choose_color. The function is given a last_color parameter. Inside the function, a list colors is created and filled with the strings 'red', 'orange', 'yellow', 'green', 'blue', 'violet' and 'purple'. A variable c is then created that is assigned a random color from the colors list. A while loop checks to see if the given parameter last_color is the same as the color assigned to the variable c. If it is, c is assigned a new random string value from the colors list and the loop checks again. The loop continues until the two variables are not the same and then the color assigned to c is returned from the function to be used in later code.