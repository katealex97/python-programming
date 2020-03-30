#PROBLEM 1 - Write a function called letter_count 

def letter_count(word, letter):
    for letter in word:
        count = 0
        count += 1
    print (count)

letter_count('this is going to be easy', 'i') #should return 3

#PROBLEM 2  - Write a function called count_words that takes a string and returns the number of words in the string.

def count_words():
    for each_word in count_words:
        count  = 0
        count += 1
        return count

count_words('hey there!!') #should return 2 

#Problem 3 - Write a function called reverse_list that takes a list and returns a new list with the items reversed.
def reverse_list(my_list):
    index = len(my_list) - 1
    reverse_list = []

    while index >= 0:
        reverse_list += my_list[index]
        index -= 1
    return reverse_list

my_list = [1, 2, 3]

print (reverse_list(my_list))

reverse_list([1,2,3])

#Problem 4 - Write a function called split_list t
def split_list(my_list, pivot):

new_list  = []
    for item in my_list:
        if item in my_list > pivot:
            new_list.append(item)

    return([my_list], [new_list])

print (split_list([4, 5, 11, 8, 19], 10))

# Problem 5 (Optional) Write a function called is_isogram
def is_isogram(any_string):
    count = 0
    for char in any_string:
        count += 1
    if count >= 1:
        return ('False')
    else:
        return('True')

value = 'hape coding'

print (is_isogram(value))

            
