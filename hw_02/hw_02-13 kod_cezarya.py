message = "Cel4lo my l!ittle friends!"
offset = 1
encoded_message = ""
print(ord("a"), ord("z"))
print(ord("A"), ord("Z"))
for ch in message:
    if ch.isalpha() and ch.isupper():
        pos = ord(ch.lower()) - 97
        pos = (pos + offset) % 26
        encoded_message += chr(pos + 97).upper()
    elif ch.isalpha() and ch.lower():
        pos = ord(ch.lower()) - 97
        pos = (pos + offset) % 26
        encoded_message += chr(pos + 97)
    else:
        encoded_message += ch
    
print(encoded_message)