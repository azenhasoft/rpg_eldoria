import time

def pausar(texto):
    print(texto)
    time.sleep(2)

def introducao():
    pausar("Bem-vindo a 'A Sombra do Dragão', um RPG de fantasia medieval!")
    pausar("Você é um aventureiro em um reino ameaçado por Valthor, um dragão ancestral.")
    pausar("Sua missão é salvar a vila de Eldoria do terror de Valthor.")

def exibir_menu_classe():
    pausar("\nEscolha sua classe:")
    pausar("1. Guerreiro - Mestre em combate corpo a corpo, com Força Bruta.")
    pausar("2. Mago - Conjurador de feitiços poderosos, com Magia Arcana.")
    pausar("3. Bardo - Encantador com palavras e música, com Charme Melódico.")
    pausar("4. Ladino - Especialista em furtividade e truques, com Furtividade.")

def escolher_classe():
    while True:
        exibir_menu_classe()
        escolha = input("Digite o número da sua classe (1-4): ")
        classes = {
            "1": "guerreiro",
            "2": "mago",
            "3": "bardo",
            "4": "ladino"
        }
        if escolha in classes:
            classe = classes[escolha]
            pausar(f"Você escolheu ser um {classe.capitalize()}!")
            return classe
        else:
            print("Escolha inválida! Digite um número de 1 a 4.")

def habilidade_classe(classe):
    habilidades = {
        "guerreiro": "Força Bruta",
        "mago": "Magia Arcana",
        "bardo": "Charme Melódico",
        "ladino": "Furtividade"
    }
    return habilidades[classe]

def jogo():
    introducao()
    classe = escolher_classe()
    habilidade = habilidade_classe(classe)
    
    pausar("\nVocê chega à vila de Eldoria, onde o dragão Valthor aterroriza os moradores.")
    pausar("O líder da vila implora sua ajuda para derrotar a besta.")
    pausar("Você descobre cinco caminhos para enfrentar a ameaça:")

    while True:
        pausar("\n1. Entrar na caverna de Valthor e enfrentá-lo diretamente.")
        pausar("2. Buscar a Lança do Destino em um templo antigo.")
        pausar("3. Negociar com Valthor, tentando evitar o confronto.")
        pausar("4. Recrutar aliados na cidade vizinha de Thornvale.")
        pausar("5. Explorar a Floresta Sombria em busca de um artefato lendário.")
        escolha = input("Qual caminho você escolhe? (1-5): ")

        if escolha == "1":
            caminho_caverna(classe, habilidade)
            break
        elif escolha == "2":
            caminho_templo(classe, habilidade)
            break
        elif escolha == "3":
            caminho_negociacao(classe, habilidade)
            break
        elif escolha == "4":
            caminho_aliados(classe, habilidade)
            break
        elif escolha == "5":
            caminho_floresta(classe, habilidade)
            break
        else:
            print("Escolha inválida! Digite 1, 2, 3, 4 ou 5.")

def caminho_caverna(classe, habilidade):
    pausar("\nVocê entra na caverna escura de Valthor, ouvindo seu rugido ecoar.")
    pausar(f"Você confia em sua {habilidade} para enfrentar o dragão.")
    pausar("Valthor desperta e avança! Você deve decidir rapidamente:")
    pausar("1. Atacar com tudo o que tem.")
    pausar("2. Tentar se esconder e atacar pelas costas.")

    while True:
        escolha = input("O que você faz? (1, 2): ")
        if escolha == "1":
            if classe == "guerreiro":
                pausar("Com sua força, você enfrenta Valthor em um combate feroz!")
                pausar("Após uma batalha épica, você corta a cabeça do dragão.")
                final_bom()
            else:
                pausar("Você tenta enfrentar Valthor, mas ele é forte demais!")
                pausar("O dragão o incinera com seu sopro flamejante.")
                final_ruim()
            break
        elif escolha == "2":
            if classe == "ladino":
                pausar("Você se esgueira e acerta um golpe crítico nas costas de Valthor!")
                pausar("O dragão cai, e você se torna um herói.")
                final_bom()
            else:
                pausar("Você tenta se esconder, mas Valthor o encontra facilmente.")
                pausar("Ele o esmaga com sua cauda.")
                final_ruim()
            break
        else:
            print("Escolha inválida! Digite 1 ou 2.")

def caminho_templo(classe, habilidade):
    pausar("\nVocê viaja até o templo em ruínas, enfrentando armadilhas mortais.")
    pausar(f"Usando sua {habilidade}, você chega à câmara da Lança do Destino.")
    pausar("Ao pegar a lança, você sente seu poder. Mas o templo começa a desmoronar!")
    pausar("Você deve decidir rapidamente:")
    pausar("1. Correr para fora do templo com a lança.")
    pausar("2. Explorar a câmara em busca de mais tesouros.")
    pausar("3. Usar sua habilidade para estabilizar o templo.")

    while True:
        escolha = input("O que você faz? (1, 2, 3): ")
        if escolha == "1":
            pausar("Você escapa do templo e usa a lança para matar Valthor!")
            final_bom()
            break
        elif escolha == "2":
            pausar("Você encontra ouro, mas o templo desaba, soterrando você.")
            final_ruim()
            break
        elif escolha == "3":
            if classe == "mago":
                pausar("Você conjura um feitiço para estabilizar o templo.")
                pausar("Com a lança e tesouros adicionais, você derrota Valthor.")
                final_bom()
            else:
                pausar("Sua tentativa falha, e o templo desmorona sobre você.")
                final_ruim()
            break
        else:
            print("Escolha inválida! Digite 1, 2 ou 3.")

def caminho_negociacao(classe, habilidade):
    pausar("\nVocê se aproxima da caverna de Valthor e oferece uma trégua.")
    pausar(f"Usando sua {habilidade}, você tenta convencer o dragão.")
    paus