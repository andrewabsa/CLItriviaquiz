score = 0

# Easy Quiz
# welcome to quiz message
# Startup screen



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

if score <= 0:
    print("Easy Quiz: Final Score:", score, "- You need more practice")
elif score >= 200:
    print("Easy Quiz: Final Score:", score, "- Not bad")
else: 
    print("Easy Quiz: Final Score:", score, "- You are the best!")



#End of easy quiz, insert feedback
#start of medium quiz (welcome message maybe?)

# Medium Quiz
answer1_2 = input("True or False? There are 86400 seconds in a day. \na. True \b. False \nAnswer: ")
if answer1_2 == "True" or answer1_2 == "a" or answer1_2 == "true":
    score += 100
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    score -= 100
    print("Incorrect! The answer is True.")
    print("Score: ", score)
    print("\n")

answer2_2 = input("Which country invented ice cream? \na. Denmark \nb. France \nc. China \nd. Japan \nAnswer: ")
if answer2_2 == "c" or answer2_2 == "China" or answer2_2 == "china":
    score += 100
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    score -= 100
    print("Incorrect! The answer is China.")
    print("Score: ", score)
    print("\n")

answer3_2 = input("Which former NBA player was nicknamed Agent Zero? \na. Lebron James \nb. Michael Jordan \nc. Charles Barkley \nd. Gilbert Arenas \nAnswer: ")
if answer3_2 == "d" or answer3_2 == "Gilbert Arenas" or answer3_2 == "gilbert arenas":
    score += 100
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    score -= 100
    print("Incorrect! The asnwer was Gilbert Arenas")
    print("Score: ", score)
    print("\n")

answer4_2 = input("What tissues connect the muscles to the bones? \na. Tendons \nb. Ligaments \nc. Connective tissue \nd. Fibrous tissue \nAnswer: ")
if answer4_2 == "a" or answer4_2 == "Tendons" or answer4_2 == "tendons":
    score += 100
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    score -= 100
    print("Incorrect! The asnwer was Gilbert Arenas")
    print("Score: ", score)
    print("\n")

answer5_2 = input("Is an eggplant a fruit or vegetable? \na. Fruit \nb. Vegetable \nAnswer: ")
if answer5_2 == "a" or  answer5_2 == "fruit" or answer5_2 == "Fruit":
    score += 100
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    score -= 100
    print("Incorrect! The answer was fruit")
    print("Score: ", score)
    print("\n")

if score <= 0:
    print("Current Score: ", score, "- Don't quit your day job")
elif score >= 200:
    print("Current Score: ", score, "- Meh")
else: 
    print("Current Score", score, "- You rock!")


#Hard Quiz

answer1_3 = input("What is the weight of a Gold Bar in Fallout: New Vegas? \na. 30g \nb. 50g \nc. 35g \nd. 40g \nAnswer: ")
if answer1_3 == "c" or answer1_3 == "35g":
    score += 100
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    score -= 100
    print("Incorrect! The answer was 35g")
    print("Score: ", score)
    print("\n")

answer2_3 = input("If you planted the seeds of Quercus robur what would grow? \na. Trees \nb. Fungi \nc. Tomatoes \d. Lemons \nAnswer: ")
if answer2_3 == "a" or answer2_3 == "Trees" or answer2_3 == "trees":
    score += 100
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    score -= 100
    print("Incorrect! The answer was trees")
    print("Score: ", score)
    print("\n")

answer3_3 = input("On which day did ARPANET suffer a 4 hour long network crash? \na. 28635 \nb. 28521 \nc. 27639 \nd. 29521 \nAnswer: ")
if answer3_3 == "d" or answer3_3 == "29521":
    score += 100
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    score -= 100
    print("Incorrect! The answer was 29521")
    print("Score: ", score)
    print("\n")

answer4_3 = input("How many protons are in an oxygen atom? \na. 8 \nb. 12 \nc. 6 \nd. 16 \nAnswer: ")
if answer4_3 == "a" or answer4_3 == "8":
    score += 100
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    score -= 100
    print("Incorrect! The answer was 8")
    print("Score: ", score)
    print("\n")

answer5_3 = input("What animal has the highest metabolism? \na. Octopus \nb. Lizard \nc. Hummingbird \nd. Lion \nAnswer: ")
if answer5_3 == "c" or answer5_3 == "Hummingbird" or answer5_3 == "hummingbird":
    score += 100
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    score -= 100
    print("Incorrect! The answer was Hummingbird")
    print("Score: ", score)
    print("\n")



