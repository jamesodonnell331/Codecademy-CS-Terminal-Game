#Codecademy CS Python Terminal Game
#Spiderman trivia/cardgame (working title)
score = 0

option1 = 'No dick head'
option2 = 'Absolutely not'
option3 = 'Amazing'
option4 = "That's crazy"
option5 = 'all of the above'

print("What is the simplest solution to this problem?")

print("A", option1)
print("B", option2)
print("C", option3)
print("D", option4)
print("E", option5)

answer = 'a'

if answer == 'A' or answer == 'a':
    score += 100
    print("Correct!")
else:
    print("Nope, sorry!")
    