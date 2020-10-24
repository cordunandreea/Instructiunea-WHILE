#Se citesc pe rând temperaturile medii ale fiecărei luni a unui an, ca numere întregi. 
#Să se afişeze cu două zecimale media anuală a temperaturilor pozitive şi a celor negative. 
#Exemplu: Date de intrare  -5  -3  1  8  12  17  20  21  18  10  6  -2  Date de ieşire  medie_poz=13.66  medie_neg=-3.33.
n=0
ap=0
an=0
bp=0
bn=0
t=0
while t<12:
    n=eval(input('introduceti temp:'))
    if n<100 and n>-100:
        t+=1
        if n>0:
            ap+=n
            bp+=1
        else:
            an+=n
            bn+=1 
    else: print('temp introdusa e invalida, introduceti alta temperatura')           

if ap>0:
    print('medie_pozitiva:',round(ap/bp,2))
else:print('nu sunt temp pozitive')
if bn>0:
    print('medie negativa:',round(an/bn,2))
else:print('nu sunt temp negative')