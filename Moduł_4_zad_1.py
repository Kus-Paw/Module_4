"""
# Niestety nie portafie uzyc funkcji boolean nie wyświetlaja mi sie zadne /
# wartosci, postanowilem użyć funkcji for która idzie po kazdyn znaku zdania'word'/
# i zwrocic wartosc True lub False
"""
"""
def polidrom(word):
    for i in range (len(word)//2):
        if (word[0:]) == word[:: -1 ]:
            word[:] == word[:: -1]:
            word == word[::-1]
            return True
        else:
            return False

print(polidrom('mam'))
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
