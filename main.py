score = 0

# Easy Quiz
answer1 = input("What US state is Area 51 located in? \na. California \nb. Michigan \nc. Washington D.C \nd. Nevada \nAnswer: ")
if answer1 == "d" or answer1 == "Nevada":
    score += 100
    print("Correct!")
    print("Score: ", score)
    print("\n")
else: 
    score -= 100
    print("Incorrect! The answer is Nevada.")
    print("Score: ", score)
    print("\n")

answer2 = input("Which restaurant's mascot is a clown? \na. Hungry Jacks \nb. KFC \nc. McDonalds \nd. Oporto \nAnswer: ")
if answer2 == "c" or answer2 == "McDonald's" or answer2 == "mcdonalds":
    score += 100
    print("Correct!")
    print("Score: ", score)
    print("\n")
else: 
    score -= 100
    print("Incorrect! The answer is McDonald's.")
    print("Score: ", score)
    print("\n")

answer3 = input("What is Cyanophobia the fear of? \na. Dogs \nb. Cats \nc. Cyanide \nd. Clowns \nAnswer: ")
if answer3 == "a" or answer3 == "dogs" or answer3 == "Dogs":
    score += 100
    print("Correct!")
    print("Score: ", score)
    print("\n")
else: 
    score -= 100
    print("Incorrect! The answer is Dogs.")
    print("Score: ", score)
    print("\n")

answer4 = input("When one is envious, they are said to be what colour? \na. Purple  \nb. Blue \nc. Green \nd. Violet \nAnswer: ")
if answer4 == "c" or answer4 == "Green" or answer4 == "green":
    score += 100
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    score -= 100
    print("Incorrect! The answer is Green.")
    print("Score: ", score)
    print("\n")

answer5 = input("How long is an olympic swimming pool(in metres)? \na. 500m \nb. 50m \nc. 100m \nd. 75m \nAnswer: ")
if answer5  == "b" or answer5 == "50m" or answer5 == "50":
    score += 100
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    score -= 100
    print("Incorrect! The answer is 50m.")
    print("Score: ", score)
    print("\n")