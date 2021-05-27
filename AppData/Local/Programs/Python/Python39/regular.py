import re
def funct(str):
    regex = re.compile("aeiou")
    if(regex.search(str)== None):
        print("given string has vowels")
    else:
        print("given string has no vowels")

str=input("enter your string ")
funct(str)

    
