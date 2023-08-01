#string formatting 
num1 = 3.1425467389
num2 = 10.2903948

#previous
print("num 1 is", num1, "and num 2 is", num2)

#format method
print('num 1 is {0} and num 2 is{1}'.format(num1, num2)) #when you use this you can output different variables into the string
#if you want to use precision you can use this .format method
print('num 1 is {0:.3} and num 2 is{1:.3}'.format(num1, num2)) 
#you can also use f-floating point numbers
print('num 1 is {0:.3f} and num 2 is{1:.3f}'.format(num1, num2)) 

#using f-strings
print(f'num 1 is {num1:.4f} and num 2 is {num2:.4f}') #this is the most recent way to do it

