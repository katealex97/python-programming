#if score is between 80 and 100, print A
#if score is between 60 and 79, print B
#if score is between 50 and 59, print C
#otherwise print D


readings = [25, 18, -5, 11, -3, -15, 8, -18, 6, 13]
#count number of negative readings
'''count = 0
for temp in readings:
    if temp < 0:
         count += 1 #adding 1 to count

print(count)'''

#find average of positive readings
total = 0
count = 0
for temp in readings:
    if temp > 0:
        count += 1
        total += temp
    
avg= total/count 

print avg

#print("The average is", cal_average([18,25,3,41,5]))
 
#find avg of positive readings, working with strings
titles = 'The Avengers', 'the avengers age of ultran', 'Captain America', 'the fist Avenger'

#count how many titles have 'The' in it
count = 0
for title in titles:
    if 'The' in title:
        count += 1

print ('list has {} titles with "The"'.format(count))

#how many vowels in a string
string = 'There is a long string that has only a few vowels'

count = 0
for char in string:
    if char in 'aeiou':
        count += 1

print('string has {} vowels in it'.format(count))