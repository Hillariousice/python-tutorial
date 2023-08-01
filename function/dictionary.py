#dictionaries is a mapping type which means basically its a set of key value pair(javascript object notation)
#if you want to retrieve the value you can use [], sometimes its good to check if a value exist before retrieving (key in dict)(.keys())(.values())
#(.count()) person ={name="lane",age=12, height="tall"}

def school_intro(dictionary):
    for key, val in dictionary.items():
        print(f'my school is {key} and is a {val}')
schools ={}
while True:
    school_name = input('enter school name:')
    school =input('enter type of school:')
    schools[school_name] = school

    another = input('add extra?(y/n)')
    if another == 'y':
        continue
    else:
        break

school_intro(schools)