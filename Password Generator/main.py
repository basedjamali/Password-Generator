import string
import random

print("==== Password Generator ====")

letters = string.ascii_letters
digits = string.digits
characters = string.punctuation
total = letters + digits + characters

def generateRandomPassoword(): 
  password = ""
  length = int(input("Enter the length of the password: "))
  for i in range(length):
    password += "".join(random.choice(total))
  print(password)
generateRandomPassoword()
