#https://www.geeksforgeeks.org/how-to-open-url-in-firefox-browser-from-python-application/

import webbrowser

complete=False;

firefox = webbrowser.Mozilla("C:\\Program Files\
\Mozilla Firefox\\firefox.exe")

while complete==False:
    print("Please enter a file to open links from.")

    fileName = input()

    try:
        file = open(fileName)
        for link in file:
            if (link[0:3]=="www"):
                firefox.open(link)
        complete=True;

    except:
        print("Could not find this file.")

