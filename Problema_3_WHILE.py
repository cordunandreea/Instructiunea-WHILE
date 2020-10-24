#Se citesc numere de la tastatură până la introducerea unui număr impar divizibil cu 3. 
#Să se afişeze suma tuturor numerelor pare introduse. 
 Exemplu: Date de intrare  7  4   6   2   1   9   Date de ieşire 12.
i=eval(input('introduceti un nr la alegere='))
c=0
while i%2==0 or (i%2!=0 and i%3!=0):
    if i%2==0:
        c+=i
    i=eval(input('introduceti un nr='))

print('suma nr pare:',c)