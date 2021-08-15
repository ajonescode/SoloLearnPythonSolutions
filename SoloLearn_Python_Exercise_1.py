#Let's imagine you want to buy an ice-cream for 10 of your friends.
#Write a program that will take the money you have and the price of one ice-cream, 
#and will output the remaining money only if you can buy that ice-cream for your all 10 friends.

a = money = int(input())
b = price = int(input())
c = total_price = b * 10
d = balance = a - c
e = a//b
if c <= 100:
   print(d)
elif e >= 10:
   print(balance)
else:
   print()