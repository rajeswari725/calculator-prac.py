
def menu():
    print("\n----------MENU-------------")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
def get_user_input():
   
        try:
            num1=float(input("enter the fist number: "))
            num2=float(input("enter the second number: "))
            return num1,num2
        except ValueError as e:
            raise ValueError(f"Invalid input. Please enter a valid number. ERROR: {e}")
def addition(num1,num2):
    return num1+num2       
def subtraction(num1,num2):
    return num1-num2  
def multiplication(num1,num2):
    return num1*num2  
def division(num1,num2):
    if num2==0:
        raise ZeroDivisionError("Division by zero is not possible.")
    return num1/num2
def main():
    while True:
        print("\nWelcome to the calculator")
        menu()
        choice=input("Enter your choice(1-4) or 5 to exit:")
        if choice not in ['1','2','3','4','5']:
            print(f"Your choice: ({choice}) is invalid. Please enter a valid choice.")
            continue
        if choice=='5':
            print("Thank you for using the calculator. Goodbye!")
            break
        try:
            num1,num2=get_user_input()
            if choice=='1':
                result=addition(num1,num2)
                print(f"Addition of {num1} and {num2}: {result:g}")
            elif choice=='2':
                result=subtraction(num1,num2)
                print(f"Subtraction of {num1} and {num2}: {result:g}")
            elif choice=='3':
                result=multiplication(num1,num2)
                print(f"Multiplication of {num1} and {num2}: {result:g}")
            elif choice=='4':
                result=division(num1,num2)
                print(f"Division of {num1} and {num2}: {result:.2f}")
        except ValueError as e:
            print(f"Invalid user input...{e}")
            continue
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            continue
if __name__=="__main__":
    main()