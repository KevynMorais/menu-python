def linha(tam=42):
    return '-'*tam


def cabeçalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())


def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except KeyboardInterrupt:
            print('\n\033[0;33mO usuário preferiu não informar o número inteiro.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return valor


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[33mSua opção: \033[m')
    return opc
