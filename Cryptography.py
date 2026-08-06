import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

running = True

while running:
    print("========================")
    print("    CRYPTOGRAPHY")
    print("========================")
    print("1. Encryption")
    print("2. Decryption")
    print("3. Exit")
    print("========================")

    choices = int(input("Enter your choice : "))

    cipher = ""
    plain = ""

    if choices == 1:
        print("===== ENCRYPTION =====")

        plain = input("Enter your message : ")

        for letter in plain:
            index = chars.index(letter)
            new_index = (index + 3) % len(chars)
            cipher += chars[new_index]

        print("======================")
        print(f"Secret text : {cipher}")
        print("======================")

    elif choices == 2:
        print("===== DECRYPTION =====")

        cipher = input("Enter your cipher text : ")

        for letter in cipher:
            index = chars.index(letter)
            new_index = (index - 3) % len(chars)
            plain += chars[new_index]

        print("\n======================")
        print(f"Original text : {plain}")
        print("======================")

    elif choices == 3:
        print("\nProgram ended. Goodbye!")
        running = False

    else:
        print("Invalid choice. Please try again.")