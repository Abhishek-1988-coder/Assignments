a=int(input("Enter a number:"))

def factorial(a):
    if a<2:
        return 1
    else:
        return a*factorial(a-1)
    
print("Factorial of "+ str(a) + " is:", factorial(a))


