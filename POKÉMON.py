print('')
print('⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣠⣤⣶⣶')
print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢰⣿⣿⣿⣿')
print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣾⣿⣿⣿⣿')
print('⣿⣿⣿⣿⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿')
print('⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿')
print('⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿')
print('⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿')
print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿')
print('⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿')
print('⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿')
print('⣿⣿⣿⣿⣿⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿')
print('⣿⣿⣿⣿⣿⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿')
print('⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿')
print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿')
print('')

cond = input('Seja Bem-vindo, usuário! Posso Saber o seu nome? [s]im ou [n]ão ')


while True:

    if not cond == 's':
        print('')
        print('Sem problemas, até próxima!')
        break
    else:
        print('')
        name = input('Obrigado! Qual é o seu nome? ')
        name = name.capitalize()

    print('')

    exit_ = input('Deseja sair do programa? [s]im ou [n]ão ')
    print('')
    if exit_ == 's':
        break
    else:
        pass



    day = input(f'{name}, qual é o dia do seu aniversário? ')

    if not day.isdigit():
        print('')
        print(f'No dia do seu aniversário, coloque apenas número, {name}!')
        continue
    day = int(day)

    print('')
    month = input('E o mês? ')
    month = month.capitalize()

    if not month.isalpha():
        print('')
        print(f'Não aceitamos números no mêS, {name}')
        continue
    else:
        pass

# Dia
    if day == 1:
        type_day = 'Dark'
    elif day == 2 or day == 26:
        type_day = 'Flying'
    elif day == 3 or day == 31:
        type_day = 'Fight'
    elif day == 4 or day == 12 or day == 29:
        type_day = 'Fairy'
    elif day == 5:
        type_day = 'Fire'
    elif day == 6 or day == 17:
        type_day = 'Normal'
    elif day == 7 or day == 14 or day == 30:
        type_day = 'Rock'
    elif day == 8 or day == 11:
        type_day ='Psychc'
    elif day == 9 or day == 13:
        type_day = 'Ice'
    elif day == 10 or day == 19:
        type_day = 'Dragon'
    elif day == 15 or day == 28:
        type_day = 'Water'
    elif day == 16:
        print = 'Ghost'
    elif day == 18:
        type_day = 'Electra'
    elif  day == 20 or day == 24:
        type_day = 'Bug'
    elif day == 21 or day == 27:
        type_day = 'Poison'
    elif day == 22:
        type_day = 'Steel'
    elif day == 23:
        type_day = 'Ground'
    elif day == 25:
        type_day = 'Grass'
    else:
        print('')
        print(f'{name}, Informe um dia válido!')
        continue


# Mês
    if month == 'Janeiro':
        type_month = 'Electr'
    elif  month == 'Fevereiro':
        type_month = 'Fairy'
    elif month == 'Março':
        type_month = 'Water'
    elif  month == 'Abril':
        type_month = 'Dark'
    elif  month == 'Maio':
        type_month = 'Bug'
    elif  month == 'Junho':
        type_month = 'Ground'
    elif month == 'Julho':
        type_month = 'Poison'
    elif  month == 'Agosto':
        type_month = 'Normal'
    elif  month == 'Setembro':
        type_month = 'fire'
    elif month == 'Outubro':
        type_month = 'fight'
    elif month == 'Novembro':
        type_month = 'Ghost'
    elif month == 'Dezembro':
        type_month = 'Ice'
    else:
        print(' ')
        print(f'{name}, informe um mês válido!')
        continue

    print('')

    print(f'De acordo com o seu dia do seu aniversário, o seu tipo primário seria {type_day}. \n'
          f'Agora, de acordo com o mês do seu aniversário , o seu tipo secundário seria {type_month}. ')
    print('')
    break

