import requests as r

#question 2,3,4
print(r.__version__)

#curl step 5
var = r.get("http://google.com/")
print(var)

#get this code from github and print the content
my_python = r.get("https://raw.githubusercontent.com/nhervieu/CMPUT404_Lab1/master/lab1.py")
print(my_python.text)