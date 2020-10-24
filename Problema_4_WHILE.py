#Elaborați un program care va calcula suma, 
#produsul și media aritmetică a numerelor de la 1 la n, pentru n introdus de la tastatură.
i=eval(input('introduceti un nr:'))
a=0
b=0
c=1
while a<i:
    a+=1
    b+=a
    c*=a
print('suma:',b)
print('produsul:', c)
print('media aritmetica:', b/a)