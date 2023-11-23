# Integer value
x = 13

# String key
key = "label"

# Convert the key to bytes
key_bytes = key.encode('utf-8')

# Perform XOR operation
result = x ^ int.from_bytes(key_bytes, 'big')

# Print the result
print("Result of XOR operation:", result)
