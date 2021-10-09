#1^3+2^3+3^3=1+8+27=36
#Based on the number of digits entered, raise it to the power of that number. eg. 3 digits rasied to 3rd power, 4 digits raised to 4th power, etc. Each digit will be raised to the power. Then add the values together

#numbers = []
#result = ()
#while True:
#    number = input("Please enter a number (enter done if finished): ")
#    if number != 'done':
#        numbers.append(number)
#    else:
#        break
number = input("Please enter a number: ")
x = len(number)
result = 0
for i in number:
    result = result + int(i) ** x
if result == int(number):
    print("It's armstrong number")
else:
    print("It's not armstrong number")
