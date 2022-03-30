'''
Uma receita para produzir um bolo conta com 2 xicaras de farinha de trigo, 3 ovos e 5 colheres de
leite (estes dados são constantes nesta receita). Você deve escrever um programa em Python que
dados como entrada A (quantidade de xicaras de farinha de trigo), B (quantidade de ovos) e C
(quantidade de colheres de leite) todos valores inteiros, o programa deve mostrar quantos bolos
podem ser produzidos.
Veja a simulação:
Ex.1 A = 4 B = 6 e C = 10 ➔ produzirá a saída: 2 bolos.
Ex.2 A = 4 B = 6 e C = 9 ➔ produzirá a saída: 1 bolo.
Ex.3 A = 10 B = 10 e C = 25 ➔ produzirá a saída: 3 bolos.
'''
print('Informe a quantidade que possui de cada ingrediente')
farinha = int(input('Xícaras de farinha >> '))
ovos = int(input('Ovos >> '))
leite = int(input('Colheres de leite >> '))
A = farinha // 2
B = ovos // 3
C = leite // 5
if A < B and A < C:
    print(f'{A} bolos')
elif B < C:
    print(f'{B} bolos')
else:
    print(f'{C} bolos')