num= int(input("digite o numero"))
print(f'fatorial de {num}')
         
fatorial=1
for i in range(num,1,-1):
    fatorial = fatorial * i
    print(fatorial)
