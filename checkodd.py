xstat = x%2
ystat = y%2
zstat = z%2
if zstat > ystat and zstat > xstat: 
    print ('z ', 'é o maior número ímpar')
elif zstat > ystat and zstat == xstat:
    if z > x:
        print ('z ', 'é o maior número ímpar')
    else:
        print ('x ', 'é o maior número í)
elif ystat > zstat
else:
    print ('nenhum número é ímpar')




#opção 2:

#declarar variáveis

x = input('Primeiro número: ')
y = input('Segundo número: ')
z = input('Terceiro número: ')

#avaliar par ou ímpar

if x%2 == 0:
    xstat = par
else:
    xstat = ímpar
if y%2 == 0:
    ystat = par
else:
    ystat = ímpar
if x%2 == 0:
    zstat = par
else:
    zstat = ímpar

#avaliar maior e retornar resultado

if x > y and x > z and xstat = ímpar:
    print (x, 'é o maior número ímpar')
elif x > y and z > x and zstat = ímpar:
    print (z, 'é o maior número ímpar')
elif ystat = ímpar:
    print (y, 'é o maior número ímpar')
else:
    print ('nenhum número é ímpar')



#opção 3 

if x%2 != 0 and x > y:
    if x > z:
        print (x, 'é o maior número ímpar')
    elif z%2 != 0:
        print (z, 'é o maior número ímpar')
elif y%2 != 0 and y > z:
    print (y, 'é o maior número ímpar')
elif z%2 != 0
        print (z, 'é o maior número ímpar')
else:
    print ('nenhum número é ímpar')