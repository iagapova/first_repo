import base64
code = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

encoding_bites = bytes.fromhex(code)
print(encoding_bites)

decoding_base64 = base64.b64encode(encoding_bites)
print(decoding_base64)

byte_string = b'r\xbc\xa9\xb6\x8f\xc1j\xc7\xbe\xeb\x8f\x84\x9d\xca\x1d\x8ax>\x8a\xcf\x96y\xbf\x92i\xf7\xbf'
ascii_string = byte_string.decode('utf-8')

print(ascii_string)
