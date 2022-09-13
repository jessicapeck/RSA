letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

cipher_text = input("enter cipher text : ")
cipher_text_groups = cipher_text.split(" ")

print(" ")

d = int(input("enter decryption exponent, d : "))

print("")

n = int(input("enter public modulus, n : "))

print("")

grouped_numbers = []

for cipher_group in cipher_text_groups:

    cipher_group = int(cipher_group)
    grouped_num = (cipher_group**d) % n
    grouped_numbers.append(str(grouped_num).zfill(4))

# test
#print(grouped_numbers)
#print("")

numbers = []

for grouped_num in grouped_numbers:
    numbers.append(grouped_num[:2])
    numbers.append(grouped_num[-2:])

# test
#print(numbers)
#print("")

plain_text = ""

for num in numbers:
    num = int(num)
    letter_representation = letters[num - 1]
    plain_text += letter_representation

print(plain_text)

    

