def get_calculation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation =='-':
        return num1 - num2
    elif operation == '*':
        return num1*num2
    elif operation == '/':
        return num1/num2 

    else: return None




def main():
    num1=input("enter first number:")
    num2= input("enter second number:")
    if num1.isdigit()and num2.isdigit():

        operation = input ("choose your opertation(*,/,+,-")
        answer= get_calculation(int(num1),int(num2),operation)

        if answer == None:
            print("the operation is not valid")
        else:
            print("the answer is "+str(answer))
    else:
        print ("the input is not a number")
main()
pass 




if name == 'main':
    main()