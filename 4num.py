num1 = int(input("Digite el primer número: "))
num2 = int(input("Digite el segundo número: "))
num3 = int(input("Digite el tercer número: "))
num4 = int(input("Digite el cuarto número: "))

if num1 >= num2 and num1 >= num3 and num1 >= num4:
    if num2 >= num3 and num2 >= num4:
        print("segundo mayor ->", num2)
    elif num3 >= num2 and num3 >= num4:
        print("segundo mayor ->", num3)
    else:
        print("segundo mayor ->", num4)
        
    
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    if num1 >= num3 and num1 >= num4:
        print("segundo mayor ->", num1)
    elif num3 >= num1 and num3 >= num4:
        print("segundo mayor ->", num3)
    else:
        print("segundo mayor ->", num4)
    

elif num3>num1 and num3>num2 and num3>num4:
    if num4 >= num2 and num4 >= num1:
        print("segundo mayor ->", num4)
    elif num2 >= num1 and num2 >= num4:
        print("segundo mayor ->", num2)
    else:
        print("segundo mayor ->", num1)

else:
    num4>num1 and num4>num2 and num4>num3
    if num3 >= num2 and num3 >= num1:
        print("segundo mayor ->", num3)
    elif num2 >= num1 and num2 >= num3:
        print("segundo mayor ->", num2)
    else:
        print("segundo mayor ->", num1)

