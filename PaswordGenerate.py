import random
import string

length = int(input("Len of the password: "))

chars = string.ascii_letters + string.digits + "!@#$%^&*()"
password = ""

for _ in range(length):
    password += random.choice(chars)

print("Your Password:", password)
