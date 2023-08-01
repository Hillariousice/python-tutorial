#maps is a kind of way to apply a function to a list of elements and slip the result into a new list
from random import shuffle

def luxury(car):
    anagram = list(car)
    shuffle(anagram)
    return ''.join(anagram)
cars = ['ford','bmw','volvo','toyota','mercedes','tesla']
anagrams =[]
 
# for car in cars:
#     anagrams.append(luxury(car))
# print(anagrams)

# print(list(map(luxury,cars)))

#list comprehension
print([luxury(car) for car in cars])


