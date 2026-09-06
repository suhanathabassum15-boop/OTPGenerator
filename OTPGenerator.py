import random
import string
s = string.digits
print(s)
n = int(input("Enter the length of Password:"))
password = " ".join(random.choice(s) for i in range(n))
print("Your Password is :",password)

