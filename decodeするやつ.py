import cryptocode
import pyperclip

str_decoded = cryptocode.decrypt(pyperclip.paste(), input())
print(str_decoded)
pyperclip.copy(str_decoded)