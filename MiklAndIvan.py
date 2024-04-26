min = int(input())
M = int(input())
J = int(input())

if M >= min and J >= min :
    print("2")
elif M >= min and J <= min :
    print("Mike")
elif M <= min and J >= min :
    print("Ivan")
elif M+J >= min :
    print("1")    
else :
    print("0")
