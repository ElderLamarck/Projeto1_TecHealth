def tradutor():
        phrase_str_old = input().lower().strip()
        phrase_list = phrase_str_old.split(' ')
        index = 0

        for words in phrase_list:
            if words == 'edema':
                phrase_list.pop(index)
                phrase_list.insert(index, 'retenção ou acúmulo de líquidos no tecido celular')
            elif words == 'mastalgia':
                phrase_list.pop(index)
                phrase_list.insert(index, 'dor no seio')

            index += 1

        phrase_str_new = ' '.join(phrase_list)
        print()
        print(phrase_str_new)

        key = input('\ndeseja ler a frase sem alteração? ').lower()

        if key == 'sim':
            print()
            print(phrase_str_old)
def main():
    pessoas = dict()

    ocupacao = int(input('digite \n 1- profissional \n 2- familiar\n'))

    while ocupacao < 1 or ocupacao > 2:
        print('valor não aceito')
        ocupacao = input('digite \n 1- profissional \n 2- familiar\n')


    if ocupacao == 1:
        print("Para fazer o login - Digite 1 \nPara criar uma conta - Digite 2")
        login = str(input())
        if login == "1":
            print("parabéns vc está dentro")
        if login == "2":
            print("criando conta...")

        while True:
            print("\nEscolha uma opção")
            print("1: Listar os pacientes")
            print("2: Cadastrar um paciente")
            print("3: Consultar os detalhes de um paciente")
            print("4: Editar os dados de um paciente")
            print("5: Remover um paciente")
            print("-1: Encerrar o programa")
            option = int(input("Opção: "))

            # Listas pessoas
            if option == 1:
                print()
                for pessoa in pessoas.values():
                    print(pessoa['nome'])
                print()

            # Cadastrar uma pessoa
            elif option == 2:
                nome = input("\nNome: ").title()
                idade = int(input("Idade: "))
                altura = float(input("Altura (m): "))
                peso = float(input("Peso (kg): "))
                tipo_sanguineo = input("Tipo sanguíneo: ").upper()
                alergia = input("Alergia: ").capitalize()
                doencas_base = input("Doenças base: ").capitalize()
                historico_cirurgia = input("Historico de cirurgias: ").capitalize()
                outras_doencas = input("Outras doenças: ").capitalize()
                rg = int(input('RG: '))
                telefone = int(input('Telefone: '))
                setor = input('Setor: ').capitalize()
                sus = input('SUS: ')


                pessoa = {'nome': nome, 'idade': idade, 'altura': altura, 'peso': peso,
                        'tipo sanguíneo': tipo_sanguineo, 'alergia': alergia, 'doenças base': doencas_base,
                        'historico de cirurgias': historico_cirurgia, 'outras doenças': outras_doencas,'RG': rg,
                        'telefone': telefone, 'setor': setor, 'SUS': sus}
                pessoas[nome] = pessoa

            # Consultar detalhes
            elif option == 3:
                nome = input("\nInforme o nome: ").title()

                pessoa = pessoas.get(nome, None)
                if pessoa is not None:
                    print("Nome:", pessoa['nome'])
                    print("Idade:", pessoa['idade'])
                    print("Altura:", pessoa['altura'])
                    print("Peso:", pessoa['peso'])
                    print("Tipo sanguíneo:", pessoa['tipo sanguíneo'])
                    print("Alergia:", pessoa['alergia'])
                    print("Doenças base:", pessoa['doenças base'])
                    print("Historico de cirurgias:", pessoa['historico de cirurgias'])
                    print("Outras doenças:", pessoa['outras doenças'])
                    print("RG: ", pessoa['RG'])
                    print("Telefone: ", pessoa['Telefone'])
                    print("Setor: ", pessoa['Setor'])
                    print("SUS: ", pessoa['SUS'])
                else:
                    print("Pessoa não encontrada")

                print()

            # Editar dados
            elif option == 4:
                nome = input("\nInforme o nome: ").title()

                novo_nome = input("Novo nome: ").title()
                nova_idade = int(input("Nova idade: "))
                nova_altura = float(input("Nova altura: "))
                novo_peso = float(input("Novo peso: "))
                novo_tipo_sanguineo = input("Novo tipo sanguíneo: ").upper()
                nova_alergia = input("Nova alergia: ").capitalize()
                nova_doenca_base = input("Nova doença base: ").capitalize()
                novo_historico_cirurgia = input("Novo historico de cirurgia: ").capitalize()
                nova_outras_doencas = input("Novas outras doenças: ").capitalize()
                novo_rg = input('Novo RG: ').capitalize()
                novo_telefone = input('Novo Telefone: ')
                novo_setor = input('Novo Setor: ').capitalize()
                novo_sus = input('Novo SUS: ')

                pessoa = pessoas.pop(nome, None)
                if pessoa is not None:
                    pessoa['nome'] = novo_nome
                    pessoa['idade'] = nova_idade
                    pessoa['altura'] = nova_altura
                    pessoa['peso'] = novo_peso
                    pessoa['tipo sanguíneo'] = novo_tipo_sanguineo
                    pessoa['alergia'] = nova_alergia
                    pessoa['doenças base'] = nova_doenca_base
                    pessoa['historico de cirurgias'] = novo_historico_cirurgia
                    pessoa['outras doenças'] = nova_outras_doencas
                    pessoa['RG'] = novo_rg
                    pessoa['telefone'] = novo_telefone
                    pessoa['setor'] = novo_setor
                    pessoa['SUS'] = novo_sus
                    pessoas[novo_nome] = pessoa
                else:
                    print("Pessoa não encontrada")

                print()

            # Remover
            elif option == 5:
                nome = input("\nInforme o nome: ").title()

                pessoa = pessoas.pop(nome, None)
                if pessoa is not None:
                    print("Pessoa removida com sucesso")
                else:
                    print("Pessoa não encontrada")

                print()

            elif option == -1:
                break

    elif ocupacao == 2:
        login = str(input("Para fazer o login - Digite 1 \nPara criar uma conta - Digite 2"))

        if login == "1":
            print("parabéns vc está dentro")
        if login == "2":
            print("criando conta...")

        print("escolha o que pretende fazer: ")
        escolha = str(input("1- tradutor"))

        if escolha == "1":
            tradutor()

if __name__ == "__main__":
    main()