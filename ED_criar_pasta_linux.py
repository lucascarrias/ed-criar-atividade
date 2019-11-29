import os


def main():
    clear_screen()

    welcome = "* Bem vindo, preguiçoso! *"
    bot_top = "*"*len(welcome)

    print("\n\t" + bot_top)
    print("\t" + welcome)
    print("\t" + bot_top + "\n\n")

    print("Este programa é para quem tem preguiça de\n" +
          "criar uma pasta dos exercícios do Dr. Fábio.\n" +
          "Uma pasta será criada com o seu nome e todos os arquivos .c\n" +
          "com uma estrutura básica.\n\n")
    print("Modelo de nome de pasta: RaimundoNFSilva_Ex-01")
    print("Modelo de nome de arquivo: ex-01_q-01.c\n\n")

    input("\n\tENTER PARA CONTINUAR ")

    while True:
        clear_screen()
        nome = input("\n\tQual o seu nome completo?\n> ")
        num_ex = input("\n\tQual o número do exercício?\n> ")
        qtd_quests = int(input("\n\tQual a quantidade de questões?\n> "))

        if input("\n\n\tConfirma os dados? S/n\n>").lower() in ['n', 'nao']:
            continue
        break

    clear_screen()

    folder_name = folder_creator(nome, num_ex)

    file_creator(folder_name, num_ex, qtd_quests)

    input("\n\n\tPRONTO! ENTER PARA FINALIZAR ")
    clear_screen()


def folder_creator(nome, num_ex):
    nome = nome.split()
    user_folder = ''

    for n in nome:
        if n == nome[0]:
            user_folder += n.capitalize()
        elif n == nome[-1] and n != nome[0]:
            user_folder += n.capitalize()
        elif n.lower() in ['da', 'de', 'e']:
            continue
        else:
            user_folder += n[0].capitalize()

    # if num_ex.isdigit():
    # 	if abs(int(num_ex)) < 10:
    # 		num_ex = '0' + str(abs(int(num_ex)))

    num_ex = add_zero(num_ex)

    folder_name = user_folder + "_EX-" + num_ex

    os.system('mkdir %s' % folder_name)

    return folder_name


def file_creator(folder_name, num_ex, qtd_quests):
    num_ex = add_zero(num_ex)

    for num in range(1, qtd_quests+1):
        num = add_zero(num)

        file_name = '-'.join(['ex', str(num_ex)]) + '_' + '-'.join(['q', str(num)]) + '.c'

        with open('/'.join(['.', folder_name, file_name]), 'w') as file:
            file.write(
                '#include <stdio.h>\n' +
                '#include <stdlib.h>\n\n' +
                'int main() {\n\n\n' +
                '\treturn 0;\n' +
                '}\n'
            )
            print(file_name + ' > Criado!')


def add_zero(number):
    if type(number) is str:
        if number.isdigit():
            if abs(int(number)) < 10:
                number = '0' + str(abs(int(number)))
    elif abs(int(number)) < 10:
        number = '0' + str(abs(int(number)))

    return number


def clear_screen():
    os.system('clear')


if __name__ == '__main__':
    main()
