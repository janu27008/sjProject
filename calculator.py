
import math


def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def expo(x,y):
    return(x**y)
def squareroot(x):
    return (math.sqrt(x))
def mod(x,y):
    return(x%y)
def fact(x):
    if x < 0:
        return "Error! Factorial of a negative number is not defined."
    elif not float(x).is_integer():
        return "Error! Factorial is only defined for integers."
    return(math.factorial(int(x)))


def calculator():
    print("select an operation")
    print('1.ADDITION')
    print('2.SUBSTRACTION')
    print('3.MULTIPLICATION')
    print('4.DIVISION')
    print('5.EXPONENTIAL')
    print('6.SQUARE ROOT')
    print('7.MODULUS')
    print('8.FACTORIAL')
    

   
    option=input('enter the operation number [1/2/3/4/5/6/7/8]')

    if option in ['1','2','3','4','5','6','7','8']:
        if option in ['1','2','3','4']:
                a=float(input("enter any number"))
                b=float(input("enter any number"))
                if option=='1':
                     print(a+b)
                elif option=='2':
                    print(a-b)
                elif option=='3':
                    print(a*b)
                elif option=='4':
                    print(a/b)
                else:
                    print('invalid input')
    
        if option in ['5','6','7','8']:
             if option=='5':
                    b=float(input("enter any number")) 
                    print(a**b)
             elif option=='6':
                    a=float(input("enter any number"))
                    print(math.sqrt(a))
             elif option=='7':
                    print(a^b)
             
             elif option=='8':
                    b=float(input("enter any number")) 
                    print(math.factorial(a))
             else:
                    print('invalid input')
       
def main():
    while True:
        calculator()
        next_calculation=('if you want to continue type yes or else no')
        if next_calculation !='yes':
            break

if __name__=='__main__':
    main()
