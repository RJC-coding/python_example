print("Enter filename to open.")
filename=input()
try:
    file = open(filename, "r")
    for line in file:
        print(line)
except:
    print("File could not be opened.")
