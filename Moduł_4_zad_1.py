"""
# zmniejszenie wszystkich liter i usunięcie spacji, dodatkowko zamiana ',' i '.' na ''.

def polidrom(word):
    word = word.lower()
    word = word.replace( ' ', '')
    word = word.replace(',', '')
    word = word.replace('.', '')

    for i in range (len(word)//2):
        if (word[0:]) == word[:: -1 ] and (word[:]) == word[:: -1]:
            return True
        else:
            return False

print(polidrom('Atokiwizdziwi kota'))
print(polidrom("A to Kamela, ale ma kota."))
"""
def palindrom(word):
    word = word.lower()
    letters = []
    for sign in word:
        if sign.isalnum():
            letters.append(sign)
    return letters == letters[::-1]

print(palindrom('Atokiwizdziwi kota'))
print(palindrom("A to Kamela, ale ma kota."))
print(palindrom("alpaka1"))
print(palindrom("mam!"))
