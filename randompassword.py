import random
chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","m","o","p","r","s","t","u","v","y","z","w","q","x",
         "A","B","C","D","E","F","G","H","I","J","K","L","M","O","P","R","S","T","U","V","Y","Z","W","Q","X",
         1,2,3,4,5,6,7,8,9,0]

password = ""
try:
    password_length = int(input("Enter your password length: "))

except ValueError:
    print("\nPlease enter integer input.")
    password_length = int(input("Enter your password length: "))

while password_length <8:
    print("\nPlease enter a larger value.")
    password_length = int(input("Enter your password length: "))

while password_length >15:
    print("\nPlease enter a smaller value.")
    password_length = int(input("Enter your password length: "))



for i in range(password_length):
    password += str(random.choice(chars))

print("--------------------------------")
print("Your password: "+password)
print("--------------------------------")
