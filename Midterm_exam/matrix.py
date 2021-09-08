'''
Þetta dæmi verður leyst með tveimur hreiðruðum for lykkjum. 

Sú fyrri telur frá 0 til size_of_matrix**2 með size_of_matrix sem þrep. 
Ástæðan fyrir þessum stillingum er að á milli hverjar línu er 
size_of_matrix stökk. Svo þannig getum við einfaldlega og læsilega
prentað út fylkið.

Sú seinni mun einfaldlega telja frá 0 til size_of_matrix og prentar
út gildið úr fyrri for lykkjunni lagt saman við gildið úr seinni for
lykkjunni plús einn.
'''

size_of_matrix = int(input("Input matrix size: "))

for x in range(0, size_of_matrix**2, size_of_matrix):
    for i in range(size_of_matrix):
        print(x+i+1, end=" ")
    print()