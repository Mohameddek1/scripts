import base64

x = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Convert the hexadecimal string to a bytes object
y = bytes.fromhex(x)

# Encode the bytes object to base64
z = base64.b64encode(y)

# Decode the base64 bytes to a UTF-8 string before printing
result_string = z.decode('utf-8')
print(result_string)
