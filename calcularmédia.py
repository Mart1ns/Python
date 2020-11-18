print('')
print(100 * '★★')
print('')

print('-Olá, vamos calcular a sua média? ')
nome = input('-Me informe o seu nome: ')

print('')
print(100 * '★★')
print('')

print(f'-Olá, {nome}! (>‿◠)✌')

print('')
print(100 * '★★')
print('')

print('-A Seguir, me informe suas notas: ✍(◔◡◔)')
print('')
n1 = float(input(' --Primeira nota:'))
n2 = float(input(' --Segunda nota:'))
n3 = float(input(' --Terceira nota:'))
n4 = float(input(' --Quarta nota:'))
n = (n1 + n2 + n3 + n4) / 4 # ---> Operação utlizada para calculara média. <---

print('')

if n >= 5:
    print(100 * '✅__')
    print('')

    print(f'-Parabéns, {nome}, a sua média é: {n}, e é uma nota azul! (っ◔◡◔)っ ❤')

    print('')
    print(100 * '✅__')

else:
    print(100 * '✘__')
    print('')

    print(f'-Poxa, a sua média é: {n}, e é uma nota vermelha. ಥ_ಥ ')

    print('')
    print(100 * '✘__')
