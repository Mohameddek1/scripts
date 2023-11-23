import string

def poly(plain: str, key: int) -> str:
    # Convert the plaintext to lowercase
    plain = plain.lower()
    #  and initialize an empty dictionary for character substitution
    charset = {}

    # Get the lowercase letters of the alphabet
    letters = string.ascii_lowercase

    # Create a substitution dictionary based on the key
    for i in range(len(letters)):
        charset.update({letters[i - key]: letters[i]})
    
    # Define a function for encryption and decryption using the substitution dictionary
    def encdec(plain: str, charset: dict) -> str:
        result = ''

        # Iterate through each character in the plaintext
        for char in plain:
            try:
                # Substitute the character using the charset dictionary
                result += charset[char]
            except KeyError:
                # If the character is not in the dictionary, keep it unchanged
                result += char

        return result

    # Call the encryption/decryption function and convert the result to uppercase
    return encdec(plain, charset).upper()

# Iterate through possible keys and print the decrypted messages
for i in range(26):
    decrypted_message = poly("JSWTQQ XHWFU UTJY FGXZWI", i)
    print(f"{decrypted_message}, key: {i+1}")
