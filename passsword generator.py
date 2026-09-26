import random

chars = "wejdfgnsdhjfgsedifhgnh343565656rgerghiergergwerg"
print("Password generator")

lenght = int(input("How long do you want your password to be ?\n: "))

password = ""

for i in range(lenght):
    password += random.choice(chars)

print(f"Your secure password is {password}")
