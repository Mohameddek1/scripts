
import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")


# Let's assume "ords" is a list of integers representing ASCII values of characters.
ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]


result_characters = []
# Explanation of the expression:
# result_characters = [chr(o ^ 0x32) for o in ords]
for o in ords:
    # operator performs a bitwise XOR operation between the current ASCII value (o) and the hexadecimal value 0x32 (which is 50 in decimal).
    xor_result = o ^ 0x32
    # The chr function converts the result of the XOR operation (an ASCII value) into its corresponding character.
    characters = chr(xor_result)
    result_characters.append(characters)
result_string = "".join(result_characters)

# Resulting string:
print("Here is your flag:")
print(result_string)
