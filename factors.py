running=True

print("FACTORS")
print()
while (running):
    print("Enter number or q to exit.")
    entry=input()
    if (entry=='q'):
        running=False
    else:
        try:
            numberEnter=int(entry)
            if (numberEnter>0):
                i=numberEnter
                j=1
                while(j<=i):
                    if (i%j==0):
                        print(j)
                    j+=1
        except:
            print("Not a real number.")


