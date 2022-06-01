#!/usr/bin/env python3

from itertools import product

chars  = [chr(i) for i in range(97, 123)]
chars += [chr(i) for i in range(65, 91)]
chars += [chr(i) for i in range(48, 58)]



# Ou descomente a linha abaixo para incluir todos os caracteres geralmente usados em um password
#chars  = [chr(i) for i in range(32, 127)]

#password = 'gato'
print("\n")


print("     |  | _ _____ ________  ")
print("     |  |/ //     \\___   / ")
print("     |    <|  Y Y  \/    /  ")
print("     |__|_ \__|_|  /_____ \ ")
print("         \/     \/      \/  ")
"""
print('')
print('{: ^100}'.format('██╗░░██╗░█████╗░███╗░░░███╗██╗██╗░░██╗░█████╗░███████╗███████╗'))
print('{: ^100}'.format('██║░██╔╝██╔══██╗████╗░████║██║██║░██╔╝██╔══██╗╚════██║██╔════╝'))
print('{: ^100}'.format('█████═╝░███████║██╔████╔██║██║█████═╝░███████║░░███╔═╝█████╗░░'))
print('{: ^100}'.format('██╔═██╗░██╔══██║██║╚██╔╝██║██║██╔═██╗░██╔══██║██╔══╝░░██╔══╝░░'))
print('{: ^100}'.format('██║░╚██╗██║░░██║██║░╚═╝░██║██║██║░╚██╗██║░░██║███████╗███████╗'))
print('{: ^100}'.format('╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝'))
print('')
"""
print("\n")
user = input(print("    --> Qual o seu nome?"))
user = user.capitalize()
password = input(print(f"--> {user}, informe uma senha para o programa tentar descobrir:\n--> "))
print("\n")
print(f"    --> Senha digitada por você {password}.")
tentativa = 0

def bruteForce_1(chars, password, lenPass):
    tentativa = 0

    for i in product(chars, repeat=lenPass):
        combina = ''.join(i)
        tentativa += 1
    
        if (tentativa % 500000 == 0):
            print('%10i --> %s' % (tentativa, combina))

        if password == combina:
            print("\n")
            return('Senha encontrada é "{}", após {} tentativas.'.format(combina, tentativa))
    print("\n")
    return ('   --> Senha não encontrada <--')

def bruteForce_2(chars, password, lenPass, comb_anterior = ''):
    global tentativa

    for LETRA in chars:
        combina = comb_anterior + LETRA
        tentativa += 1
        if (tentativa % 500000 == 0):
            print('%10i --> %s' % (tentativa, combina))

        if password == combina:
            print(' *************************************************')
            print(' -> Senha encontrada é "{}", após {} tentativas. *'.format(combina, tentativa))
            print(' *************************************************')
            #return 'ok'
            exit()

        elif (lenPass != 1):
            # E aqui a chamada da recursividade
            bruteForce_2(chars, password, lenPass-1, combina)

print(bruteForce_1(chars, password, lenPass=4))
print('*' * 60 + '\n')

print(bruteForce_2(chars, password, len(password)))
print('*' * 60 + '\n')

print(bruteForce_2(chars, 'cabo', 4))
print('*' * 60 + '\n')

print(bruteForce_2(chars, 'cabo', 5))

# Fim
