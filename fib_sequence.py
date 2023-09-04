a=0
b=1
i=0
upTo=10
print("Fibonacci sequence up to " + str(upTo) + "\n")
while (i < upTo):
    print(a)
    temp=a+b
    a=b
    b=temp
    i+=1
