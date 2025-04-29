import time
import sys

def pausar(texto):
    print(texto, flush=True)
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
        print("Digite o número da sua classe (1-4): ", end="", flush=True)
        escolha = input().strip()
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
            pausar("Escolha inválida! Digite um número de 1 a 4.")

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
    pausar("Iniciando o jogo...")
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
        print("Qual caminho você escolhe? (1-5): ", end="", flush=True)
        escolha = input().strip()

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
            pausar("Escolha inválida! Digite 1, 2, 3, 4 ou 5.")

def caminho_caverna(classe, habilidade):
    pausar("\nVocê entra na caverna escura de Valthor, ouvindo seu rugido ecoar.")
    pausar(f"Você confia em sua {habilidade} para enfrentar o dragão.")
    pausar("Valthor desperta e avança! Você deve decidir rapidamente:")
    pausar("1. Atacar com tudo o que tem.")
    pausar("2. Tentar se esconder e atacar pelas costas.")

    while True:
        print("O que você faz? (1, 2): ", end="", flush=True)
        escolha = input().strip()
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
            pausar("Escolha inválida! Digite 1 ou 2.")

def caminho_templo(classe, habilidade):
    pausar("\nVocê viaja até o templo em ruínas, enfrentando armadilhas mortais.")
    pausar(f"Usando sua {habilidade}, você chega à câmara da Lança do Destino.")
    pausar("Ao pegar a lança, você sente seu poder. Mas o templo começa a desmoronar!")
    pausar("Você deve decidir rapidamente:")
    pausar("1. Correr para fora do templo com a lança.")
    pausar("2. Explorar a câmara em busca de mais tesouros.")
    pausar("3. Usar sua habilidade para estabilizar o templo.")

    while True:
        print("O que você faz? (1, 2, 3): ", end="", flush=True)
        escolha = input().strip()
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
            pausar("Escolha inválida! Digite 1, 2 ou 3.")

def caminho_negociacao(classe, habilidade):
    pausar("\nVocê se aproxima da caverna de Valthor e oferece uma trégua.")
    pausar(f"Usando sua {habilidade}, você tenta convencer o dragão.")
    pausar("Valthor ouve, mas exige algo em troca. Ele propõe:")
    pausar("1. Oferecer sua lealdade eterna como servo.")
    pausar("2. Entregar a vila de Eldoria como tributo.")

    while True:
        print("O que você faz? (1, 2): ", end="", flush=True)
        escolha = input().strip()
        if escolha == "1":
            if classe == "bardo":
                pausar("Sua música acalma Valthor, que aceita sua lealdade.")
                pausar("Você salva Eldoria, mas vive como servo do dragão.")
                final_agridoce()
            else:
                pausar("Valthor aceita, mas logo se cansa de você e o devora.")
                final_ruim()
            break
        elif escolha == "2":
            pausar("Você trai Eldoria, e Valthor poupa sua vida.")
            pausar("Você vive, mas carrega a culpa pela destruição da vila.")
            final_agridoce()
            break
        else:
            pausar("Escolha inválida! Digite 1 ou 2.")

def caminho_aliados(classe, habilidade):
    pausar("\nVocê viaja para Thornvale para recrutar aliados contra Valthor.")
    pausar(f"Usando sua {habilidade}, você tenta convencer os guerreiros locais.")
    pausar("O líder de Thornvale exige uma prova de sua coragem:")
    pausar("1. Derrotar um lobo gigante na arena.")
    pausar("2. Roubar um artefato dos bandidos locais.")

    while True:
        print("O que você faz? (1, 2): ", end="", flush=True)
        escolha = input().strip()
        if escolha == "1":
            if classe in ["guerreiro", "mago"]:
                pausar("Você derrota o lobo com sua habilidade, ganhando aliados.")
                pausar("Com o exército, você enfrenta e derrota Valthor!")
                final_bom()
            else:
                pausar("O lobo é forte demais, e você é gravemente ferido.")
                pausar("Sem aliados, você não pode enfrentar Valthor.")
                final_ruim()
            break
        elif escolha == "2":
            if classe == "ladino":
                pausar("Você rouba o artefato com sucesso, impressionando Thornvale.")
                pausar("Com aliados, você derrota Valthor!")
                final_bom()
            else:
                pausar("Você é pego pelos bandidos e não consegue aliados.")
                pausar("Sem apoio, Valthor destrói Eldoria.")
                final_ruim()
            break
        else:
            pausar("Escolha inválida! Digite 1 ou 2.")

def caminho_floresta(classe, habilidade):
    pausar("\nVocê entra na Floresta Sombria, onde dizem haver um orbe místico.")
    pausar(f"Usando sua {habilidade}, você enfrenta perigos sobrenaturais.")
    pausar("Você encontra o orbe, mas um espírito guardião aparece!")
    pausar("1. Tentar convencer o espírito a entregar o orbe.")
    pausar("2. Lutar contra o espírito pelo orbe.")

    while True:
        print("O que você faz? (1, 2): ", end="", flush=True)
        escolha = input().strip()
        if escolha == "1":
            if classe == "bardo":
                pausar("Seu charme convence o espírito, que lhe dá o orbe.")
                pausar("Com o orbe, você enfraquece Valthor e o derrota!")
                final_bom()
            else:
                pausar("O espírito não confia em você e o amaldiçoa.")
                pausar("Você perece na floresta, e Eldoria é destruída.")
                final_ruim()
            break
        elif escolha == "2":
            if classe in ["guerreiro", "mago"]:
                pausar("Você derrota o espírito e toma o orbe!")
                pausar("Com o orbe, você mata Valthor e salva Eldoria.")
                final_bom()
            else:
                pausar("O espírito é poderoso demais e o derrota.")
                pausar("Sem o orbe, Eldoria cai perante Valthor.")
                final_ruim()
            break
        else:
            pausar("Escolha inválida! Digite 1 ou 2.")

def final_bom():
    pausar("\nVocê derrota Valthor e salva Eldoria!")
    pausar("Os aldeões o celebram como herói, e seu nome é lembrado por gerações.")
    pausar("FIM - Final Bom")

def final_ruim():
    pausar("\nVocê falha em sua missão e morre tragicamente.")
    pausar("Eldoria é destruída por Valthor, e seu nome é esquecido.")
    pausar("FIM - Final Ruim")

def final_agridoce():
    pausar("\nVocê evita a destruição de Eldoria, mas a um custo pessoal.")
    pausar("Você vive com o peso de suas escolhas, longe da glória.")
    pausar("FIM - Final Agridoce")

if __name__ == "__main__":
    jogo()
    print("Programa finalizado!", flush=True)