# Caesar Cipher: ENCRYPTING A MESSAGE
==========================================================================================================================================================================
==========================================================================================================================================================================

text = input('Enter your message:')
chiper = ''
for char in text:
    '''The isalpha() method returns True if all the characters are alphabet letters (a-z).
    Example of characters that are not alphabet letters: (space)!'''
    if not char.isalpha():
        continue
    char = char.upper()
    #The ord() function returns the number representing the unicode code of a specified character.
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    chiper += chr(code)
print(chiper)

==========================================================================================================================================================================
==========================================================================================================================================================================
# Caesar Cipher: DECRYPTING A MESSAGE
chiper = input('Enter your cryptogram:')
text = ''
for char in chiper:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)
print(text)
