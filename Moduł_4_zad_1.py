#Niestety nie portafie uzyc funkcji boolean nie wyświetlaja mi sie zadne /
# wartosci, postanowilem użyć funkcji for która idzie po kazdyn znaku zdania'word'/
# i zwrocic wartosc True lub False

def Polidrom2(word):
    for i in range (len(word)//2):
        if (word[0:]) == word[:: -1 ]:
            return True
        else:
            return False

print(Polidrom2('mam'))