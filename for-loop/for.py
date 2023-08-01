#for loop
names =['james', 'john', 'jack']
# for name in names:
#     print(name)
#     print(len(name))
#     print(name, len(name))

# for name in names[0;2]:
#     print(name)

# for name in names:
#     if name == 'john':
#         print(f'found {name}')
#         break  #when you find the name you are looking for you can break out of the loop
#     else:
#        print(name)

#while loop
school = 10
student =0

while student < school:
    if student == 0:
        student += 1
        continue #continue through the loop and skip the rest of the code
    if student % 2 == 0:
        print(student)
    if student <= 4:
        break
    student += 1    