from pwn import xor


# solution 1

# def xor_string(label):
#     result = ""
#     for char in label:
#         # Convert each character to its Unicode integer representation
#         char_code = ord(char)
#         # XOR with 13
#         xor_result = char_code ^ 13
#         # Convert the result back to a character and append to the final string
#         result += chr(xor_result)
#     return result

# # Example usage
# label = "label"
# flag = xor_string(label)
# print(flag)


# solution 2


# label = b"label"
# flag = xor(label, 13)
# print(f"crypto{{{flag}}}")


# solution 3

def xor_string(key, x):
    result = ""
    for char in key:
        # Convert each character to its Unicode integer representation
        char_code = ord(char)
        # XOR with the key
        xor_result = xor(key, char_code)
        # Convert the result back to a character and append to the final string
        result += chr(xor_result)
    return result

print(xor_string(b"label", 13))