a='abcdefghijklmnopqrstuvwxyz'

#word='gvlqef'
def encrypt(word,shift):
 encrypt=''
 for letter in word:
   position=a.index(letter)
   encrypt += a[position+shift]
 return encrypt
print(encrypt(word,3))