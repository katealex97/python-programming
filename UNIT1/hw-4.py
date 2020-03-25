import random
#generate range of individuals in sample

#1 - 14 20%
#15 - 64 60%
#65 - 99 20%

one_to_14  = range (1,15)

fifteen_to_64 = range(15,65)

sixty_five_and_over = range(65,100)

population = []

for num in range (1, 101):
    val = random.random () #generate number between 0.0 and 1.0
    if val >= 0.8:
        #add age group over 65
        population.append(random.choice(sixty_five_and_over))
    elif val >= 0.21:
        #add 15 - 65 age group
        population.append(random.choice(fifteen_to_64))
    else: 
        #add 1-14 age group
        population.append(random.choice(one_to_14)

print(population)

count = 0
for age in population:
    if age >= 80:
        count += 1

print(count)
