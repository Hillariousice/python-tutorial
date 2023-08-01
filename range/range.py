#ranges generate a list of numbers which we can then use to iterate over with for loops

#  for n in range(5):
#         print(n) #this will print 0-4

# for n in range(3,10): #3 is the starting point and 10 is the ending point
#     print(n) #this will print 3-9

# for n in range(3,16,4): #3 is the starting point,10 is the ending point and 4 is the step
#     print(n) #this will print 3-9

pie = ["cream","potatoes","apple","meat","pumpkin"]
# for n in range(len(pie)):
#     print(n,pie(n)) its going to print each other with their position

# for n in range(len(pie)-1,-1,-1):
#     print(n,pie(n))

for n in range(len(pie)-1,2,-2):
    print(n,pie(n))

