import random

quitinput = str(input("Type 'quit' to leave, press enter to start the game\n"))

while quitinput != 'quit':
    userinput = input("Choose between Rock, Paper, Scissor: ")
    options = ["Rock", "Paper", "Scissor"]
    computer = random.choice(options)

    userwins = 0
    computerwins = 0

    wintext = "you won!"
    tietext = "its a tie!"
    losetext = "you lost!"

    if userinput == "Rock" and computer == "Scissor":
        userwins += 1
        print(wintext)
    elif userinput == "Paper" and computer == "Rock":
        userwins += 1
        print(wintext)
    elif userinput == "Scissor" and computer == "Paper":
        userwins += 1
        print(wintext)
    elif userinput == computer:
        print(tietext)
    else:
        computerwins += 1
        print(losetext)

    totalrounds = userwins + computerwins

# testcode
