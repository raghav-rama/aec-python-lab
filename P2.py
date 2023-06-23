'''Write a python program to simulate working of simple calculator.'''
def calculator():
    print("Welcome to the Simple Calculator!")
    while True:
        print("Please select an operator")
        print("1.Addition")
        print("2.Substraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit")
        choice=input("Enter your choice(1-5):")
        if choice=='5':
            print("Thank You for using Simple Calculator")
            break
        num1=float(input("Enter thr first number:"))
        num2=float(input("Enter the second number:"))
        result=None
        if choice=='1' or choice=='+':
            result=num1+num2
        elif choice=='2' or choice=='-':
            result=num1-num2
        elif choice=='3' or choice=='*':
            result=num1*num2
        elif choice=='4' or choice=='/':
            if num2!=0:
                result=num1/num2
            else:
                resut="Error, cannot divide by zero!!"
        else:
            print("invalid choice!!")
            if result is not None:
                print("Result",result)
            print()
calculator()