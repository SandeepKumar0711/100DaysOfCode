import os
# import art2
# print(art2.logo)
bid_list={}
choice='yes'
print("Welcome to the secret auction program.")
while choice=='yes':
  name=input("What is your name?:")
  bid=int(input("What's your bid?: $"))
  bid_list[name]=bid
  choice=input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if choice=='yes':
    os.system('cls')
max=0
for key,value in bid_list.items():
  if max<value:
    max=value
    name=key
os.system('cls')
print(f"The winner is {name} with a bid of ${max}.")
