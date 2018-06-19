#Ask the user do they want to start the quiz then ignore their response
value = input("Are you ready to begin the quiz?\n")

counter = 0

#Let them know the quiz is ready to start
print("Okay here we go anyways\n")

#Start the first question
questionOne = int(input("Q1) What is the capital of Ireland?\n\t1) Sydney\n\t2) Croatia\n\t3) Dublin\n"))
while(questionOne >=4 or questionOne <= 0):
    print("Your response must be either 1, 2 or 3!\n")
    questionOne = int(input("That is not one of the suggested value please try again!"))

#Check to see if the user got the question correct or not
if(questionOne == 3):
    print("That's right")
    counter = counter + 1
else:
    print("Sorry, the correct answer is number 3, Dublin")

#Second question
questionTwo = int(input("Q2) What is the color of the sun?\n\t1) Yellow\n\t2) pink\n\t3) blue\n"))
while(questionTwo >= 4 or questionTwo <= 0):
    print("Your response must be either 1, 2 or 3!\n")
    questionTwo = int(input("That is not one of the suggested value please try again!"))

#Check to see did the user get the correct answer
if(questionTwo == 1):
    print("That's right")
    counter = counter + 1
else:
    print("Sorry, the correct answer is yellow")

#Creating the third question which is a true/false question
questionThree = int(input("Is it possible to walk on water?\n\t1) No\n\t2) Yes\n"))
while(questionThree >= 3 or questionThree <= 0):
    print("Your response must be either 1 or 2!\n")
    questionThree = int(input("That is not one of the suggested value please try again!"))

#Check to see if the user got the answer correct
if(questionThree == 1):
    print("That's correct!")
    counter = counter + 1
else:
    print("Sorry you really can't walk on water, unfortunately!")

print("The quiz is now complete!\nYou scored", counter, " out of three, well done!")

