# Sistema de informação do Triangulo

print(' \n\t\t\t -- Informação do triangulo -- \n')

# Entrada

D = int(input(' Informe o lado D de um triangulo: '))
E = int(input(' Informe o lado E de um triangulo: '))
F = int(input(' Informe o lado F de um triangulo: '))

# Prossesamento

if (D < (E+F) )  and   (E < (D+F) ) and  (F < (D+E) ):

    print(f'{D}, {E} e {F} formam um triangulo')

    if(D == E ) and  (E == F ):
        print('Triangulo Equilatero')
    elif (D == E) or (E == F) or (D == F):
        print('Triangulo isoceles ')
    else:
        print('Triangulo Escaleno, Triangulo isoceles e Triangulo escaleno ')

else:
    print(f'{D}, {E} e {F} Nao Formam triangulo ')