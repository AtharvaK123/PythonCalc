import tkinter
m = tkinter.Tk()

def add (first, second):
    try:
        print('Here is your answer: ' + str(first + second))
    except: 
        print('You entered something wrong!')

def subtract (first, second):
    try:
        print('Here is your answer: ' + str(first - second))
    except: 
        print('You entered something wrong!')
    
def multiply (first, second):
    try:
        print('Here is your answer: ' + str(first * second))
    except: 
        print('You entered something wrong!')

def divide (first, second):
    try:
        print('Here is your answer: ' + str(first / second))
    except: 
        print('You entered something wrong!')

def abs (first, second):
    try:
        print('Here is your answer: ' + str(first ** second))
    except: 
        print('You entered something wrong!')

ans = 'y'

while(ans == 'y'):
    ans = input('Proceed? y/n ')
    
    if ans == 'n':
        break

    first = input('Enter your first number here >> ')
    type = input('What is your operand >> ')
    second = input('Enter your second number here >> ')

    try: 
        if(type == '+'):
            first = int(first)
            second = int(second)
            add(first, second)
        elif(type == '-'):
            first = int(first)
            second = int(second)
            subtract(first, second)
        elif(type == '*'):
            first = int(first)
            second = int(second)
            multiply(first, second)
        elif(type == '/'):
            first = int(first)
            second = int(second)
            divide(first, second)
        elif(type == '^'):
            first = int(first)
            second = int(second)
            abs(first, second)
    except: print('You entered something wrong')

    m.mainloop()