# Escolha de Produtos

print('escolha o que deseja comprar:')
print('1 - maça')
print('2 - laranja')
print('3 - banana')
produto = int(input('qual a sua escolha?'))
qtd = int(input('Quantas unidades?'))
if (produto == 1):
  pagar = qtd * 2.3
  print('você comprou {} maças. total a pagar: {}'.format (qtd,pagar))
else:
  if (produto == 2):
    pagar = qtd * 3.6
    print('você comprou {} laranjas. total a pagar: {}'.format (qtd,pagar))
  else:
    if (produto == 3):
      pagar = qtd * 1.85
      print('você comprou {} bananas. total a pagar: {}'.format (qtd,pagar))
    else:
     print('produto inexistente')
