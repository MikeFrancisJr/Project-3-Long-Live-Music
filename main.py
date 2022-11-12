# Show the game Title 
print(r"""
              __        __                  ___ 
        |    /  \ |\ | / _`    |    | \  / |__  
        |___ \__/ | \| \__>    |___ |  \/  |___ 
                                        
                          __     __    /        
               |\/| |  | /__` | /  `  /         
               |  | \__/ .__/ | \__, .       

""")

# Display instructions on how to play the game
print("Welcome to LONG LIVE MUSIC! Today we will test your love for music.")
print("In a moment you will answer 5 different questions that will determine")
print("if you are a 'High Level', 'Mediocre', or 'Low Level' fan of this")
print("art form.")
print()
print("Please ONLY enter 'T' for True or 'F' for False as your answer.  Enjoy!")
print()

# Create a tuple that holds the list of questions
questions = ("Q1. Beyonce was the lead singer of a group called 'Destiny's Child'", "Q2. Notorious BIG died in 2007", "Q3. Jay-Z's real name is Shawn Carter", "Q4. Taylor Swift won her first grammy in 2005", "Q5. Rihanna's first album is called 'Music in the Sun'")

# Create a tuple that holds the list of answers
answers = ("T", "F", "T", "F", "T")

# Create a variable that holds the length of questions
numberOfQuestions = len(questions)

# Create an empty variable that holds the value of the user's guess
userGuess = ""

# Create a variable that counts the number of turns
count = 0

# Create a for loop that loops through the each question in the tuple
for index in range(numberOfQuestions):
  print(questions[index])
  
  # Create a loop that continues as long as user's guess doesn't equal 'T' or 'F'
  while(userGuess != "T" and userGuess != "F"):

    #Prompt the user to enter an answer
    userGuess = input("Please enter your answer: ")
    print()

    # Compare and track if the user's guess is the same as the answer in the tuple
    if(userGuess == answers[index]):
      count += 1

  # Create a variable with a default value for user's guess inside the while loop 
  userGuess = ""

print(f"You answered {count} out of {numberOfQuestions} correctly!")

# If user guesses all 5 correctly
if(count == 5):
  print("You are a 'High Level' music fan! Congratulations and thanks for playing!")

elif(count >= 3):
  print("You are a 'Mediocre' music fan. Good job and thanks for playing!")

else:
  print("You are a 'Low Level' music fan.  Sorry, but thanks for playing.")