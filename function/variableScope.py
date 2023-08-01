#Variable scope ,a scope define the area a variable can be access in

my_book = 'the boy that cry woof' #global scope variable 

def print_book():
    # global my_book   #if you want to override the global scope
    my_chair= 'black chair'     #local scope
    print('inside',my_book, my_chair)
print_book()   

print('outside',my_book)     