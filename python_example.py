import datetime

class user:
    print("Please enter your name.")
    userName = ""
    
    def setUserName(self, newUserName):
        self.userName=newUserName
        if len(self.userName)>100:
            print("This name is too long.")
            self.userName=""
        if len(self.userName)==0:
            print("Please enter your name.")
            
    def getUserName(self):
        return self.userName

class main:
    user = user()
    while len(user.getUserName())==0:
        newUserName = input().strip()
        user.setUserName(newUserName)
    currentDay = datetime.datetime.now().strftime("%A")
    responseText = "Hello, {}. It is {}."
    print(responseText.format(user.userName, currentDay))

main = main()
