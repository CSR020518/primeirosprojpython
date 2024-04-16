# Validação Nome e Idade

nome = input('qual seu nome?')
idade = int(input('qual a sua idade'))
if nome == 'Chester':
  print('Olá Chester!')
elif idade < 18:
  print('Você não é o Chester! E é menor de idade!')
elif idade > 100:
  print('Diferente de você, o Chester não é imortal!')
    
      