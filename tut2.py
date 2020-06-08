x = input("1st number")
y = input("2nd number")
z = input("3rd number")
num1 = float(x)
num2 = float(y)
num3 = float(z)
def max_num(num1 , num2 , num3 ):
    if num1>=num2 and num1>=num3:
        return(num1)
    elif num2>= num1 and num2>=3:
        return(num2)
    else:
        return(num3)
print(max_num(num1 , num2 , num3 ))    


            