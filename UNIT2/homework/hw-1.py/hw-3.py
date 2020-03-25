odd_strings = ['abba', '111', 'canal', 'level', 'abc', 'racecar',
'123451' , '0.0', 'papa', '-pq-']

count = 0
for string in odd_strings:
    #find strings greater than 3 and have same
    #first and last character
    first = string[0]
    last = string[len(string) - 1] #python allows neg. indexes last = string[-1]
    if len(string) > 3 and first = last:
        count += 1

print(count)


