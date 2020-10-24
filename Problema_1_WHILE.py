#Se introduc succesiv numere nenule până la introducerea numărului 0. Să se afişeze suma tuturor numerelor introduse. 
#Exemplu: Date de intrare   3  5  4  2  0  Date de ieşire 14.
i=1
suma=0
while i!=0:
    i=1
    i=eval(input('Introduceti un numar nenul:'))
    suma+=i
print(suma)