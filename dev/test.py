def sum(x, y):
    return x + y

def divide(x, y):
    return x/y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y


if __name__ == "__main__":
    while True:
        print("hello people, how are you doing?")
        print("so, now you can use this programm for do somethink with numbers)")
        print("lets start!")
        print("At first think about what do you want to do")
        answer = input("do you want to use our programm or yourself?(our/myself/exit):")

        
        if answer == 'our':
            print("1.sum")
            print("2.divide")
            print("3.subtract")
            print("4.multiply")
            choice = input("please, choose programm: ")
            num1 = int(input("enter the first number: "))
            num2 = int(input("enter the second number: "))

                
            if choice == '1':
                print(num1, "+", num2 , "=", sum(num1,num2))
                a = sum(num1,num2)
            elif choice == '2':
                print(num1, "/", num2 , "=", divide(num1,num2))
                a = divide(num1,num2)
            elif choice == '3':
                print(num1, "-", num2 , "=", subtract(num1,num2))
                a = subtract(num1,num2)
            elif choice == '4':
                print(num1, "*", num2 , "=", multiply(num1,num2))
                a = multiply(num1,num2)
            else:
                print("invalid input")
                break
        
        if answer == 'myself':
            took = (input("take an action:"))
            num1 = int(input("enter the first number: "))
            num2 = int(input("enter the second number: "))


            if took == '+':
                print(num1, "+", num2 , "=", sum(num1,num2))
                a = sum(num1,num2)
            elif took == '/':
                print(num1, "/", num2 , "=", divide(num1,num2))
                a = divide(num1,num2)
            elif took == '-':
                print(num1, "-", num2 , "=", subtract(num1,num2))
                a = subtract(num1,num2)
            elif took == '*':
                print(num1, "*", num2 , "=", multiply(num1,num2))
                a = multiply(num1,num2)
            else:
                print("ok")
                break
        if answer == 'exit': 
            break  
        ask = (input("continue?:"))
        if ask == 'no':
            break

        if ask == 'yes':
            
            num3 = int(input("enter the number: "))
            action = (input("take an action:"))
            if action == '+':
                print(a, "+", num3, "=", sum(a, num3))
                a = sum(a, num3)
            elif action == '/':
                print(a, "/", num3, "=", divide(a, num3))
                a = divide(a, num3)
            elif action == '-':
                print(a, "-", num3, "=", subtract(a, num3))
                a = subtract(a, num3)
            elif action == '*':
                print(a, "*", num3, "=", multiply(a, num3))
                a = multiply(a, num3)
            else:
                print("ok")
                break
        does = input('do you want to continue yet?:')
        if does == 'no':
            break

        if does == 'yes':
            
            num3 = int(input("enter the number: "))
            act = (input("take an action:"))
            if action == '+':
                print(a, "+", num3, "=", sum(a, num3))
                a = sum(a, num3)
            elif action == '/':
                print(a, "/", num3, "=", divide(a, num3))
                a = divide(a, num3)
            elif action == '-':
                print(a, "-", num3, "=", subtract(a, num3))
                a = subtract(a, num3)
            elif action == '*':
                print(a, "*", num3, "=", multiply(a, num3))
                a = multiply(a, num3)
            else:
                print("ok")
                break
            break


           

    




                
            
             
        