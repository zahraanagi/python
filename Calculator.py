print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

option =int(input('choose an opertation: '))


if(option in range(1,5)):
    num1=int(input(" enter first number"))
    num2=int(input(" enter second number"))

    if option==1:
        result=num1+num2 
        a='+' 
    elif option==2:
        result=num1-num2 
        a='-' 
    elif option==3:
        result=num1*num2 
        a='*' 
    elif option==4: 
        result=num1/num2 
        a='/'        
    
    print(f"{num1} {a} {num2} = {result}")
    
else:
    print(" Invalid operation")
