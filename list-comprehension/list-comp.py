#LIST COMPREHENSION
#List comprehension is an elegant way to define and create lists based on existing lists.
#List comprehension is generally more compact and faster than normal functions and loops for creating list.
#However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly.
#Remember, every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension.
#Syntax:
prices=[10,20,30,40,50,60,70,80,90,100]
dl_prices =[]
for price in prices:
    dl_prices.append(price*2)
print(dl_prices)

#List comprehension
dl_prices = [price*2 for price in prices]
print(dl_prices)

#square of numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
sqr_numbers_even =[]
for number in numbers:
    if(number**2)%2==0:
        sqr_numbers_even.append(number**2)
print(sqr_numbers_even)

#List comprehension
sqr_numbers_even = [number**2 for number in numbers if (number**2)%2==0]
print(sqr_numbers_even)