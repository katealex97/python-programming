secret = 7
user_val = int(input ('Enter your guess: '))
while user_val != secret:
    print('No, guess again: ')
    user_val = int(input('Enter your guess: ')


#check if a string is a palindrome 
#same forwards as backwards

#'level', 'racecar', 'aaaa'

#use a while loop
my_str = 'level'
rev_str = ''

while index >= 0:
    rev_str += my_str[index]
    index -= 1

print(rev_str)

if my_str == rev_str:
    print('palindrome!!')
else print('no palindrone')
