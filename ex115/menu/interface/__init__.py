def menu(msg):
    while True:
        mensagem('MENU PRINCIPAL')
        print('1 - Ver pessoas cadastradas.')
        print('2 - Cadastrar nova Pessoa.')
        print('3 - Sair do sistema')
        try:
            o = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;33mVocê deixou o programa.\033[m')
            break
        else:
            if o == 1:
                mensagem('Opção 1')
                continue
            elif o == 2:
                mensagem('Opção 2')
                continue
            elif o == 3:
                mensagem('Saindo do sistema... Até logo!')
                break
            else:
                print('\033[0;31mERRO! Digite uma opção válida.\033[m')

def mensagem(msg):
    tam = len(msg) + 20
    print('-' * tam)
    print(msg.center(tam))
    print('-' * tam)
