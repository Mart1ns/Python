from random import randint

def aleatorio():
    x = randint(1, 10)
    return x


while True:

    print('')
    decisao = input('Deseja continuar a execução do programa? [s]im ou [n]ão  ' )
    if not decisao == 's':
        break
    else:
        pass

    name = input('Qual é o seu nome? ')
    name = name.capitalize()
    adivinhar = input(f'{name}, pensei em um número entre 1 e 10. Tente adivinhar! -->')

    if not adivinhar.isdigit():
        print(f'{name}, digite apenas números!')
        continue


    if adivinhar == aleatorio():
        print(f'Boa, {name}! Você acertou!! ')


