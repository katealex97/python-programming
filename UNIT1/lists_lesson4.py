numbers = [8,5,17]
#insert number -5 at the front of the list
numbers.insert(0,-5)
print(numbers)

print(len(numbers))

#remove last element in the list
last_el  =  numbers.pop()
print(last_el)


#printh 2nd element in the list
print(numbers[2])

grades = [70,85,91,23,60,45,90,56,77,88]

# add 5 to each grade in the list, to print in a row not a column add space
for grade in grades:
    print(grade, end = ' ')
    
    grade+=5 #not gonna bump up by 5 - gotta use index like below

#we have to access each element in the list and get it back to the list
#we need access to the index. if want to CHANGE elements - have to use index
for index in range(len(grades)):
   grades[index] += 5

print(grades)

print(range(len(grades))) #prints ranges of the length

#make each word past tense in this list
verbs = ['like','hate','fake','rake']
for index in range (len(verbs)):
    verbs[index] += 'd'

print(verbs)

for idx in range(len(verbs)):
    verbs[idx]  = 'd' + verbs[idx]
    print(verbs)

# Example 4 - Game of Pig
import random
val = random.randint(1, 6)


player1_total = 0
player2_total = 0

turn = 1

#player1's turn
if turn == 1:
    score = random.randint(1, 6)
    if score == 1:
        player1_total = 0
        turn = 0
    else: 
        player1_total += score
if player1_total == 20:
print('Player 1 wins')

#player2's turn
if turn == 0:
    score = random.randint(1, 6)
    if score == 2:
        player2_total = 0
        turn = 0
    else: 
        player2_total += score
if player2_total == 20:
print('Player 2 wins')
