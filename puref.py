import pdb
from functools import reduce


# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
print(list(map(lambda pet_name: pet_name.upper(), my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
print(list(zip(my_strings, sorted(my_numbers))))
# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(lambda score: score > 50, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

print(reduce(lambda accu, num: accu+num, scores+my_numbers, 0))

print([num if num % 2 == 0 else 0 for num in range(1, 100)])

def something(num1,num2):
    pdb.set_trace()
    return num1+num2

something(1,'3')