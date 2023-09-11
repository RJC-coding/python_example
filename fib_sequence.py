a=0
b=1
i=0
print("Fibonacci sequence")
print("Enter a number.")
#number=
try:
    upTo=int(input())
    print("Fibonacci sequence up to " + str(upTo) + "\n")
    while (i < upTo):
        print(a)
        temp=a+b
        a=b
        b=temp
        i+=1
except:
    print("Could not use this number.")
