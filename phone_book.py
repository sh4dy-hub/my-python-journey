

# phone book  desined by shady في 25 مايو 2025
# اول مشروع frist project


book ={
'01271210516':'shady',
'01071210516':'mathew',
'01171210516':'mina',
'01571210516':'fayez',
'01022932012':"paco",
'01122932012':"mario",
'01222932012':"mosht",
'01522932012':"sena",
}


def welcome () :
    print(' welcome your the programe ')
    your_name = input(' inter your name :  ')
    print ( 'hello' ,your_name  )

def list ():
    print('1- search by number ')
    print( "2-add number" )
    const = int(input('chosis service : '))
    if const == 1 :
        searsh_by_number()
    elif const == 2 :
        add_number()
    else :
        print (' the chose not found !')       

def searsh_by_number():
    number = input('inter the phone number to search : ')
    if number in book :
        print(f'this number who {book[number]} ')
    else :
        print('this is invailed number')
         
def add_number ():
    name = input(' inter the name : ')
    num = input( ' inter the phone number : ')
    contact = [name,num]
    book[num]= name
    print(f'contact saved : {name} - {num} ')
   



welcome()
list()

input('press inter to exit')

