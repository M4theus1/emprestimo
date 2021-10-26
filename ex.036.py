print('\033[1;94m', '*' * 50,  'Minha Casa Minha Vida', '*' * 50)
print('\033[0;0m ')
nome = str(input('Olá, poderia nos informar o seu nome? ')).strip().split()
print('\033[1;94m', '*'*50)
print('\033[0;0m ', 'Olá, ', nome[0],'!')
print('\033[1;94m', '*'*50, '\033[0;0m')
valor = float(input('Poderia nos informar o valor da casa? R$'))
salario = float(input('Poderia nos informar também o seu salário? R$'))
anos = float(input('Você gostaria de pagar esse empréstimo em quantos anos? '))
prestacao = valor / (anos * 12)

print('Para pagar uma casa de R${:.2f} em {:.1f} anos, a prestação será de R${:.2f}'.format(valor, anos, prestacao))
print(' ')

if prestacao >= (salario) * 30/100:
    print('\033[1;31m', 'Empréstimo negado! Seu salário não é compatível para essa quantia de financiamento')
else:
    print('\033[1;32m', 'Empréstimo APROVADO!!! Parabéns!')
