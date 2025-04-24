# -*- coding: utf-8 -*-
import json
import random
import os

# Variaveis globais
jogador = {
    "nome": "Eldrin",
    "mana": 0,
    "mana_max": 0,
    "saude": 0,
    "saude_max": 0,
    "inventario": [],
    "vitorias": 0,
    "cena_atual": "introducao",
    "feiticos": [],
    "habilidades": [],
    "escudo_turnos": 0,
    "classe": ""
}

inimigo_atual = None
sacerdote_vivo = False
sacerdote = None
encapuzado_confrontado = False

# Escolha de Classe (Nivel Maximo)
def escolher_classe():
    while not jogador["classe"]:
        print("Escolha sua classe:")
        print("1. Guerreiro (Foco em Saude e Forca, poucos feiticos)")
        print("2. Ladino (Foco em Destreza e Conhecimento, furtividade e itens)")
        print("3. Mago (Foco em Mana e Conhecimento, muitos feiticos)")
        print("4. Paladino (Foco em Saude, Forca e Carisma, magia divina)")
        print("5. Bardo (Foco em Carisma e Destreza, cancoes e habilidades variadas)")
        escolha = input("Escolha (1-5): ")
        if escolha == "1":
            jogador["classe"] = "Guerreiro"
            jogador["saude_max"] = 110
            jogador["saude"] = 110
            jogador["mana_max"] = 60
            jogador["mana"] = 60
            jogador["feiticos"] = ["Golpe Forte"]
            jogador["habilidades"] = ["Ataque Poderoso", "Defesa", "Vitalidade", "Ataque Extra", "Resistencia"]
            print("Voce se tornou um Guerreiro no nivel maximo.")
        elif escolha == "2":
            jogador["classe"] = "Ladino"
            jogador["saude_max"] = 90
            jogador["saude"] = 90
            jogador["mana_max"] = 70
            jogador["mana"] = 70
            jogador["inventario"].append("Kit de Ladrao")
            jogador["feiticos"] = ["Furtividade"]
            jogador["habilidades"] = ["Esconder nas Sombras", "Golpe Oportunista", "Evasao", "Mestre das Armadilhas", "Assassinar"]
            print("Voce se tornou um Ladino no nivel maximo.")
        elif escolha == "3":
            jogador["classe"] = "Mago"
            jogador["saude_max"] = 80
            jogador["saude"] = 80
            jogador["mana_max"] = 130
            jogador["mana"] = 130
            jogador["feiticos"] = ["Bola de Fogo", "Visao Mistica", "Escudo Arcano", "Raio Congelante", "Ilusao"]
            jogador["habilidades"] = ["Meditacao Arcana", "Escudo Arcano", "Potencializar Magia", "Teletransporte", "Maestria Elemental"]
            print("Voce se tornou um Mago no nivel maximo.")
        elif escolha == "4":
            jogador["classe"] = "Paladino"
            jogador["saude_max"] = 105
            jogador["saude"] = 105
            jogador["mana_max"] = 80
            jogador["mana"] = 80
            jogador["feiticos"] = ["Cura Menor"]
            jogador["habilidades"] = ["Imposicao de Maos", "Aura Protetora", "Julgamento", "Bencao Divina", "Furia Divina"]
            print("Voce se tornou um Paladino no nivel maximo.")
        elif escolha == "5":
            jogador["classe"] = "Bardo"
            jogador["saude_max"] = 95
            jogador["saude"] = 95
            jogador["mana_max"] = 90
            jogador["mana"] = 90
            jogador["feiticos"] = ["Inspiracao", "Balada Lendaria"]
            jogador["habilidades"] = ["Cancao da Bravura", "Melodia Curativa", "Harmonia Inspiradora", "Contracanto", "Balada Lendaria"]
            print("Voce se tornou um Bardo no nivel maximo.")
        else:
            print("Escolha invalida. Tente novamente.")
    print(f"Nome: {jogador['nome']}, Classe: {jogador['classe']}, Saude: {jogador['saude']}/{jogador['saude_max']}, Mana: {jogador['mana']}/{jogador['mana_max']}, Feiticos: {jogador['feiticos']}, Habilidades: {jogador['habilidades']}, Inventario: {jogador['inventario']}")

# Funcoes auxiliares
def salvar_jogo():
    with open("save.json", "w") as f:
        json.dump(jogador, f)
    print("Jogo salvo!")

def carregar_jogo():
    if os.path.exists("save.json"):
        global jogador
        with open("save.json", "r") as f:
            jogador = json.load(f)
        print("Jogo carregado!")
        exibir_cena(jogador["cena_atual"])
    else:
        print("Nenhum jogo salvo encontrado!")

def exibir_cena(cena):
    jogador["cena_atual"] = cena
    if cena in cenas:
        cenas[cena](None)

def mostrar_status():
    print(f"\n--- Estado do Jogador ---")
    print(f"Nome: {jogador['nome']}")
    print(f"Classe: {jogador['classe']}")
    print(f"Saude: {jogador['saude']}/{jogador['saude_max']}")
    print(f"Mana: {jogador['mana']}/{jogador['mana_max']}")
    print(f"Inventario: {jogador['inventario']}")
    print(f"Feiticos: {jogador['feiticos']}")
    print(f"Habilidades: {jogador['habilidades']}")
    print("-------------------------\n")

# Banco de dados para o gerador
aventuras_base = {
    "missoes": [
        {"nome": "Resgatar Aldeao", "descricao": "Um aldeao foi capturado por bandidos na floresta. Salve-o!", "recompensa": {"item": "Pocao de Mana"}, "dificuldade": "Facil"},
        {"nome": "Cacar Espectro", "descricao": "Um espectro assombra as ruinas. Derrote-o para recuperar um tomo.", "recompensa": {"item": "Tomo do Caos"}, "dificuldade": "Media"},
        {"nome": "Explorar Caverna", "descricao": "Uma caverna misteriosa guarda um cajado antigo. Enfrente suas armadilhas.", "recompensa": {"item": "Cajado de Lyssia"}, "dificuldade": "Dificil"}
    ],
    "inimigos": [
        {"nome": "Lobo Sombrio", "hp": 45, "dano": 10, "fraqueza": ["Bola de Fogo"], "historia": "Um predador encantado pela magia negra."},
        {"nome": "Espectro de Kalthar", "hp": 60, "dano": 15, "fraqueza": ["Cura Menor"], "historia": "Um cavaleiro traido, agora amaldicoado."},
        {"nome": "Aranha Necrotica", "hp": 30, "dano": 8, "fraqueza": ["Raio Congelante"], "historia": "Criada por um ritual falho."}
    ]
}

# Funcao geradora
def gerador_aventura(tipo="missao"):
    if tipo == "missao":
        missao = random.choice(aventuras_base["missoes"])
        return {
            "nome": missao["nome"],
            "descricao": missao["descricao"],
            "recompensa": missao["recompensa"],
            "cena": "missao_aleatoria"
        }
    elif tipo == "inimigo":
        inimigo = random.choice(aventuras_base["inimigos"])
        return {
            "nome": inimigo["nome"],
            "hp": inimigo["hp"],
            "dano": inimigo["dano"],
            "fraqueza": inimigo["fraqueza"],
            "historia": inimigo["historia"],
            "cena": "combate_inimigos"
        }

# Funcoes de cenas
def introducao(escolha):
    while True:
        print(f"""
Bem-vindo, {jogador['nome']}, aventureiro!
A cidade de Vaeloria clama por sua ajuda. Desaparecimentos assombram as ruas, e luzes estranhas brilham na Floresta Sombria.
Voce esta nos portoes da cidade. Explore o Salao do Conselho, a taverna ou a biblioteca para investigar.
1. Ir ao Salao do Conselho
2. Visitar a taverna
3. Explorar a biblioteca arcana
4. Salvar jogo
5. Carregar jogo
6. Mostrar Status
        """)
        escolha = input("Escolha (1-6): ")
        if escolha == "1":
            exibir_cena("salao_conselho")
            break
        elif escolha == "2":
            exibir_cena("taverna")
            break
        elif escolha == "3":
            exibir_cena("biblioteca")
            break
        elif escolha == "4":
            salvar_jogo()
        elif escolha == "5":
            carregar_jogo()
            break
        elif escolha == "6":
            mostrar_status()
        else:
            print("Escolha invalida. Tente novamente.")

def salao_conselho(escolha):
    while True:
        print(f"""
No Salao do Conselho, o Lorde Regente e o Capitao da Guarda te recebem. O Regente explica: 'Os desaparecimentos comecaram ha semanas.'
1. Perguntar ao Regente sobre o culto
2. Falar com o Capitao sobre suspeitas
3. Aceitar a missao e partir para a Floresta Sombria
4. Ir para a taverna
5. Ir para a biblioteca arcana
6. Salvar jogo
7. Mostrar Status
        """)
        escolha = input("Escolha (1-7): ")
        if escolha == "1":
            print("O Regente sussurra: 'Ha rumores de um culto nas ruinas.'")
            print("Voce permanece no Salao, ponderando as informacoes.")
        elif escolha == "2":
            print("O Capitao diz: 'Um conselheiro age estranho. Cuidado na floresta.'")
            jogador["inventario"].append("Dica do Traidor")
            print("Voce permanece no Salao, avaliando a dica.")
        elif escolha == "3":
            print("Voce aceita a missao e parte para a Floresta Sombria.")
            jogador["inventario"].append("Mapa da Floresta")
            exibir_cena("floresta_sombria")
            break
        elif escolha == "4":
            print("Voce sai do Salao e vai para a taverna.")
            exibir_cena("taverna")
            break
        elif escolha == "5":
            print("Voce sai do Salao e vai para a biblioteca arcana.")
            exibir_cena("biblioteca")
            break
        elif escolha == "6":
            salvar_jogo()
        elif escolha == "7":
            mostrar_status()
        else:
            print("Escolha invalida. Tente novamente.")

def taverna(escolha):
    global encapuzado_confrontado
    while True:
        print(f"""
Na taverna, um velho bebado murmura sobre 'sombras que falam'. {'Um encapuzado te observa.' if not encapuzado_confrontado else 'O encapuzado ja foi confrontado.'}
1. Confrontar o encapuzado{' (indisponivel)' if encapuzado_confrontado else ''}
2. Falar com o bebado
3. Sair da taverna
4. Ir para o Salao do Conselho
5. Ir para a biblioteca arcana
6. Usar Pocao de Mana (se tiver)
7. Salvar jogo
8. Mostrar Status
        """)
        escolha = input("Escolha (1-8): ")
        if escolha == "1":
            if not encapuzado_confrontado:
                print("O encapuzado foge, mas deixa cair um pingente.")
                jogador["inventario"].append("Pingente Misterioso")
                encapuzado_confrontado = True
                print("Voce permanece na taverna, observando o ambiente.")
            else:
                print("Voce ja confrontou o encapuzado.")
        elif escolha == "2":
            print("O bebado diz: 'Eles se reunem nas ruinas antigas.'")
            print("Voce permanece na taverna, refletindo sobre a informacao.")
        elif escolha == "3":
            if "Mapa da Floresta" in jogador["inventario"]:
                print("Com o mapa em maos, voce sai da taverna e segue para a Floresta Sombria.")
                exibir_cena("floresta_sombria")
                break
            else:
                print("Voce sai da taverna, mas sem um mapa, decide voltar ao Salao do Conselho.")
                exibir_cena("salao_conselho")
                break
        elif escolha == "4":
            print("Voce sai da taverna e vai para o Salao do Conselho.")
            exibir_cena("salao_conselho")
            break
        elif escolha == "5":
            print("Voce sai da taverna e vai para a biblioteca arcana.")
            exibir_cena("biblioteca")
            break
        elif escolha == "6":
            if "Pocao de Mana" in jogador["inventario"]:
                jogador["mana"] = min(jogador["mana_max"], jogador["mana"] + 30)
                jogador["inventario"].remove("Pocao de Mana")
                print("Voce usou uma Pocao de Mana, restaurando 30 de Mana.")
            else:
                print("Voce nao tem Pocoes de Mana.")
        elif escolha == "7":
            salvar_jogo()
        elif escolha == "8":
            mostrar_status()
        else:
            print("Escolha invalida. Tente novamente.")

def biblioteca(escolha):
    while True:
        print(f"""
Na biblioteca arcana, voce encontra um tomo sobre magias proibidas.
1. Lancar Visao Mistica (-10 Mana)
2. Continuar lendo o tomo
3. Sair da biblioteca
4. Ir para o Salao do Conselho
5. Ir para a taverna
6. Usar Pocao de Mana (se tiver)
7. Salvar jogo
8. Mostrar Status
        """)
        escolha = input("Escolha (1-8): ")
        if escolha == "1":
            if jogador["mana"] >= 10 and "Visao Mistica" in jogador["feiticos"]:
                jogador["mana"] -= 10
                print("Voce ve uma visao: um altar na floresta, pulsando com energia negra.")
                print("Voce continua na biblioteca, analisando a visao.")
            elif "Visao Mistica" not in jogador["feiticos"]:
                print("Voce nao conhece esse feitico.")
            else:
                print("Mana insuficiente!")
        elif escolha == "2":
            print("O tomo menciona um culto antigo.")
            print("Voce permanece na biblioteca, folheando o tomo.")
        elif escolha == "3":
            if "Mapa da Floresta" in jogador["inventario"]:
                print("Com o mapa em maos, voce sai da biblioteca e segue para a Floresta Sombria.")
                exibir_cena("floresta_sombria")
                break
            else:
                print("Voce sai da biblioteca, mas sem um mapa, decide voltar ao Salao do Conselho.")
                exibir_cena("salao_conselho")
                break
        elif escolha == "4":
            print("Voce sai da biblioteca e vai para o Salao do Conselho.")
            exibir_cena("salao_conselho")
            break
        elif escolha == "5":
            print("Voce sai da biblioteca e vai para a taverna.")
            exibir_cena("taverna")
            break
        elif escolha == "6":
            if "Pocao de Mana" in jogador["inventario"]:
                jogador["mana"] = min(jogador["mana_max"], jogador["mana"] + 30)
                jogador["inventario"].remove("Pocao de Mana")
                print("Voce usou uma Pocao de Mana, restaurando 30 de Mana.")
            else:
                print("Voce nao tem Pocoes de Mana.")
        elif escolha == "7":
            salvar_jogo()
        elif escolha == "8":
            mostrar_status()
        else:
            print("Escolha invalida. Tente novamente.")

def floresta_sombria(escolha):
    if "Mapa da Floresta" not in jogador["inventario"]:
        print("Voce precisa do Mapa da Floresta para explorar esta area. Volte ao Salao do Conselho.")
        exibir_cena("salao_conselho")
        return
    while True:
        print(f"""
Mana: {jogador['mana']}/{jogador['mana_max']} | Saude: {jogador['saude']}/{jogador['saude_max']}
Inventario: {jogador['inventario']}
Voce entra na Floresta Sombria. O ar e pesado, e sussurros ecoam.
1. Explorar uma trilha estreita
2. Lancar Visao Mistica (-10 Mana)
3. Seguir um ruido estranho
4. Buscar uma nova missao
5. Usar Pocao de Mana (se tiver)
6. Salvar jogo
7. Mostrar Status
        """)
        escolha = input("Escolha (1-7): ")
        if escolha == "1":
            if random.random() < 0.4:
                if random.random() < 0.3 and "Dica do Traidor" in jogador["inventario"]:
                    print("Voce encontra pistas do Traidor e segue para um confronto.")
                    exibir_cena("encontro_truidor")
                    break
                else:
                    print("Um evento inesperado ocorre na floresta...")
                    evento_aleatorio(None)
                    break
            else:
                print("Inimigos surgem das sombras!")
                exibir_cena("combate_inimigos")
                break
        elif escolha == "2":
            if jogador["mana"] >= 10 and "Visao Mistica" in jogador["feiticos"]:
                jogador["mana"] -= 10
                print("Visao Mistica revela uma armadilha. Voce encontra ruinas antigas.")
                exibir_cena("ruinas_antigas")
                break
            elif "Visao Mistica" not in jogador["feiticos"]:
                print("Voce nao conhece esse feitico.")
            else:
                print("Mana insuficiente!")
        elif escolha == "3":
            print("Voce segue o ruido e encontra um eremita misterioso.")
            exibir_cena("encontro_eremita")
            break
        elif escolha == "4":
            print("Voce busca uma nova missao na floresta...")
            exibir_cena("missao_aleatoria")
            break
        elif escolha == "5":
            if "Pocao de Mana" in jogador["inventario"]:
                jogador["mana"] = min(jogador["mana_max"], jogador["mana"] + 30)
                jogador["inventario"].remove("Pocao de Mana")
                print("Voce usou uma Pocao de Mana, restaurando 30 de Mana.")
            else:
                print("Voce nao tem Pocoes de Mana.")
        elif escolha == "6":
            salvar_jogo()
        elif escolha == "7":
            mostrar_status()
        else:
            print("Escolha invalida. Tente novamente.")

def evento_aleatorio(escolha):
    eventos = [
        ("Voce encontra um bau encantado. Dentro, ha uma Pocao de Mana.", lambda: jogador["inventario"].append("Pocao de Mana")),
        ("Uma armadilha magica dispara! Voce perde saude.", lambda: jogador.update({"saude": max(0, jogador["saude"] - 12)})),
        ("Um viajante perdido te da um Amuleto de Protecao.", lambda: jogador["inventario"].append("Amuleto de Protecao")),
        ("Um Corvo Necrotico ataca!", lambda: None, "combate_inimigos", {"nome": "Corvo Necrotico", "hp": 30, "dano": 12, "texto": "Um corvo necrotico voa em sua direcao!", "fraqueza": ["Ilusao", "Raio Congelante"], "esquiva": 0.3})
    ]
    evento, efeito, *extras = random.choice(eventos)
    print(f"{evento}\n1. Continuar")
    input("Escolha (1): ")
    if len(extras) > 0:
        jogador["cena_atual"] = extras[0]
        global inimigo_atual
        inimigo_atual = extras[1]
        inimigo_atual["hp_atual"] = inimigo_atual["hp"]
        exibir_cena("combate_inimigos")
    else:
        efeito()
        if jogador["saude"] <= 0:
            fim_jogo("Voce sucumbe aos ferimentos. Vaeloria esta perdida.")
        else:
            exibir_cena("floresta_sombria")

def encontro_truidor(escolha):
    while True:
        print(f"""
Voce encontra o Traidor, um conselheiro corrupto, escondido na floresta. Ele segura um pergaminho sombrio e te encara com desdem.
1. Confronta-lo com palavras
2. Atacar imediatamente
3. Tentar fugir
4. Salvar jogo
5. Mostrar Status
        """)
        escolha = input("Escolha (1-5): ")
        if escolha == "1":
            print("Com palavras firmes, voce convence o Traidor a revelar seus planos. Ele entrega o pergaminho.")
            jogador["inventario"].append("Pergaminho Sombrio")
            print("Voce segue para as ruinas, com novas informacoes.")
            exibir_cena("ruinas_antigas")
            break
        elif escolha == "2":
            print("Voce golpeia o Traidor com forca, derrotando-o rapidamente. Voce pega seu pergaminho.")
            jogador["inventario"].append("Pergaminho Sombrio")
            jogador["vitorias"] += 1
            print("Voce segue para as ruinas, vitorioso.")
            exibir_cena("ruinas_antigas")
            break
        elif escolha == "3":
            print("Voce tenta fugir, mas o Traidor te alcanca e ataca!")
            jogador["saude"] -= 5  # Reduzido de 10 para 5
            print("Voce perde 5 de saude na fuga.")
            if jogador["saude"] <= 0:
                fim_jogo("Voce sucumbe aos ferimentos do Traidor. Vaeloria esta perdida.")
                break
            print("Voce escapa e segue para as ruinas.")
            exibir_cena("ruinas_antigas")
            break
        elif escolha == "4":
            salvar_jogo()
        elif escolha == "5":
            mostrar_status()
        else:
            print("Escolha invalida. Tente novamente.")

def encontro_eremita(escolha):
    while True:
        print(f"""
Um eremita sabio surge entre as arvores. Seus olhos brilham com conhecimento antigo, e ele parece saber sobre o culto.
1. Pedir conselhos sobre o culto
2. Oferecer ajuda em troca de informacoes
3. Ignorar o eremita e seguir adiante
4. Salvar jogo
5. Mostrar Status
        """)
        escolha = input("Escolha (1-5): ")
        if escolha == "1":
            print("O eremita revela: 'O culto usa um pergaminho para selar seu ritual. Encontre-o nas ruinas.'")
            jogador["inventario"].append("Pergaminho de Selamento")
            print("Voce segue para as ruinas, com o pergaminho em maos.")
            exibir_cena("ruinas_antigas")
            break
        elif escolha == "2":
            print("Impressionado com sua oferta, o eremita decide te acompanhar como aliado.")
            jogador["inventario"].append("Aliada Eremita")
            print("Voce segue para as ruinas com o eremita ao seu lado.")
            exibir_cena("ruinas_antigas")
            break
        elif escolha == "3":
            print("Voce ignora o eremita e segue seu caminho para as ruinas.")
            exibir_cena("ruinas_antigas")
            break
        elif escolha == "4":
            salvar_jogo()
        elif escolha == "5":
            mostrar_status()
        else:
            print("Escolha invalida. Tente novamente.")

def ruinas_antigas(escolha):
    while True:
        print(f"""
Voce chega as ruinas antigas, cobertas por trepadeiras e energia sombria. Um altar pulsa ao longe.
1. Investigar o altar
2. Lancar Visao Mistica (-10 Mana)
3. Usar Pocao de Mana (se tiver)
4. Usar Cura Menor (se tiver)
5. Salvar jogo
6. Mostrar Status
        """)
        escolha = input("Escolha (1-6): ")
        if escolha == "1":
            print("Voce se aproxima do altar, mas inimigos menores aparecem antes do confronto final!")
            exibir_cena("combate_inimigos")
            if jogador["saude"] > 0:  # Se sobreviver ao combate inicial
                exibir_cena("altar_sacrificio")
            break
        elif escolha == "2":
            if jogador["mana"] >= 10 and "Visao Mistica" in jogador["feiticos"]:
                jogador["mana"] -= 10
                print("Visao Mistica revela o ritual no altar. Voce avanca com cuidado.")
                exibir_cena("altar_sacrificio")
                break
            elif "Visao Mistica" not in jogador["feiticos"]:
                print("Voce nao conhece esse feitico.")
            else:
                print("Mana insuficiente!")
        elif escolha == "3":
            if "Pocao de Mana" in jogador["inventario"]:
                jogador["mana"] = min(jogador["mana_max"], jogador["mana"] + 30)
                jogador["inventario"].remove("Pocao de Mana")
                print("Voce usou uma Pocao de Mana, restaurando 30 de Mana.")
            else:
                print("Voce nao tem Pocoes de Mana.")
        elif escolha == "4":
            if "Cura Menor" in jogador["feiticos"] and jogador["mana"] >= 15:
                jogador["mana"] -= 15
                jogador["saude"] = min(jogador["saude_max"], jogador["saude"] + 25)
                print("Voce usou Cura Menor, restaurando 25 de saude.")
            else:
                print("Voce nao tem o feitico Cura Menor ou mana suficiente.")
        elif escolha == "5":
            salvar_jogo()
        elif escolha == "6":
            mostrar_status()
        else:
            print("Escolha invalida. Tente novamente.")

def missao_aleatoria(escolha):
    global inimigo_atual
    missao = gerador_aventura("missao")
    while True:
        print(f"""
Nova Missao: {missao['nome']}
Descricao: {missao['descricao']}
Recompensa: {missao['recompensa']['item']}
1. Aceitar a missao
2. Recusar e voltar
3. Salvar jogo
4. Mostrar Status
        """)
        escolha = input("Escolha (1-4): ")
        if escolha == "1":
            print(f"Voce aceita a missao: {missao['nome']}!")
            inimigo_atual = gerador_aventura("inimigo")
            inimigo_atual["hp_atual"] = inimigo_atual["hp"]
            print(f"Um {inimigo_atual['nome']} aparece! Historia: {inimigo_atual['historia']}")
            exibir_cena("combate_inimigos")
            if jogador["saude"] > 0:  # Apos combate, se sobreviver
                jogador["inventario"].append(missao["recompensa"]["item"])
                print(f"Missao concluida! Ganhou {missao['recompensa']['item']}.")
            exibir_cena("floresta_sombria")
            break
        elif escolha == "2":
            print("Voce recusa a missao e retorna.")
            exibir_cena("floresta_sombria")
            break
        elif escolha == "3":
            salvar_jogo()
        elif escolha == "4":
            mostrar_status()
        else:
            print("Escolha invalida. Tente novamente.")

def combate_inimigos(escolha):
    global inimigo_atual
    if escolha is None:
        inimigos = [
            {"nome": "Lobos Sombrios", "hp": 45, "dano": 10, "texto": "Dois lobos sombrios emergem, olhos brilhando.", "fraqueza": ["Bola de Fogo", "Raio Congelante"]},
            {"nome": "Espectros Arcanos", "hp": 35, "dano": 12, "texto": "Espectros flutuam, imunes a ataques fisicos.", "fraqueza": ["Visao Mistica", "Ilusao"]},
            {"nome": "Golem Corrompido", "hp": 75, "dano": 15, "texto": "Um golem avanca, lento mas resistente.", "fraqueza": ["Ilusao"]}
        ]
        inimigo_atual = random.choice(inimigos)
        inimigo_atual["hp_atual"] = inimigo_atual["hp"]

    opcoes_combate = [f"{i+1}. Lancar {feitico} ({custo} Mana)" for i, (feitico, custo) in enumerate([
        ("Bola de Fogo", 20), ("Escudo Arcano", 20), ("Visao Mistica", 10),
        ("Raio Congelante", 25), ("Ilusao", 15), ("Cura Menor", 15), ("Balada Lendaria", 15)
    ]) if feitico in jogador["feiticos"]] + [f"{len(jogador['feiticos'])+1}. Tentar fugir"]

    while inimigo_atual["hp_atual"] > 0 and jogador["saude"] > 0:
        print(f"\n--- Combate ---")
        print(f"{inimigo_atual['texto']}")
        print(f"Inimigo: {inimigo_atual['nome']} | HP: {inimigo_atual['hp_atual']}/{inimigo_atual['hp']}")
        mostrar_status()
        print("Escolha uma acao:")
        for opcao in opcoes_combate:
            print(opcao)
        escolha_combate = input(f"Escolha (1-{len(opcoes_combate)}): ")

        if escolha_combate.isdigit():
            escolha_index = int(escolha_combate) - 1
            if 0 <= escolha_index < len(opcoes_combate) - 1:
                feitico_escolhido = opcoes_combate[escolha_index].split(" (")[0].split(". ")[1].replace("Lancar ", "")
                custo = int(opcoes_combate[escolha_index].split("(")[1].split(" ")[0])

                if jogador["mana"] >= custo:
                    jogador["mana"] -= custo
                    dano = 0
                    if feitico_escolhido == "Bola de Fogo":
                        dano = 30 if feitico_escolhido in inimigo_atual["fraqueza"] else 15
                    elif feitico_escolhido == "Raio Congelante":
                        dano = 25 if feitico_escolhido in inimigo_atual["fraqueza"] else 10
                    elif feitico_escolhido == "Ilusao":
                        dano = 20 if feitico_escolhido in inimigo_atual["fraqueza"] else 5
                    elif feitico_escolhido == "Visao Mistica":
                        dano = 10
                    elif feitico_escolhido == "Cura Menor":
                        jogador["saude"] = min(jogador["saude_max"], jogador["saude"] + 20)
                        print("Voce usou Cura Menor, restaurando sua saude.")
                        dano = 0
                    elif feitico_escolhido == "Escudo Arcano":
                        print("Escudo Arcano reduz danos por 2 turnos!")
                        jogador["escudo_turnos"] = 2
                        dano = 0
                    elif feitico_escolhido == "Golpe Forte":
                        dano = 30  # Ajustado para ser fixo, sem depender de forca
                    elif feitico_escolhido == "Furtividade":
                        print("Voce tenta se esconder nas sombras...")
                        if random.random() < 0.75:  # Aumentei a chance de sucesso
                            print("Voce escapa do combate!")
                            return "ruinas_antigas"
                        else:
                            print("Voce falha em se esconder!")
                            dano = 0
                    elif feitico_escolhido == "Inspiracao":
                        print("Voce inspira a si mesmo, aumentando ligeiramente seu proximo ataque.")
                        dano = 0
                    elif feitico_escolhido == "Balada Lendaria":
                        dano = 50
                        print("Sua balada ressoa com poder!")

                    if dano > 0:
                        if "esquiva" in inimigo_atual and random.random() < inimigo_atual["esquiva"]:
                            print(f"{inimigo_atual['nome']} esquiva seu ataque!")
                        else:
                            inimigo_atual["hp_atual"] -= dano
                            print(f"Voce usou {feitico_escolhido}, causando {dano} de dano!")

                    if inimigo_atual["hp_atual"] <= 0:
                        print(f"Voce derrotou {inimigo_atual['nome']}!")
                        jogador["vitorias"] += 1
                        if random.random() < 0.6:
                            jogador["inventario"].append("Pocao de Mana")
                            print("Voce encontrou uma Pocao de Mana!")
                        return "ruinas_antigas"

                    dano_inimigo = inimigo_atual["dano"]
                    if jogador["escudo_turnos"] > 0:
                        dano_inimigo //= 2
                        jogador["escudo_turnos"] -= 1
                    if "Amuleto de Protecao" in jogador["inventario"]:
                        dano_inimigo = int(dano_inimigo * 0.8)
                    jogador["saude"] -= dano_inimigo
                    print(f"{inimigo_atual['nome']} ataca, causando {dano_inimigo} de dano!")

                    if jogador["saude"] <= 0:
                        fim_jogo("Voce sucumbe aos ferimentos. Vaeloria esta perdida.")
                        return None

                else:
                    print("Mana insuficiente!")
            elif escolha_index == len(opcoes_combate) - 1:
                sorte = random.randint(1, 10)
                if sorte > 4:
                    print("Voce escapa, mas se machuca na fuga.")
                    jogador["saude"] -= 8
                    return "ruinas_antigas"
                else:
                    print("Voce nao escapa e e atacado!")
                    dano_inimigo = inimigo_atual["dano"]
                    if jogador["escudo_turnos"] > 0:
                        dano_inimigo //= 2
                        jogador["escudo_turnos"] -= 1
                    if "Amuleto de Protecao" in jogador["inventario"]:
                        dano_inimigo = int(dano_inimigo * 0.8)
                    jogador["saude"] -= dano_inimigo
                    print(f"{inimigo_atual['nome']} ataca, causando {dano_inimigo} de dano!")
                    if jogador["saude"] <= 0:
                        fim_jogo("Voce sucumbe aos ferimentos. Vaeloria esta perdida.")
                        return None
            else:
                print("Escolha invalida.")
        else:
            print("Entrada invalida.")

    return jogador["cena_atual"]

def altar_sacrificio(escolha):
    global sacerdote_vivo, sacerdote
    if sacerdote is None:
        sacerdote = {"nome": "Sumo Sacerdote", "hp": 60, "mana": 50, "dano_magico": 15, "texto": "O Sumo Sacerdote do culto esta realizando o ritual!", "fraqueza": ["Segredo do Culto", "Balada Lendaria"]}
        sacerdote_vivo = True

    while sacerdote_vivo and jogador["saude"] > 0:
        print(f"\n--- Altar de Sacrificio ---")
        print(f"{sacerdote['texto']} HP: {sacerdote['hp']}/{60}, Mana: {sacerdote['mana']}/{50}")
        mostrar_status()
        opcoes_climax = [f"{i+1}. Lancar {feitico} ({custo} Mana)" for i, (feitico, custo) in enumerate([
            ("Bola de Fogo", 20), ("Raio Congelante", 25), ("Ilusao", 15), ("Visao Mistica", 10), ("Cura Menor", 15), ("Balada Lendaria", 15)
        ]) if feitico in jogador["feiticos"]]
        num_feiticos = len(opcoes_climax)
        opcoes_climax.append(f"{num_feiticos + 1}. Tentar selar o ritual (Pergaminho de Selamento)")
        if "Pingente Misterioso" in jogador["inventario"]:
            opcoes_climax.append(f"{num_feiticos + 2}. Usar o Pingente Misterioso")
        if "Aliada Eremita" in jogador["inventario"]:
            opcoes_climax.append(f"{num_feiticos + 3 if 'Pingente Misterioso' in jogador['inventario'] else num_feiticos + 2}. Pedir ajuda a Eremita")
        opcoes_climax.append(f"{len(opcoes_climax) + 1}. Fugir")
        opcoes_climax.append(f"{len(opcoes_climax) + 1}. Salvar jogo")
        opcoes_climax.append(f"{len(opcoes_climax) + 1}. Mostrar Status")

        print("Escolha uma acao:")
        for opcao in opcoes_climax:
            print(opcao)
        escolha_climax = input(f"Escolha (1-{len(opcoes_climax)}): ")

        if escolha_climax.isdigit():
            escolha_index = int(escolha_climax) - 1
            num_feiticos_base = len([f for f in jogador['feiticos'] if f in ["Bola de Fogo", "Raio Congelante", "Ilusao", "Visao Mistica", "Cura Menor", "Balada Lendaria"]])

            if 0 <= escolha_index < num_feiticos_base:
                feitico_escolhido = [f for f in jogador['feiticos'] if f in ["Bola de Fogo", "Raio Congelante", "Ilusao", "Visao Mistica", "Cura Menor", "Balada Lendaria"]][escolha_index]
                custo = [20 if f == "Bola de Fogo" else 25 if f == "Raio Congelante" else 15 if f == "Ilusao" else 10 if f == "Visao Mistica" else 15 for f in jogador['feiticos'] if f in ["Bola de Fogo", "Raio Congelante", "Ilusao", "Visao Mistica", "Cura Menor", "Balada Lendaria"]][escolha_index]

                if jogador["mana"] >= custo:
                    jogador["mana"] -= custo
                    dano_jogador = 0
                    if feitico_escolhido == "Bola de Fogo":
                        dano_jogador = 35 if "Segredo do Culto" in jogador["inventario"] else 20
                    elif feitico_escolhido == "Raio Congelante":
                        dano_jogador = 30 if "Segredo do Culto" in jogador["inventario"] else 15
                    elif feitico_escolhido == "Ilusao":
                        dano_jogador = 25
                    elif feitico_escolhido == "Visao Mistica":
                        dano_jogador = 15
                    elif feitico_escolhido == "Cura Menor":
                        jogador["saude"] = min(jogador["saude_max"], jogador["saude"] + 25)
                        print("Voce usou Cura Menor, restaurando sua saude.")
                        dano_jogador = 0
                    elif feitico_escolhido == "Golpe Forte":
                        dano_jogador = 30
                    elif feitico_escolhido == "Inspiracao":
                        print("Voce se sente mais inspirado!")
                        dano_jogador = 0
                    elif feitico_escolhido == "Balada Lendaria":
                        dano_jogador = 50
                        print("Sua balada ressoa com poder!")

                    if dano_jogador > 0:
                        sacerdote["hp"] -= dano_jogador
                        print(f"Voce usou {feitico_escolhido}, causando {dano_jogador} de dano!")
                else:
                    print("Mana insuficiente!")

            elif escolha_index == num_feiticos_base:
                if "Pergaminho de Selamento" in jogador["inventario"]:
                    print("Voce le o pergaminho antigo. O ritual e desfeito! O mago negro nao renascera.")
                    fim_jogo("Vitoria! Vaeloria esta salva.")
                    break
                else:
                    print("Voce nao tem o pergaminho de selamento!")

            elif "Pingente Misterioso" in jogador["inventario"] and escolha_index == num_feiticos_base + 1:
                print("Voce usa o Pingente Misterioso, que brilha intensamente. Um segredo do culto e revelado, enfraquecendo o sacerdote!")
                jogador["inventario"].append("Segredo do Culto")
                jogador["inventario"].remove("Pingente Misterioso")
                sacerdote["hp"] -= 10
                print("O Sumo Sacerdote perde 10 HP!")

            elif "Aliada Eremita" in jogador["inventario"] and escolha_index == (num_feiticos_base + 2 if "Pingente Misterioso" in jogador["inventario"] else num_feiticos_base + 1):
                print("A eremita ataca o sacerdote com magia ancestral!")
                dano_eremita = random.randint(20, 40)
                sacerdote["hp"] -= dano_eremita
                print(f"A eremita causa {dano_eremita} de dano!")
                if random.random() < 0.3:
                    print("A eremita e gravemente ferida!")
                    jogador["inventario"].remove("Aliada Eremita")

            elif escolha_index == (num_feiticos_base + (3 if "Pingente Misterioso" in jogador["inventario"] else 2) if "Aliada Eremita" in jogador["inventario"] else num_feiticos_base + (2 if "Pingente Misterioso" in jogador["inventario"] else 1)):
                print("Voce tenta fugir do altar...")
                sorte_fuga = random.randint(1, 10)
                if sorte_fuga > 3:
                    print("Voce consegue escapar das ruinas.")
                    exibir_cena("floresta_sombria")
                    break
                else:
                    print("Voce nao consegue fugir!")

            elif escolha_index == (num_feiticos_base + (4 if "Pingente Misterioso" in jogador["inventario"] else 3) if "Aliada Eremita" in jogador["inventario"] else num_feiticos_base + (3 if "Pingente Misterioso" in jogador["inventario"] else 2)):
                salvar_jogo()

            elif escolha_index == (num_feiticos_base + (5 if "Pingente Misterioso" in jogador["inventario"] else 4) if "Aliada Eremita" in jogador["inventario"] else num_feiticos_base + (4 if "Pingente Misterioso" in jogador["inventario"] else 3)):
                mostrar_status()

            else:
                print("Escolha invalida.")

            if sacerdote["hp"] > 0:
                dano_sacerdote = sacerdote["dano_magico"]
                if "Amuleto de Protecao" in jogador["inventario"]:
                    dano_sacerdote = int(dano_sacerdote * 0.8)
                if "Pingente Misterioso" in jogador["inventario"]:
                    dano_sacerdote = int(dano_sacerdote * 0.8)
                jogador["saude"] -= dano_sacerdote
                print(f"O Sumo Sacerdote lanca Raio Sombrio, causando {dano_sacerdote} de dano!")

                if jogador["saude"] <= 0:
                    fim_jogo("Voce foi derrotado pelo Sumo Sacerdote. O mago negro renasceu.")
                    sacerdote_vivo = False

            if sacerdote["hp"] <= 0:
                print("O Sumo Sacerdote cai! O ritual e interrompido.")
                fim_jogo("Vitoria! O culto foi desmantelado.")
                sacerdote_vivo = False
        else:
            print("Entrada invalida.")
    if not sacerdote_vivo:
        exibir_cena("fim_jogo")

def fim_jogo(mensagem):
    print("\n--- Fim de Jogo ---")
    print(mensagem)
    print("---------------------\n")

# Mapa de cenas
cenas = {
    "introducao": introducao,
    "salao_conselho": salao_conselho,
    "taverna": taverna,
    "biblioteca": biblioteca,
    "floresta_sombria": floresta_sombria,
    "combate_inimigos": combate_inimigos,
    "encontro_eremita": encontro_eremita,
    "ruinas_antigas": ruinas_antigas,
    "altar_sacrificio": altar_sacrificio,
    "fim_jogo": fim_jogo,
    "evento_aleatorio": evento_aleatorio,
    "encontro_truidor": encontro_truidor,
    "missao_aleatoria": missao_aleatoria
}

# Iniciar o jogo
escolher_classe()
exibir_cena("introducao")