print('')
print('{: ^170}'.format('███╗░░██╗░█████╗░██████╗░██╗░░░██╗████████╗░█████╗░'))
print('{: ^170}'.format('████╗░██║██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗'))
print('{: ^170}'.format('██╔██╗██║███████║██████╔╝██║░░░██║░░░██║░░░██║░░██║'))
print('{: ^170}'.format('██║╚████║██╔══██║██╔══██╗██║░░░██║░░░██║░░░██║░░██║'))
print('{: ^170}'.format('██║░╚███║██║░░██║██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝'))
print('{: ^170}'.format('╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░'))
print('')

while True:

    exit_ = input('{: ^170}'.format(
        'Deseja parar com a execução do programa? Responda com [s]im ou [n]ão '
    ))
    exit_ = exit_.lower()

    if exit_ == 's':
        print('')
        print('{: ^170}'.format('Sem problemas, até mais!'))
        break

    print('')

    name = input('{: ^170}'.format('Qual é o seu nome? '))
    name = name.capitalize()

    print('')

    month = input('{: ^170}'.format(f'{name}, você nasceu em qual mês? '))
    print('')
    month = month.capitalize()

    if not month.isalpha():
        print('{: ^170}'.format(
            f'Não trabalho com caracteres que não sejam letras!!'))
        continue
        print('')

    if month == 'Janeiro':
        print('{: ^170}'.format(
            f'De acordo com o mês do seu aniversário({month}), {name}, você seria o Hidan!!'
        ))
        break
    elif month == 'Fevereiro':
        print('{: ^170}'.format(
            f'De acordo com o mês do seu aniversário({month}), {name}, você seria o Sasuke!'
        ))
        break
    elif month == 'Março':
        print('{: ^170}'.format(
            f'De acordo com o mês do seu aniversário({month}), {name}, você seria o Naruto!!'
        ))
        break
    elif month == 'Abril':
        print('{: ^170}'.format(
            f'De acordo com o mês do seu aniversário({month}), {name}, você seria o Itachi!!'
        ))
        break
    elif month == 'Maio':
        print('{: ^170}'.format(
            f'De acordo com o mês do seu aniversário({month}), {name}, você seria o Madara!!'
        ))
        break
    elif month == 'Junho':
        print('{: ^170}'.format(
            f'De acordo com o mês do seu aniversário({month}), {name}, você seria o Obito!!'
        ))
        break
    elif month == 'Julho':
        print('{: ^170}'.format(
            f'De acordo com o mês do seu aniversário({month}), {name}, você seria o Minato!!'
        ))
        break
    elif month == 'Agosto':
        print('{: ^170}'.format(
            f'De acordo com o mês do seu aniversário({month}), {name}, você seria o jiraya!!'
        ))
        break
    elif month == 'Setembro':
        print('{: ^170}'.format(
            f'De acordo com o mês do seu aniversário({month}), {name}, você seria a Konan!!'
        ))
        break
    elif month == 'Outubro':
        print('{: ^170}'.format(
            f'De acordo com o mês do seu aniversário({month}), {name}, você seria o Kabuto!!'
        ))
        break
    elif month == 'Novembro':
        print('{: ^170}'.format(
            f'De acordo com o mês do seu aniversário({month}), {name}, você seria o Kakuzu!!'
        ))
        break
    elif month == 'Dezembro':
        print('{: ^170}'.format(
            f'De acordo com o mês do seu aniversário({month}), {name}, você seria o Hidan!!'
        ))
        break
    else:
        print('{: ^170}'.format(f'Informe um mês válido, {name}'))
        continue
