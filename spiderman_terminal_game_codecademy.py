#Codecademy CS Python Terminal Game
#Spiderman trivia/cardgame (working title)
score = 0

option1 = 'No'
option2 = 'Absolutely not'
option3 = 'Amazing'
option4 = "That's crazy"
option5 = 'All of the Above'

print("A", option1) 
print("B", option2) 
print("C", option3) 
print("D", option4) 
print("E", option5)

input("What is the simplest solution to this problem?")

answer = 'a'

if answer == 'A' or answer == 'a':
    score += 100
    print("Correct!")
else:
    print("Nope, sorry!")

option1 = 'Miles Morales'
option2 = 'Spider Man'
option3 = 'Green Goblin'
option4 = "Dr. Octavius"
option5 = 'All of the Above'

print("A", option1) 
print("B", option2) 
print("C", option3) 
print("D", option4)
print("E", option5)

input("Who is the Prowler's nephew?")

answer = 'a'

if answer == 'A' or answer == 'a':
    score += 100
    print("Correct!")
else:
    print("Nope, sorry!")

print(score)
