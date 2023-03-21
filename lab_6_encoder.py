# Edwardo Trevino 03/09/2023
# Lab 06: Software Engineering'


def encode(pass_stored):
    encoded_pass = str()
    for i in pass_stored:
        i = int(i)
        if i >= 7:
            i = i +3
            i -= 10
            encoded_pass += str(i)
        else:
            i += 3
            encoded_pass += str(i)
    return encoded_pass

def decode(pass_encoded): #Braden Lord added the decode function
    var = ''
    for i in pass_encoded:
        temp = int(i)
        temp -= 3
        if temp < 0:
            temp += 10
        var += str(temp)
    print(f'The encoded password is {pass_encoded}, and the original password is {var}.')
            

pass_encoded = ''
while __name__ == "__main__":
    print("\nMenu\n-------------")
    print("1. Encode\n2. Decode\n3. Exit")
    option = int(input("Choose an option: "))
    if option == 1:
        pass_stored = input("Please enter your password to encode: ")
        pass_encoded = encode(pass_stored)
        print('Your password has been encoded and stored!')
    if option == 2:#braden Lord added option 2 to the main function
        if pass_encoded == '':
            print('There is no password to decode, select a different option')
        else:
            decode(pass_encoded)
    if option == 3:
        break
