import random
import math

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

print("requirements for p and q : must be two different, large prime numbers")
p = int(input("enter p : "))
q = int(input("enter q : "))

print("")

# test
#print(f"p = {p}, q = {q}")
#print("")

n = p*q
euler_phi_function_of_n = (p - 1) * (q - 1)

# test
#print(f"n = {n}, eulier phi function of n = {euler_phi_function_of_n}")
#print("")

print(f"requirements for encryption component e : the GCD of e and {euler_phi_function_of_n} is 1")

possible_e = []

for count in range(euler_phi_function_of_n):
    if math.gcd(count,euler_phi_function_of_n) == 1:
        possible_e.append(count)

# display possible values of e
print(f"possible values of e include : {possible_e}")

e = int(input("enter e : "))

print("")

# test
#print(f"e = {e}")
#print("")

count = 1
while True:
    if ((euler_phi_function_of_n * count) + 1) % e == 0:
        d = ((euler_phi_function_of_n * count) + 1) // e
        break 

    count = count + 1

# test
#print(f"d = {d}")
#print("")

plain_text = input("enter cipher text : ")
plain_text = plain_text.lower().strip()

print("")

# test
#print(plain_text)
#print("")

cipher_text = ""
numbers = []
grouped_numbers = []

for char in plain_text:
    if char in letters:
        number_representation = str(letters.index(char) + 1).zfill(2)
        numbers.append(number_representation)

if len(numbers) % 2 != 0:
    padding_number = str(random.randint(0,26)).zfill(2)
    numbers.append(padding_number)

# test
#print(numbers)
#print("")

for count in range(0,len(numbers),2):
    num_1 = str(numbers[count])
    num_2 = str(numbers[count + 1])

    grouped_num = num_1 + num_2

    grouped_numbers.append(grouped_num)

# test
#print(grouped_numbers)
#print("")

for grouped_num in grouped_numbers:
    grouped_num = int(grouped_num)
    cipher_number = (grouped_num**e) % n
    cipher_number = str(cipher_number).zfill(4)
    cipher_text += cipher_number + " "

print(f"public key : e = {e}, n = {n}")
print(f"private key : d = {d}, n = {n}")

print("")

print(f"cipher text : {cipher_text}")

print("")

