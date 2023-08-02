a = int(input('Valor de A:'))
b = int(input('Valor de B:'))
c = int(input('Valor de C:'))

delta = b**2 - 4*a*c




x1 = (-b - delta**0.5)/(2*a)
x2 = (-b + delta**0.5)/(2*a)



if delta==0:
        print('X1 = X2',  x1)
    
elif delta>0:
        print('X1: ', x1)
        print('X2: ', x2)
        print('delta: ', delta)
else:
            print('Raiz nao existe!')
        
