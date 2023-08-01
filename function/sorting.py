#set and sorting sorted() in python capital letter comes first, set is a new data type set() is used to remove duplicates
def school_count(dictionary):
    grades =list(dictionary.values())
    for grade in set( grades):
        num = grades.count(grade)
        print(f'there are {num} {grade} school')


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
school_count(schools)    