# Edwardo Trevino 03/09/2023
# Lab 06: Software Engineering'


def encode():
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


def decode():
    pass
            

while __name__ == "__main__":
    print("1. Encode\n2. Decode\n3. Exit")
    option = int(input("Choose an option: "))
    if option == 1:
        pass_stored =input("Please enter your password to encode: ")
        encode()
        print('Your password has been encoded and stored!')
    if option == 2:
        pass
    if option == 3:
        break
