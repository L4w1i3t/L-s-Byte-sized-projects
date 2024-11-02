def caesar_cipher(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            # Determine the starting ASCII code based on uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around the alphabet using modulo operation
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_message += encrypted_char
        else:
            # Non-alphabetical characters remain unchanged
            encrypted_message += char
    return encrypted_message

# Get user input for the message and shift number
message = input("Enter the message to encrypt: ")
while True:
    try:
        shift = int(input("Enter the shift number (1-25): "))
        if 1 <= shift <= 25:
            break
        else:
            print("Please enter a number between 1 and 25.")
    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 25.")

# Encrypt the message and display the result
encrypted = caesar_cipher(message, shift)
print(f"Encrypted message: {encrypted}")
