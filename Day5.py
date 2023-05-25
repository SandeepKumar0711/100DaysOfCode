# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to PyPassword Generator!")
no_of_letters=int(input("How many letters would you like in your password?"))
no_of_symbols=int(input("How many symbols would you like?"))
no_of_numbers=int(input("How many symbols would you like?"))
password=""
for i in range(no_of_letters):
    password+=letters[random.randint(0,len(letters)-1)]

for i in range(no_of_symbols):
    password+=symbols[random.randint(0,len(symbols)-1)]

for i in range(no_of_numbers):
    password+=numbers[random.randint(0,len(numbers)-1)]
list1=[]

for i in password:
    list1.append(i)
random.shuffle(list1)
password=""
for i in list1:
    password+=i

print("Here is your password: ",password)