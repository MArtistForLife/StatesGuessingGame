import turtle as turt # to help with visualizing
import pandas as pd

screen = turt.Screen()
screen.title("USA States Game")
picture = "blank_states_img.gif"
screen.addshape(picture)
turt.shape(picture)

statesGuessed = []

# check if guess is among 50 states
theStates = pd.read_csv("50_states.csv") # to read file
playerScore = 0 # starting point when you start guessing

while len(statesGuessed) < 50:
    gameResponse = screen.textinput(title = f"Guess the state! {playerScore}/50", prompt = "What's the name of a state?").title() # to help us ignore case in responses
    print(gameResponse) # will confirm in terminal what we typed :)

    if gameResponse.lower() == "exit":
        statesMissing = [state for state in theStates["state"] if state not in statesGuessed]
        newData = pd.DataFrame(statesMissing, columns=["state"])
        newData.to_csv("statesToLearn.csv")
        break

    if gameResponse in theStates["state"].values: # if our guess is in that csv file
        if gameResponse not in statesGuessed:
            statesGuessed.append(gameResponse) # we need to add to the list of states already guessed
            print("Correct!")
            playerScore += 1 # increase score by 1

            stateData = theStates[theStates["state"] == gameResponse] # look at data of state inside theStates that was your gameResponse
            x = stateData["x"].values[0] # pull the x-coordinate of the guessed state
            y = stateData["y"].values[0] # pull the y-coordinate of the guessed state
            # .values makes the DataFrame a NumPy array, which extracts values from that column
            # [0] will make sure you get the first and only x- or y- value retrieved from array for that guessed state (in this case, one row because the guess means one correct response)

            # create a turtle lol
            t = turt.Turtle()
            t.penup() # don't draw lines!!
            t.goto(x,y) # to use coordinates of guessed state 
            t.write(gameResponse, align="center") # write state's name in the center 
            t.penup() # to prevent drawing lines after writing

        else:
            print("Nice, but you already answered this. Try again ^^")
    else:
        print("Whoops! Try again :)")

print(f"Your final score is {playerScore} out of 50.")