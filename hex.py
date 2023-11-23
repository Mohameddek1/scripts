# Hexadecimal string
x = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# Convert the hexadecimal string to a bytes object
y = bytes.fromhex(x)

# Print the bytes object
print(y)
