print('')
print('{: ^100}'.format('██╗░░██╗░█████╗░███╗░░░███╗██╗██╗░░██╗░█████╗░███████╗███████╗'))
print('{: ^100}'.format('██║░██╔╝██╔══██╗████╗░████║██║██║░██╔╝██╔══██╗╚════██║██╔════╝'))
print('{: ^100}'.format('█████═╝░███████║██╔████╔██║██║█████═╝░███████║░░███╔═╝█████╗░░'))
print('{: ^100}'.format('██╔═██╗░██╔══██║██║╚██╔╝██║██║██╔═██╗░██╔══██║██╔══╝░░██╔══╝░░'))
print('{: ^100}'.format('██║░╚██╗██║░░██║██║░╚═╝░██║██║██║░╚██╗██║░░██║███████╗███████╗'))
print('{: ^100}'.format('╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝'))
print('')

def aleatorio():
    from random import randint
    x = randint(1, 6)
    return x


dado = aleatorio()
print('{: ^100}'.format(f'O número aleatório --> {dado}'))