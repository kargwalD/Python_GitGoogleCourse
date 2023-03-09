def greater(a,b):
    if a>b:
        return a
    else:
        return b
    
#Hello is greater; strlen is greater
print("The greater number is: " + greater("Hello","Hell"))

#Hellp is greater; ASCII value of p is higher
print("The greater number is: " + greater("Hello","Hellp"))

#Hellpo is greater
print("The greater number is: " + greater("Hello","Hellpo"))
