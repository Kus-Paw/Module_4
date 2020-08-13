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
def polidrom_2(word):
    
    word = word.lower()
    word = word.replace( ' ', '')
    word = word.replace(',', '')
    word = word.replace('.', '')
   
    for i in range (len(word)):
        (word.isalnum()) == True
        if word[:] == word[:: -1] and (word[:]) == word[:: -1]:
            return True
        else:
            return False
    
print(polidrom_2('Atokiwizdziwi kota'))
print(polidrom_2("A to Kamela, ale ma kota."))
print(polidrom_2("alpaka1"))
print(polidrom_2("mam!"))
