#https://www.geeksforgeeks.org/how-to-open-url-in-firefox-browser-from-python-application/

import webbrowser

# Passing firefox executable path to the
# Mozilla class.
firefox = webbrowser.Mozilla("C:\\Program Files\
\Mozilla Firefox\\firefox.exe")

print("Please enter a file to open links from.")

fileName = input()

try:
#file = open("links.txt")
    file = open(fileName)
    for link in file:
        if (link[0:3]=="www"):
            firefox.open(link)

except:
    print("Could not find file.")
  
# Using open() function to display the URL.
#firefox.open(link)
