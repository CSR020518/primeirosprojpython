# Definição Triângulos

A = int(input('Digito o 1° lado do triâncgulo:'))
B = int(input('Digito o 2° lado do triâncgulo:'))
C = int(input('Digito o 3° lado do triâncgulo:'))

if (A > 0) and (B > 0) and (C > 0):
    if (A + B > C) and (A + C > B) and (B + C > A):
    # Se você chegou até aqui, é porque o triângulo é válido!
       if (A != B) and (A != C) and ( B!= C):
           print('Triângulo escaleno!')
       else:
           if (A == B) and (A == C) and ( B==C):
               print('Triângulo equilátero!') 
           else:
               print('Triângulo isósceles!')
    else:
        print('Ao menos um dos valores indicados não servem para formar um triângulo')

else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo')