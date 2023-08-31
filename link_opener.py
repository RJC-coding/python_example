#https://www.geeksforgeeks.org/how-to-open-url-in-firefox-browser-from-python-application/

import webbrowser

# Passing firefox executable path to the
# Mozilla class.
firefox = webbrowser.Mozilla("C:\\Program Files\
\Mozilla Firefox\\firefox.exe")

file = open("links.txt")
for link in file:
    if (link[0:3]=="www"):
        firefox.open(link)
  
# Using open() function to display the URL.
#firefox.open(link)
