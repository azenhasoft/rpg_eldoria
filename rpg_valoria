import json
import random
import os

# Atributos do jogador
jogador = {
    "nome": "Eldrin",
    "mana": 0,
    "mana_max": 0,
    "saude": 0,
    "saude_max": 0,
    "conhecimento": 0,
    "forca": 0,  # Adicionando atributo de Força para Guerreiro e Paladino
    "destreza": 0, # Adicionando atributo de Destreza para Ladino e Bardo
    "carisma": 0, # Adicionando atributo de Carisma para Paladino e Bardo
    "inventario": [],
    "vitorias": 0,
    "cena_atual": "introducao",
    "nivel": 1,
    "xp": 0,
    "feitiços": [],
    "habilidades": [], # Adicionando lista para habilidades específicas de classe
    "escudo_turnos": 0,
    "classe": ""
}

# Variáveis globais
inimigo_atual = None
sacerdote_vivo = False
sacerdote = None

# Escolha de Classe
def escolher_classe():
    while not jogador["classe"]:
        print("Escolha sua classe:")
        print("1. Guerreiro (Foco em Saúde e Força, poucos feitiços)")
        print("2. Ladino (Foco em Destreza e Conhecimento, furtividade e itens)")
        print("3. Mago (Foco em Mana e Conhecimento, muitos feitiços)")
        print("4. Paladino (Foco em Saúde, Força e Carisma, magia divina)")
        print("5. Bardo (Foco em Carisma e Destreza, canções e habilidades variadas)")
        escolha = input("Escolha (1-5): ")
        if escolha == "1":
            jogador["classe"] = "Guerreiro"
            jogador["saude_max"] = 70
            jogador["saude"] = 70
            jogador["mana_max"] = 20
            jogador["mana"] = 20
            jogador["conhecimento"] = 5
            jogador["forca"] = 15
            jogador["destreza"] = 10
            jogador["carisma"] = 8
            jogador["feitiços"] = ["Golpe Forte"]
            jogador["habilidades"] = ["Ataque Poderoso"]
            print("Você se tornou um Guerreiro.")
        elif escolha == "2":
            jogador["classe"] = "Ladino"
            jogador["saude_max"] = 50
            jogador["saude"] = 50
            jogador["mana_max"] = 30
            jogador["mana"] = 30
            jogador["conhecimento"] = 15
            jogador["forca"] = 10
            jogador["destreza"] = 15
            jogador["carisma"] = 12
            jogador["inventario"].append("Kit de Ladrão")
            jogador["feitiços"] = ["Furtividade"]
            jogador["habilidades"] = ["Esconder nas Sombras"]
            print("Você se tornou um Ladino.")
        elif escolha == "3":
            jogador["classe"] = "Mago"
            jogador["saude_max"] = 40
            jogador["saude"] = 40
            jogador["mana_max"] = 90
            jogador["mana"] = 90
            jogador["conhecimento"] = 18
            jogador["forca"] = 8
            jogador["destreza"] = 12
            jogador["carisma"] = 10
            jogador["feitiços"] = ["Bola de Fogo", "Visão Mística"]
            jogador["habilidades"] = ["Meditação Arcana"]
            print("Você se tornou um Mago.")
        elif escolha == "4":
            jogador["classe"] = "Paladino"
            jogador["saude_max"] = 65
            jogador["saude"] = 65
            jogador["mana_max"] = 40
            jogador["mana"] = 40
            jogador["conhecimento"] = 10
            jogador["forca"] = 13
            jogador["destreza"] = 10
            jogador["carisma"] = 15
            jogador["feitiços"] = ["Cura Menor"]
            jogador["habilidades"] = ["Imposição de Mãos"]
            print("Você se tornou um Paladino.")
        elif escolha == "5":
            jogador["classe"] = "Bardo"
            jogador["saude_max"] = 55
            jogador["saude"] = 55
            jogador["mana_max"] = 50
            jogador["mana"] = 50
            jogador["conhecimento"] = 12
            jogador["forca"] = 10
            jogador["destreza"] = 13
            jogador["carisma"] = 16
            jogador["feitiços"] = ["Inspiração"]
            jogador["habilidades"] = ["Canção da Bravura"]
            print("Você se tornou um Bardo.")
        else:
            print("Escolha inválida. Tente novamente.")
    print(f"Nome: {jogador['nome']}, Classe: {jogador['classe']}, Saúde: {jogador['saude']}/{jogador['saude_max']}, Mana: {jogador['mana']}/{jogador['mana_max']}, Conhecimento: {jogador['conhecimento']}, Força: {jogador['forca']}, Destreza: {jogador['destreza']}, Carisma: {jogador['carisma']}, Feitiços: {jogador['feitiços']}, Habilidades: {jogador['habilidades']}, Inventário: {jogador['inventario']}")

# Sistema de níveis (adaptando para novas classes e habilidades)
def verificar_nivel():
    xp_requisitos = [80, 160, 240, 320]
    habilidades_por_nivel = {
        2: {"Guerreiro": "Defesa", "Ladino": "Golpe Oportunista", "Mago": "Escudo Arcano", "Paladino": "Aura Protetora", "Bardo": "Melodia Curativa"},
        3: {"Guerreiro": "Vitalidade", "Ladino": "Evasão", "Mago": "Potencializar Magia", "Paladino": "Julgamento", "Bardo": "Harmonia Inspiradora"},
        4: {"Guerreiro": "Ataque Extra", "Ladino": "Mestre das Armadilhas", "Mago": "Teletransporte", "Paladino": "Bênção Divina", "Bardo": "Contracanto"},
        5: {"Guerreiro": "Resistência", "Ladino": "Assassinar", "Mago": "Maestria Elemental", "Paladino": "Fúria Divina", "Bardo": "Balada Lendária"}
    }
    nivel_anterior = jogador["nivel"]
    for nivel, xp_req in enumerate(xp_requisitos, 1):
        if jogador["xp"] >= xp_req and jogador["nivel"] < nivel + 1:
            jogador["nivel"] = nivel + 1
            jogador["saude_max"] += 10
            jogador["saude"] = jogador["saude_max"]
            jogador["mana_max"] += 15
            jogador["mana"] = jogador["mana_max"]
            if nivel + 1 in habilidades_por_nivel and jogador["classe"] in habilidades_por_nivel[nivel + 1]:
                nova_habilidade = habilidades_por_nivel[nivel + 1][jogador["classe"]]
                jogador["habilidades"].append(nova_habilidade)
                print(f"Você aprendeu uma nova habilidade: {nova_habilidade}!")
    if jogador["nivel"] > nivel_anterior:
        print(f"Você alcançou o nível {jogador['nivel']}! Saúde e Mana aumentados.")

# Funções auxiliares
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
    print(f"Nível: {jogador['nivel']}")
    print(f"XP: {jogador['xp']}")
    print(f"Saúde: {jogador['saude']}/{jogador['saude_max']}")
    print(f"Mana: {jogador['mana']}/{jogador['mana_max']}")
    print(f"Conhecimento: {jogador['conhecimento']}")
    print(f"Força: {jogador['forca']}")
    print(f"Destreza: {jogador['destreza']}")
    print(f"Carisma: {jogador['carisma']}")
    print(f"Inventário: {jogador['inventario']}")
    print(f"Feitiços: {jogador['feitiços']}")
    print(f"Habilidades: {jogador['habilidades']}")
    print("-------------------------\n")

# Funções de cenas
def introducao(escolha):
    while True:
        print(f"""
Bem-vindo, {jogador['nome']}, aventureiro!
A cidade de Vaeloria clama por sua ajuda. Desaparecimentos assombram as ruas, e luzes estranhas brilham na Floresta Sombria.
Você chega aos portões da cidade. O que deseja fazer?
1. Ir ao Salão do Conselho
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
            print("Escolha inválida. Tente novamente.")

def salao_conselho(escolha):
    while True:
        print(f"""
No Salão do Conselho, o Lorde Regente e o Capitão da Guarda te recebem. O Regente explica: 'Os desaparecimentos começaram há semanas.'
1. Perguntar ao Regente sobre o culto (Conhecimento >= 15)
2. Falar com o Capitão sobre suspeitas (Conhecimento >= 10)
3. Aceitar a missão e partir
4. Salvar jogo
5. Carregar jogo
6. Mostrar Status
        """)
        escolha = input("Escolha (1-6): ")
        if escolha == "1":
            if jogador["conhecimento"] >= 15:
                print("O Regente sussurra: 'Há rumores de um culto nas ruínas.'")
                jogador["conhecimento"] += 5
                jogador["xp"] += 20
                verificar_nivel()
                exibir_cena("floresta_sombria")
                break
            else:
                print("Você não tem conhecimento suficiente para perguntar sobre isso.")
        elif escolha == "2":
            if jogador["conhecimento"] >= 10:
                print("O Capitão diz: 'Um conselheiro age estranho. Cuidado na floresta.'")
                jogador["inventario"].append("Dica do Traidor")
                jogador["xp"] += 15
                verificar_nivel()
                exibir_cena("floresta_sombria")
                break
            else:
                print("Você não tem conhecimento suficiente para entender as suspeitas do Capitão.")
        elif escolha == "3":
            jogador["inventario"].append("Mapa da Floresta")
            jogador["conhecimento"] += 5
            jogador["xp"] += 10
            verificar_nivel()
            exibir_cena("floresta_sombria")
            break
        elif escolha == "4":
            salvar_jogo()
        elif escolha == "5":
            carregar_jogo()
            break
        elif escolha == "6":
            mostrar_status()
        else:
            print("Escolha inválida. Tente novamente.")

def taverna(escolha):
    while True:
        print(f"""
Na taverna, um velho bêbado murmura sobre 'sombras que falam'. Um encapuzado te observa.
1. Confrontar o encapuzado
2. Falar com o bêbado (Conhecimento >= 10)
3. Sair da taverna
4. Usar Poção de Mana (se tiver)
5. Salvar jogo
6. Mostrar Status
        """)
        escolha = input("Escolha (1-6): ")
        if escolha == "1":
            print("O encapuzado foge, mas deixa cair um pingente.")
            jogador["inventario"].append("Pingente Misterioso")
            jogador["xp"] += 10
            verificar_nivel()
            exibir_cena("floresta_sombria")
            break
        elif escolha == "2":
            if jogador["conhecimento"] >= 10:
                print("O bêbado diz: 'Eles se reúnem nas ruínas antigas.'")
                jogador["conhecimento"] += 5
                jogador["xp"] += 20
                verificar_nivel()
                exibir_cena("floresta_sombria")
                break
            else:
                print("O bêbado parece confuso demais para conversar.")
        elif escolha == "3":
            exibir_cena("floresta_sombria")
            break
        elif escolha == "4":
            if "Poção de Mana" in jogador["inventario"]:
                jogador["mana"] = min(jogador["mana_max"], jogador["mana"] + 30)
                jogador["inventario"].remove("Poção de Mana")
                print("Você usou uma Poção de Mana, restaurando 30 de Mana.")
            else:
                print("Você não tem Poções de Mana.")
        elif escolha == "5":
            salvar_jogo()
        elif escolha == "6":
            mostrar_status()
        else:
            print("Escolha inválida. Tente novamente.")

def biblioteca(escolha):
    while True:
        print(f"""
Na biblioteca arcana, você encontra um tomo sobre magias proibidas.
1. Lançar Visão Mística (-10 Mana)
2. Continuar lendo o tomo
3. Sair da biblioteca
4. Usar Poção de Mana (se tiver)
5. Salvar jogo
6. Mostrar Status
        """)
        escolha = input("Escolha (1-6): ")
        if escolha == "1":
            if jogador["mana"] >= 10 and "Visão Mística" in jogador["feitiços"]:
                jogador["mana"] -= 10
                print("Você vê uma visão: um altar na floresta, pulsando com energia negra.")
                jogador["conhecimento"] += 10
                jogador["xp"] += 20
                verificar_nivel()
                exibir_cena("floresta_sombria")
                break
            elif "Visão Mística" not in jogador["feitiços"]:
                print("Você não conhece esse feitiço.")
            else:
                print("Mana insuficiente!")
        elif escolha == "2":
            print("O tomo menciona um culto antigo.")
            jogador["conhecimento"] += 5
            jogador["xp"] += 10
            verificar_nivel()
            exibir_cena("floresta_sombria")
            break
        elif escolha == "3":
            exibir_cena("floresta_sombria")
            break
        elif escolha == "4":
            if "Poção de Mana" in jogador["inventario"]:
                jogador["mana"] = min(jogador["mana_max"], jogador["mana"] + 30)
                jogador["inventario"].remove("Poção de Mana")
                print("Você usou uma Poção de Mana, restaurando 30 de Mana.")
            else:
                print("Você não tem Poções de Mana.")
        elif escolha == "5":
            salvar_jogo()
        elif escolha == "6":
            mostrar_status()
        else:
            print("Escolha inválida. Tente novamente.")

def evento_aleatorio(escolha):
    eventos = [
        ("Você encontra um baú encantado. Dentro, há uma Poção de Mana.", lambda: jogador["inventario"].append("Poção de Mana")),
        ("Uma armadilha mágica dispara! Você perde saúde.", lambda: jogador.update({"saude": max(0, jogador["saude"] - 12)})),
        ("Um viajante perdido te dá um Amuleto de Proteção.", lambda: jogador["inventario"].append("Amuleto de Proteção")),
        ("Um Corvo Necrótico ataca!", lambda: None, "combate_inimigos", {"nome": "Corvo Necrótico", "hp": 30, "dano": 12, "texto": "Um corvo necrótico voa em sua direção!", "fraqueza": ["Ilusão", "Raio Congelante"], "esquiva": 0.3})
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
        jogador["xp"] += 15
        verificar_nivel()
        if jogador["saude"] <= 0:
            fim_jogo("Você sucumbe aos ferimentos. Vaeloria está perdida.")
        else:
            exibir_cena("floresta_sombria")

def encontro_truidor(escolha):
    while True:
        print(f"""
Você encontra um conselheiro de Vaeloria, mas ele parece nervoso. Ele admite: 'Fui forçado a ajudar o culto!'
1. Convencê-lo a se redimir (Carisma >= 25)
2. Confrontá-lo
3. Deixá-lo ir
4. Salvar jogo
5. Mostrar Status
        """)
        escolha = input("Escolha (1-5): ")
        if escolha == "1":
            if jogador["carisma"] >= 25:
                print("O traidor concorda em ajudar, revelando o ponto fraco do líder do culto.")
                jogador["inventario"].append("Segredo do Culto")
                jogador["conhecimento"] += 10
                jogador["xp"] += 40
                verificar_nivel()
                exibir_cena("ruinas_antigas")
                break
            else:
                print("Você não consegue convencê-lo.")
        elif escolha == "2":
            print("O traidor entra em pânico e ativa uma armadilha mágica!")
            jogador["saude"] -= 15
            jogador["xp"] += 10
            verificar_nivel()
            if jogador["saude"] <= 0:
                fim_jogo("Você sucumbe à armadilha. Vaeloria está perdida.")
            else:
                exibir_cena("ruinas_antigas")
                break
        elif escolha == "3":
            print("O traidor foge, mas deixa um mapa parcial das ruínas.")
            jogador["inventario"].append("Mapa Parcial")
            jogador["xp"] += 15
            verificar_nivel()
            exibir_cena("ruinas_antigas")
            break
        elif escolha == "4":
            salvar_jogo()
        elif escolha == "5":
            mostrar_status()
        else:
            print("Escolha inválida. Tente novamente.")

def floresta_sombria(escolha):
    if random.random() < 0.4:
        if random.random() < 0.3 and "Dica do Traidor" in jogador["inventario"]:
            exibir_cena("encontro_truidor")
        else:
            evento_aleatorio(None)
        return
    while True:
        print(f"""
Mana: {jogador['mana']}/{jogador['mana_max']} | Saúde: {jogador['saude']}/{jogador['saude_max']} | Nível: {jogador['nivel']}
Inventário: {jogador['inventario']}
Você entra na Floresta Sombria. O ar é pesado, e sussurros ecoam.
1. Explorar uma trilha estreita
2. Lançar Visão Mística (-10 Mana)
3. Seguir um ruído estranho
4. Usar Poção de Mana (se tiver)
5. Salvar jogo
6. Mostrar Status
        """)
        escolha = input("Escolha (1-6): ")
        if escolha == "1":
            exibir_cena("combate_inimigos")
            break
        elif escolha == "2":
            if jogador["mana"] >= 10 and "Visão Mística" in jogador["feitiços"]:
                jogador["mana"] -= 10
                print("Visão Mística revela uma armadilha. Você encontra ruínas antigas.")
                jogador["conhecimento"] += 5
                jogador["xp"] += 20
                verificar_nivel()
                exibir_cena("ruinas_antigas")
                break
            elif "Visão Mística" not in jogador["feitiços"]:
                print("Você não conhece esse feitiço.")
            else:
                print("Mana insuficiente!")
        elif escolha == "3":
            exibir_cena("encontro_eremita")
            break
        elif escolha == "4":
            if "Poção de Mana" in jogador["inventario"]:
                jogador["mana"] = min(jogador["mana_max"], jogador["mana"] + 30)
                jogador["inventario"].remove("Poção de Mana")
                print("Você usou uma Poção de Mana, restaurando 30 de Mana.")
            else:
                print("Você não tem Poções de Mana.")
        elif escolha == "5":
            salvar_jogo()
        elif escolha == "6":
            mostrar_status()
        else:
            print("Escolha inválida. Tente novamente.")

def combate_inimigos(escolha):
    global inimigo_atual
    if escolha is None:
        inimigos = [
            {"nome": "Lobos Sombrios", "hp": 45, "dano": 10, "texto": "Dois lobos sombrios emergem, olhos brilhando.", "fraqueza": ["Bola de Fogo", "Raio Congelante"]},
            {"nome": "Espectros Arcanos", "hp": 35, "dano": 12, "texto": "Espectros flutuam, imunes a ataques físicos.", "fraqueza": ["Visão Mística", "Ilusão"]},
            {"nome": "Golem Corrompido", "hp": 75, "dano": 15, "texto": "Um golem avança, lento mas resistente.", "fraqueza": ["Ilusão"]}
        ]
        inimigo_atual = random.choice(inimigos)
        inimigo_atual["hp_atual"] = inimigo_atual["hp"]

    opcoes_combate = [f"{i+1}. Lançar {feitico} ({custo} Mana)" for i, (feitico, custo) in enumerate([
        ("Bola de Fogo", 20), ("Escudo Arcano", 20), ("Visão Mística", 10),
        ("Raio Congelante", 25), ("Ilusão", 15), ("Cura Menor", 15)
    ]) if feitico in jogador["feitiços"]] + [f"{len(jogador['feitiços'])+1}. Tentar fugir"]

    while inimigo_atual["hp_atual"] > 0 and jogador["saude"] > 0:
        print(f"\n--- Combate ---")
        print(f"{inimigo_atual['texto']}")
        print(f"Inimigo: {inimigo_atual['nome']} | HP: {inimigo_atual['hp_atual']}/{inimigo_atual['hp']}")
        mostrar_status()
        print("Escolha uma ação:")
        for opcao in opcoes_combate:
            print(opcao)
        escolha_combate = input(f"Escolha (1-{len(opcoes_combate)}): ")

        if escolha_combate.isdigit():
            escolha_index = int(escolha_combate) - 1
            if 0 <= escolha_index < len(opcoes_combate) - 1:
                feitico_escolhido = opcoes_combate[escolha_index].split(" (")[0].split(". ")[1].replace("Lançar ", "")
                custo = int(opcoes_combate[escolha_index].split("(")[1].split(" ")[0])

                if jogador["mana"] >= custo:
                    jogador["mana"] -= custo
                    dano = 0
                    if feitico_escolhido == "Bola de Fogo":
                        dano = 30 if feitico_escolhido in inimigo_atual["fraqueza"] else 15
                    elif feitico_escolhido == "Raio Congelante":
                        dano = 25 if feitico_escolhido in inimigo_atual["fraqueza"] else 10
                    elif feitico_escolhido == "Ilusão":
                        dano = 20 if feitico_escolhido in inimigo_atual["fraqueza"] else 5
                    elif feitico_escolhido == "Visão Mística":
                        dano = 10
                        jogador["conhecimento"] += 5
                    elif feitico_escolhido == "Cura Menor":
                        jogador["saude"] = min(jogador["saude_max"], jogador["saude"] + 20)
                        print("Você usou Cura Menor, restaurando sua saúde.")
                        dano = 0 # Cura não causa dano
                    elif feitico_escolhido == "Escudo Arcano":
                        print("Escudo Arcano reduz danos por 2 turnos!")
                        jogador["escudo_turnos"] = 2
                        dano = 0 # Escudo não causa dano
                    elif feitico_escolhido == "Golpe Forte":
                        dano = 20 + jogador["forca"] // 2
                    elif feitico_escolhido == "Furtividade":
                        print("Você tenta se esconder nas sombras...")
                        if random.random() < jogador["destreza"] / 20:
                            print("Você escapa do combate!")
                            return "ruinas_antigas" # Ou outra cena apropriada após fuga
                        else:
                            print("Você falha em se esconder!")
                            dano = 0
                    elif feitico_escolhido == "Inspiração":
                        print("Você inspira a si mesmo, aumentando ligeiramente seu próximo ataque.")
                        # Implementar efeito para o próximo turno, talvez uma variável temporária
                        dano = 0
                    elif feitico_escolhido == "Cura Menor": # Paladino
                        jogador["saude"] = min(jogador["saude_max"], jogador["saude"] + 25) # Cura ligeiramente maior
                        print("Você canaliza energia divina para curar suas feridas.")
                        dano = 0

                    if dano > 0:
                        if "esquiva" in inimigo_atual and random.random() < inimigo_atual["esquiva"]:
                            print(f"{inimigo_atual['nome']} esquiva seu ataque!")
                        else:
                            inimigo_atual["hp_atual"] -= dano
                            print(f"Você usou {feitico_escolhido}, causando {dano} de dano!")

                    if inimigo_atual["hp_atual"] <= 0:
                        print(f"Você derrotou {inimigo_atual['nome']}!")
                        jogador["vitorias"] += 1
                        jogador["xp"] += 40
                        verificar_nivel()
                        if random.random() < 0.6:
                            jogador["inventario"].append("Poção de Mana")
                            print("Você encontrou uma Poção de Mana!")
                        return "ruinas_antigas"

                    dano_inimigo = inimigo_atual["dano"]
                    if jogador["escudo_turnos"] > 0:
                        dano_inimigo //= 2
                        jogador["escudo_turnos"] -= 1
                    if "Amuleto de Proteção" in jogador["inventario"]:
                        dano_inimigo = int(dano_inimigo * 0.8)
                    jogador["saude"] -= dano_inimigo
                    print(f"{inimigo_atual['nome']} ataca, causando {dano_inimigo} de dano!")

                    if jogador["saude"] <= 0:
                        fim_jogo("Você sucumbe aos ferimentos. Vaeloria está perdida.")
                        return None # Fim de jogo

                else:
                    print("Mana insuficiente!")
            elif escolha_index == len(opcoes_combate) - 1:
                sorte = random.randint(1, 10)
                if sorte > 4:
                    print("Você escapa, mas se machuca na fuga.")
                    jogador["saude"] -= 8
                    return "ruinas_antigas"
                else:
                    print("Você não escapa e é atacado!")
                    dano_inimigo = inimigo_atual["dano"]
                    if jogador["escudo_turnos"] > 0:
                        dano_inimigo //= 2
                        jogador["escudo_turnos"] -= 1
                    if "Amuleto de Proteção" in jogador["inventario"]:
                        dano_inimigo = int(dano_inimigo * 0.8)
                    jogador["saude"] -= dano_inimigo
                    print(f"{inimigo_atual['nome']} ataca, causando {dano_inimigo} de dano!")
                    if jogador["saude"] <= 0:
                        fim_jogo("Você sucumbe aos ferimentos. Vaeloria está perdida.")
                        return None # Fim de jogo
            else:
                print("Escolha inválida.")
        else:
            print("Entrada inválida.")

    return jogador["cena_atual"] # Se o loop terminar sem condições de vitória/derrota

def encontro_eremita(escolha):
    while True:
        print(f"""
Você encontra uma eremita idosa. Ela diz: 'O culto tenta ressuscitar um mago negro.'
1. Perguntar sobre o ritual (Conhecimento >= 20)
2. Pedir ajuda
3. Convencê-la a lutar no clímax (Carisma >= 15)
4. Partir
5. Salvar jogo
6. Mostrar Status
        """)
        escolha = input("Escolha (1-6): ")
        if escolha == "1":
            if jogador["conhecimento"] >= 20:
                print("A eremita revela: 'O ritual pode ser selado com um pergaminho.'")
                jogador["inventario"].append("Pergaminho de Selamento")
                jogador["conhecimento"] += 10
                jogador["xp"] += 30
                verificar_nivel()
                exibir_cena("ruinas_antigas")
                break
            else:
                print("A eremita parece relutante em compartilhar mais informações.")
        elif escolha == "2":
            print("A eremita te dá um Amuleto de Proteção.")
            jogador["inventario"].append("Amuleto de Proteção")
            jogador["xp"] += 10
            verificar_nivel()
            exibir_cena("ruinas_antigas")
            break
        elif escolha == "3":
            if jogador["carisma"] >= 15:
                print("A eremita concorda em ajudar no clímax, mas sua vida estará em risco.")
                jogador["inventario"].append("Aliada Eremita")
                jogador["xp"] += 25
                verificar_nivel()
                exibir_cena("ruinas_antigas")
                break
            else:
                print("A eremita não parece convencida a lutar.")
        elif escolha == "4":
            exibir_cena("ruinas_antigas")
            break
        elif escolha == "5":
            salvar_jogo()
        elif escolha == "6":
            mostrar_status()
        else:
            print("Escolha inválida. Tente novamente.")

def ruinas_antigas(escolha):
    while True:
        print(f"""
Mana: {jogador['mana']}/{jogador['mana_max']} | Saúde: {jogador['saude']}/{jogador['saude_max']} | Nível: {jogador['nivel']}
Inventário: {jogador['inventario']}
Você chega às ruínas antigas. Um Guardião Rúnico bloqueia o caminho.
1. Combater o Guardião
2. Usar Visão Mística para evitar o Guardião (-10 Mana)
3. Usar Poção de Mana (se tiver)
4. Usar Cura Menor (-15 Mana, se disponível)
5. Salvar jogo
6. Mostrar Status
        """)
        escolha = input("Escolha (1-6):
        if escolha == "1":
            global inimigo_atual
            inimigo_atual = {"nome": "Guardião Rúnico", "hp": 70, "dano": 18, "texto": "O Guardião Rúnico, feito de pedra e magia, se move!", "fraqueza": ["Golpe Forte", "Fúria"], "esquiva": 0.1}
            exibir_cena("combate_inimigos")
            break
        elif escolha == "2":
            if jogador["mana"] >= 10 and "Visão Mística" in jogador["feitiços"]:
                jogador["mana"] -= 10
                print("Visão Mística revela uma passagem secreta. Você evita o Guardião.")
                jogador["conhecimento"] += 10
                jogador["xp"] += 30
                verificar_nivel()
                exibir_cena("altar_sacrificio")
                break
            elif "Visão Mística" not in jogador["feitiços"]:
                print("Você não conhece esse feitiço.")
            else:
                print("Mana insuficiente!")
        elif escolha == "3":
            if "Poção de Mana" in jogador["inventario"]:
                jogador["mana"] = min(jogador["mana_max"], jogador["mana"] + 30)
                jogador["inventario"].remove("Poção de Mana")
                print("Você usou uma Poção de Mana, restaurando 30 de Mana.")
            else:
                print("Você não tem Poções de Mana.")
        elif escolha == "4":
            if jogador["mana"] >= 15 and "Cura Menor" in jogador["feitiços"]:
                jogador["mana"] -= 15
                jogador["saude"] = min(jogador["saude_max"], jogador["saude"] + 20)
                print("Você usou Cura Menor, restaurando sua saúde.")
            elif "Cura Menor" not in jogador["feitiços"]:
                print("Você não conhece esse feitiço.")
            else:
                print("Mana insuficiente!")
        elif escolha == "5":
            salvar_jogo()
        elif escolha == "6":
            mostrar_status()
        else:
            print("Escolha inválida. Tente novamente.")

def altar_sacrificio(escolha):
    global sacerdote_vivo, sacerdote
    if sacerdote is None:
        sacerdote = {"nome": "Sumo Sacerdote", "hp": 100, "mana": 80, "dano_magico": 25, "texto": "O Sumo Sacerdote do culto está realizando o ritual!", "fraqueza": ["Segredo do Culto", "Balada Lendária"]}
        sacerdote_vivo = True

    while sacerdote_vivo and jogador["saude"] > 0:
        print(f"\n--- Altar de Sacrifício ---")
        print(f"{sacerdote['texto']} HP: {sacerdote['hp']}/{100}, Mana: {sacerdote['mana']}/{80}")
        mostrar_status()
        opcoes_climax = [f"{i+1}. Lançar {feitico} ({custo} Mana)" for i, (feitico, custo) in enumerate([
            ("Bola de Fogo", 20), ("Raio Congelante", 25), ("Ilusão", 15), ("Visão Mística", 10), ("Cura Menor", 15)
        ]) if feitico in jogador["feitiços"]] + ["{}. Tentar selar o ritual (Pergaminho de Selamento)".format(len(jogador['feitiços']) + 1)]

        if "Aliada Eremita" in jogador["inventario"]:
            opcoes_climax.append("{}. Pedir ajuda à Eremita".format(len(opcoes_climax) + 1))

        opcoes_climax.append("{}. Fugir".format(len(opcoes_climax) + 1))
        opcoes_climax.append("{}. Salvar jogo".format(len(opcoes_climax) + 1))
        opcoes_climax.append("{}. Mostrar Status".format(len(opcoes_climax) + 1))

        escolha_climax = input(f"Escolha (1-{len(opcoes_climax)}): ")

        if escolha_climax.isdigit():
            escolha_index = int(escolha_climax) - 1
            num_feitiços = len(jogador['feitiços'])

            if 0 <= escolha_index < num_feitiços:
                feitico_escolhido = [f for f in jogador['feitiços']][escolha_index]
                custo = [20 if f == "Bola de Fogo" else 25 if f == "Raio Congelante" else 15 if f == "Ilusão" else 10 if f == "Visão Mística" else 15 for f in jogador['feitiços']][escolha_index]

                if jogador["mana"] >= custo:
                    jogador["mana"] -= custo
                    dano_jogador = 0
                    if feitico_escolhido == "Bola de Fogo":
                        dano_jogador = 35 if "Segredo do Culto" in jogador["inventario"] else 20
                    elif feitico_escolhido == "Raio Congelante":
                        dano_jogador = 30 if "Segredo do Culto" in jogador["inventario"] else 15
                    elif feitico_escolhido == "Ilusão":
                        dano_jogador = 25
                    elif feitico_escolhido == "Visão Mística":
                        dano_jogador = 15
                        jogador["conhecimento"] += 5
                    elif feitico_escolhido == "Cura Menor":
                        jogador["saude"] = min(jogador["saude_max"], jogador["saude"] + 25)
                        print("Você usou Cura Menor, restaurando sua saúde.")
                        dano_jogador = 0
                    elif feitico_escolhido == "Golpe Forte":
                        dano_jogador = 25 + jogador["forca"]
                    elif feitico_escolhido == "Inspiração":
                        # Implementar efeito para o próximo ataque
                        print("Você se sente mais inspirado!")
                        dano_jogador = 0
                    elif feitico_escolhido == "Balada Lendária":
                        dano_jogador = 50
                        print("Sua balada ressoa com poder!")

                    if dano_jogador > 0:
                        sacerdote["hp"] -= dano_jogador
                        print(f"Você usou {feitico_escolhido}, causando {dano_jogador} de dano!")

                else:
                    print("Mana insuficiente!")

            elif escolha_index == num_feitiços: # Tentar selar
                if "Pergaminho de Selamento" in jogador["inventario"]:
                    print("Você lê o pergaminho antigo. O ritual é desfeito! O mago negro não renascerá.")
                    fim_jogo("Vitória! Vaeloria está salva.")
                    break
                else:
                    print("Você não tem o pergaminho de selamento!")

            elif "Aliada Eremita" in jogador["inventario"] and escolha_index == num_feitiços + 1:
                print("A eremita ataca o sacerdote com magia ancestral!")
                dano_eremita = random.randint(20, 40)
                sacerdote["hp"] -= dano_eremita
                print(f"A eremita causa {dano_eremita} de dano!")
                if random.random() < 0.3:
                    print("A eremita é gravemente ferida!")
                    jogador["inventario"].remove("Aliada Eremita")

            elif escolha_index == num_feitiços + (2 if "Aliada Eremita" in jogador["inventario"] else 1): # Fugir
                print("Você tenta fugir do altar...")
                sorte_fuga = random.randint(1, 10)
                if sorte_fuga > 3:
                    print("Você consegue escapar das ruínas.")
                    exibir_cena("floresta_sombria") # Ou outra cena de fuga
                    break
                else:
                    print("Você não consegue fugir!")

            elif escolha_index == num_feitiços + (3 if "Aliada Eremita" in jogador["inventario"] else 2): # Salvar
                salvar_jogo()
            elif escolha_index == num_feitiços + (4 if "Aliada Eremita" in jogador["inventario"] else 3): # Status
                mostrar_status()
            else:
                print("Escolha inválida.")

            if sacerdote["hp"] > 0:
                feitico_sacerdote = random.choice(["Raio Sombrio", "Drenar Vida"])
                dano_sacerdote = sacerdote["dano_magico"]
                if feitico_sacerdote == "Drenar Vida":
                    cura_sacerdote = random.randint(10, 20)
                    sacerdote["hp"] = min(100, sacerdote["hp"] + cura_sacerdote)
                    dano_sacerdote = random.randint(15, 25)
                    jogador["saude"] -= dano_sacerdote
                    print(f"O Sumo Sacerdote lança Drenar Vida, curando-se em {cura_sacerdote} e causando {dano_sacerdote} de dano!")
                else:
                    jogador["saude"] -= dano_sacerdote
                    print(f"O Sumo Sacerdote lança Raio Sombrio, causando {dano_sacerdote} de dano!")

                if jogador["saude"] <= 0:
                    fim_jogo("Você foi derrotado pelo Sumo Sacerdote. O mago negro renasceu.")
                    sacerdote_vivo = False

            if sacerdote["hp"] <= 0:
                print("O Sumo Sacerdote cai! O ritual é interrompido.")
                fim_jogo("Vitória! O culto foi desmantelado.")
                sacerdote_vivo = False
        else:
            print("Entrada inválida.")
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
    "encontro_truidor": encontro_truidor
}

# Iniciar o jogo
escolher_classe()
exibir_cena("introducao")
