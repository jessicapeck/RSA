import math
import random
import os

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def encrypt(letters):
    os.system("cls")

    print("requirements for p and q : must be two different prime numbers")
    p = int(input("enter p : "))
    q = int(input("enter q : "))
    print("")

    # TEST
    #print(f"p = {p}, q = {q}")
    #print("")

    n = p*q
    euler_phi_function_of_n = (p - 1) * (q - 1)

    # TEST
    #print(f"n = {n}, eulier phi function of n = {euler_phi_function_of_n}")
    #print("")

    print(f"requirements for encryption component e : the GCD of e and {euler_phi_function_of_n} is 1")
    print("some possible values of e include : ")
    print("")

    # calculate up to 100 possible values of e
    possible_e = []

    item_count = 0
    count = 0

    while item_count <= 100 and count <= euler_phi_function_of_n:
        if math.gcd(count ,euler_phi_function_of_n) == 1:
            possible_e.append(count)
            item_count += 1

        count += 1

    # display possible values of e to user
    max_num = max(possible_e)
    max_num_length = len(str(max_num))

    num_rows = len(possible_e) // 10
    filler = " "
    item_num = 0

    for row in range(num_rows):
        row = ""
        for count in range(10):
            filler_space = filler * (max_num_length - len(str(possible_e[item_num + count])))

            row = row + f" | {possible_e[item_num + count]}{filler_space} | "

        row_length = len(row)

        print("-" * row_length)
        print(row)   

        item_num += 10

    print("-" * row_length)

    print("")

    # get input of e
    e = int(input("enter e : "))

    print("")

    # TEST
    #print(f"e = {e}")
    #print("")

    # calculate d
    count = 1
    while True:
        if ((euler_phi_function_of_n * count) + 1) % e == 0:
            d = ((euler_phi_function_of_n * count) + 1) // e
            break 

        count = count + 1

    # TEST
    #print(f"d = {d}")
    #print("")

    # get input of plain text
    plain_text = input("enter plain text : ")
    plain_text = plain_text.lower().strip()

    print("")

    # encrypt
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

    # TEST
    #print(f"numbers = {numbers}")
    #print("")

    for count in range(0,len(numbers),2):
        num_1 = str(numbers[count])
        num_2 = str(numbers[count + 1])

        grouped_num = num_1 + num_2

        grouped_numbers.append(grouped_num)

    # TEST
    #print(f"grouped_numbers = {grouped_numbers}")
    #print("")

    for grouped_num in grouped_numbers:
        grouped_num = int(grouped_num)
        cipher_number = (grouped_num**e) % n
        cipher_number = str(cipher_number).zfill(4)
        cipher_text += cipher_number + " "

    # display public key and private key information
    print(f"public key : e = {e}, n = {n}")
    print(f"private key : d = {d}, n = {n}")

    print("")

    # display cipher text
    print(f"cipher text : {cipher_text}")

    print("")

    return

def decrypt(letters):
    os.system("cls")

    # get input of cipher text
    cipher_text = input("enter cipher text : ")
    cipher_text_groups = cipher_text.split(" ")

    print(" ")

    # get input of d
    d = int(input("enter decryption exponent, d : "))

    print("")

    # get input of n
    n = int(input("enter public modulus, n : "))

    print("")

   # decrypt
    grouped_numbers = []

    for cipher_group in cipher_text_groups:

        cipher_group = int(cipher_group)
        grouped_num = (cipher_group**d) % n
        grouped_numbers.append(str(grouped_num).zfill(4))

    # TEST
    #print(f"grouped_numbers = {grouped_numbers}")
    #print("")

    numbers = []

    for grouped_num in grouped_numbers:
        numbers.append(grouped_num[:2])
        numbers.append(grouped_num[-2:])

    # TEST
    #print(f"numbers = {numbers}")
    #print("")

    plain_text = ""

    for num in numbers:
        num = int(num)
        letter_representation = letters[num - 1]
        plain_text += letter_representation

    # display plain text
    print(plain_text)

    print(" ")

    return

def main():
    while True:
        # display menu option
        print("")
        print("-"*31)
        print("| 1. encrypt using RSA        |")
        print("| 2. decrypt RSA cipher text  |")
        print("| 3. exit")
        print("-"*31)
        print("")

        option_choices = ["1","2","3"]

        while True:
            option = input("please enter number to choose option : ")
            option = option.lower().strip()

            # validate option choice
            if option not in option_choices:
                print("*** invalid option choice ***")
                print("")
            else:
                break

        # call encrypt or decrypt function
        if option == "1":
            encrypt(letters)
        elif option == "2":
            decrypt(letters)
        elif option == "3":
            break

main()

os.system("cls")

print("thank you, goodbye!")
print("")