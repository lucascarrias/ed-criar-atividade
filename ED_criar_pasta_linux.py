import os


def main():
    os.system('clear')

    welcome = "* Bem vindo, preguiçoso! *"
    bot_top = "*"*len(welcome)

    print(bot_top)
    print(welcome)
    print(bot_top + "\n\n\n")

    print("Este é programa é para quem tem preguiça de\n" +
          "criar uma pasta dos exercícios do Dr. Fábio.\n" +
          "Uma pasta será criada com o seu nome e todos os arquivos .c\n" +
          "com uma estrutura básica.\n\n")
    print("Modelo de nome de pasta: RaimundoNFSilva_Ex-01")
    print("Modelo de nome de arquivo: ex-01_q-01.c\n\n")

    input("ENTER PARA CONTINUAR")

    while True:
        os.system('clear')
        nome = input("Qual o seu nome completo: > ")
        num_ex = input("Qual o número do exercício: > ")
        qtd_quests = int(input("Qual a quantidade de questões: > "))

        if input("\n\nConfirma os valores acima? S/N >").lower() in ['sim', 's']:
            break

    os.system('clear')

    folder_creator(nome, num_ex)

    file_creator(folder_name, num_ex, qtd_quests)

    input("PRONTO! ENTER PARA FINALIZAR")
    os.system('clear')


def folder_creator(nome, num_ex):
    global folder_name

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


def file_creator(folder_name, num_ex, qtd_quests):
    num_ex = add_zero(num_ex)

    for num in range(1, qtd_quests+1):
        num = add_zero(num)

        file_name = '-'.join(['ex', str(num_ex)]) + '_' + '-'.join(['q', str(num)]) + '.c'

        with open('/'.join(['.', folder_name, file_name]), 'w') as file:
            file.write("#include <stdio.h>\n\nvoid main(){\n\n\n\n}\n")
            print(file_name + ' > Criado!')


def add_zero(number):
    if type(number) is str:
        if number.isdigit():
            if abs(int(number)) < 10:
                number = '0' + str(abs(int(number)))
    elif abs(int(number)) < 10:
        number = '0' + str(abs(int(number)))

    return number


main()
