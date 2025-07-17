def introducao():
    """Exibe a introdução do jogo e a premissa."""
    print("Bem-vindo a Ecos de Eldoria, um RPG de texto ambientado em um reino de fantasia medieval!")
    print("\nNeste jogo, você é um aventureiro em Eldoria, uma terra outrora pacífica, agora ameaçada pela Sombra do Rei Lich, Necros.")
    print("Sua missão é deter Necros e libertar o reino, enfrentando escolhas que levarão a diferentes destinos: glória, ruína ou um futuro incerto.")
    print("\nPrepare-se para sua jornada em um mundo de magia, monstros e bravura...")
    print("-" * 60) # Linha divisória para separar seções

def escolher_classe():
    """Permite ao jogador escolher uma classe e retorna a classe selecionada."""
    classes_validas = {
        "1": "Guerreiro (Força Bruta)",
        "2": "Mago (Arcano Dominante)",
        "3": "Arqueiro (Precisão Letal)",
        "4": "Ladino (Discrição Mortal)",
        "5": "Bardo (Charme Persuasivo)"
    }

    while True:
        print("\nEscolha sua classe:")
        for key, value in classes_validas.items():
            print(f"{key} - {value}")

        escolha = input("Digite o número da sua classe: ").strip()

        if escolha in classes_validas:
            print(f"\nVocê escolheu: {classes_validas[escolha]}!")
            return classes_validas[escolha]
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 5.")

def capitulo_um(classe):
    """Primeiro capítulo da aventura, com escolhas iniciais baseadas na classe."""
    print("\n" + "=" * 60)
    print("CAPÍTULO 1: O Chamado de Vilarejo Sereno")
    print("=" * 60)
    print(f"\nComo um(a) {classe}, você ouve os clamores do Vilarejo Sereno, assolado por criaturas sombrias, arautos de Necros.")
    print("Boatos de rituais profanos se espalham, e a necessidade de agir é iminente.")

    if "Guerreiro" in classe:
        print("\nSua força e coragem são inegáveis. Você pode atacar diretamente o acampamento de criaturas ou proteger a milícia local.")
        print("1 - Atacar Acampamento de Criaturas")
        print("2 - Proteger e Treinar a Milícia Local")
        escolha = input("O que você faz? ").strip()
        return escolha
    elif "Mago" in classe:
        print("\nSeu conhecimento arcano é sua maior arma. Você pode buscar tomos antigos de magia ou conjurar um escudo protetor para o vilarejo.")
        print("1 - Buscar Tomos Antigos de Magia")
        print("2 - Conjurar Escudo Mágico para o Vilarejo")
        escolha = input("O que você faz? ").strip()
        return escolha
    elif "Arqueiro" in classe:
        print("\nSua precisão é lendária. Você pode se esgueirar para uma posição elevada e eliminar alvos-chave ou armar armadilhas estratégicas.")
        print("1 - Eliminar Alvos-Chave Inimigos")
        print("2 - Armar Armadilhas Estratégicas")
        escolha = input("O que você faz? ").strip()
        return escolha
    elif "Ladino" in classe:
        print("\nSua astúcia e discrição são suas maiores vantagens. Você pode roubar informações dos inimigos ou infiltrar-se em suas linhas para sabotagem.")
        print("1 - Roubar Planos Inimigos")
        print("2 - Infiltrar e Sabotar as Defesas Inimigas")
        escolha = input("O que você faz? ").strip()
        return escolha
    elif "Bardo" in classe:
        print("\nSua música e lábia podem mover corações. Você pode inspirar os aldeões a lutar ou tentar negociar com os líderes das criaturas.")
        print("1 - Inspirar os Aldeões com Canções de Bravura")
        print("2 - Tentar Negociar com os Líderes Inimigos")
        escolha = input("O que você faz? ").strip()
        return escolha
    return "0" # Retorna "0" caso a classe não se encaixe nas condições

def resultado_capitulo_um(classe, escolha):
    """Determina o resultado do Capítulo 1 e retorna um status para o próximo capítulo."""
    if "Guerreiro" in classe:
        if escolha == "1":
            print("\nVocê lidera um ataque feroz ao acampamento. Muitos caem, mas você obtém informações sobre a localização do covil de Necros.")
            return "informacao_covil"
        elif escolha == "2":
            print("\nVocê treina a milícia, transformando camponeses em defensores. O vilarejo resiste, e sua fama se espalha, atraindo aliados.")
            return "aliados_fama"
    elif "Mago" in classe:
        if escolha == "1":
            print("\nVocê mergulha em ruínas esquecidas e encontra tomos que revelam um ritual antigo capaz de enfraquecer Necros.")
            return "ritual_enfraquecer"
        elif escolha == "2":
            print("\nSeu escudo mágico protege o vilarejo, afastando as criaturas. Os aldeões ficam seguros, e você ganha tempo para investigar.")
            return "tempo_investigar"
    elif "Arqueiro" in classe:
        if escolha == "1":
            print("\nDe longe, você elimina os líderes das criaturas, desorganizando suas forças. O avanço inimigo é contido.")
            return "inimigo_contido"
        elif escolha == "2":
            print("\nSuas armadilhas decimam as hordas. A rota de ataque inimiga é comprometida, forçando-os a recuar e buscar nova rota.")
            return "rota_comprometida"
    elif "Ladino" in classe:
        if escolha == "1":
            print("\nVocê se infiltra e rouba planos de Necros, descobrindo um ponto fraco em sua guarda pessoal.")
            return "ponto_fraco_necros"
        elif escolha == "2":
            print("\nSua sabotagem causa caos nas linhas inimigas. Equipamentos são destruídos, e a moral deles despenca.")
            return "moral_inimiga_baixa"
    elif "Bardo" in classe:
        if escolha == "1":
            print("\nSuas canções infundem coragem nos aldeões, que resistem bravamente. Eles agora confiam em você para guiá-los.")
            return "aldeões_confiam"
        elif escolha == "2":
            print("\nCom sua lábia, você convence os líderes das criaturas a recuarem, mas percebe que a verdadeira ameaça é Necros.")
            return "ameaca_realizada"
    
    print("\nSuas escolhas levaram a um beco sem saída. A Sombra de Necros avança sem oposição.")
    return "derrota" # Caso a escolha seja inválida ou leve a um resultado neutro/ruim

def capitulo_dois(status_anterior):
    """Segundo capítulo da aventura, influenciado pelas ações anteriores."""
    print("\n" + "=" * 60)
    print("CAPÍTULO 2: O Caminho para a Cidadela Sombria")
    print("=" * 60)

    if status_anterior == "informacao_covil":
        print("\nCom a localização do covil de Necros, você se prepara para o ataque final. É uma caverna escura e infestada.")
        print("Você pode invadir diretamente a caverna para um confronto brutal ou tentar encontrar uma entrada secreta.")
        print("1 - Invasão Direta")
        print("2 - Buscar Entrada Secreta")
        escolha = input("Como você entra no covil? ").strip()
        return escolha
    elif status_anterior == "aliados_fama":
        print("\nSeus novos aliados estão prontos para a batalha contra Necros, mas a moral deles depende de um líder forte.")
        print("Você pode liderar uma carga frontal, inspirando todos, ou usar seus aliados para uma tática de cerco prolongado.")
        print("1 - Liderar Carga Frontal")
        print("2 - Tática de Cerco Prolongado")
        escolha = input("Como você usa seus aliados? ").strip()
        return escolha
    elif status_anterior == "ritual_enfraquecer":
        print("\nO ritual arcano pode enfraquecer Necros, mas exige tempo e concentração em um local de poder místico.")
        print("Você pode realizar o ritual rapidamente e enfrentar Necros enfraquecido ou preparar o ritual em segredo para uma vantagem total.")
        print("1 - Realizar Ritual Rápido")
        print("2 - Preparar Ritual em Segredo")
        escolha = input("Qual sua estratégia arcana? ").strip()
        return escolha
    elif status_anterior == "tempo_investigar":
        print("\nCom o vilarejo seguro, você investigou e descobriu uma relíquia antiga que pode selar Necros, mas está bem guardada.")
        print("Você pode tentar furtar a relíquia com discrição ou lutar para obtê-la à força.")
        print("1 - Furtar a Relíquia")
        print("2 - Lutar pela Relíquia")
        escolha = input("Como você adquire a relíquia? ").strip()
        return escolha
    elif status_anterior == "inimigo_contido":
        print("\nO avanço inimigo foi contido, mas Necros está furioso e enviou suas tropas de elite. É hora de um confronto decisivo.")
        print("Você pode emboscar as tropas de elite ou atrair Necros para uma batalha campal onde suas habilidades são superiores.")
        print("1 - Emboscar Tropas de Elite")
        print("2 - Atrair Necros para Batalha Campal")
        escolha = input("Qual sua tática de combate? ").strip()
        return escolha
    elif status_anterior == "rota_comprometida":
        print("\nAs armadilhas comprometeram as rotas principais de Necros, mas ele está usando passagens subterrâneas. Você precisa interceptá-lo.")
        print("Você pode esperar por ele em uma saída crucial ou ir atrás dele nas passagens escuras.")
        print("1 - Esperar em Saída Crucial")
        print("2 - Perseguir nas Passagens Subterrâneas")
        escolha = input("Como você intercepta Necros? ").strip()
        return escolha
    elif status_anterior == "ponto_fraco_necros":
        print("\nVocê descobriu um ponto fraco na guarda de Necros, mas explorá-lo exige precisão e uma distração bem orquestrada.")
        print("Você pode usar o ponto fraco para um ataque surpresa ou criar uma distração massiva para quebrar sua defesa.")
        print("1 - Ataque Surpresa no Ponto Fraco")
        print("2 - Criar Distração Massiva")
        escolha = input("Qual sua estratégia de infiltração? ").strip()
        return escolha
    elif status_anterior == "moral_inimiga_baixa":
        print("\nA moral do inimigo está em frangalhos, mas Necros ainda é uma força a ser temida. É a hora de desferir o golpe final.")
        print("Você pode incitar uma revolta entre os soldados de Necros ou atacar diretamente seu santuário enquanto ele está vulnerável.")
        print("1 - Incitar Revolta entre os Soldados")
        print("2 - Atacar Santuário de Necros")
        escolha = input("Como você finaliza a batalha? ").strip()
        return escolha
    elif status_anterior == "aldeões_confiam":
        print("\nOs aldeões estão prontos para lutar ao seu lado, mas não são soldados experientes. Você precisa de uma tática que minimize perdas.")
        print("Você pode liderar um ataque de guerrilha, usando o conhecimento local, ou organizar uma defesa forte, esperando Necros atacar.")
        print("1 - Liderar Ataque de Guerrilha com Aldeões")
        print("2 - Organizar Defesa Forte do Vilarejo")
        escolha = input("Qual sua tática com os aldeões? ").strip()
        return escolha
    elif status_anterior == "ameaca_realizada":
        print("\nVocê percebeu que Necros é a verdadeira ameaça. Ele está no centro do poder das criaturas. Você deve confrontá-lo.")
        print("Você pode tentar um confronto direto e dramático, ou usar sua lábia para expor as mentiras de Necros aos seus seguidores.")
        print("1 - Confronto Direto com Necros")
        print("2 - Expor as Mentiras de Necros para seus Seguidores")
        escolha = input("Como você o enfrenta? ").strip()
        return escolha
    
    return "0" # Caso um status_anterior inesperado chegue aqui

def final(classe, status_anterior, escolha_final):
    """Determina e exibe um dos três finais possíveis: Glória, Ruína ou Futuro Incerto."""
    print("\n" + "=" * 60)
    print("O DESTINO DE ELDORIA")
    print("=" * 60)

    # Lógica para o Final de Glória
    if ("Guerreiro" in classe and status_anterior == "informacao_covil" and escolha_final == "1") or \
       ("Mago" in classe and status_anterior == "ritual_enfraquecer" and escolha_final == "2") or \
       ("Arqueiro" in classe and status_anterior == "inimigo_contido" and escolha_final == "1") or \
       ("Ladino" in classe and status_anterior == "ponto_fraco_necros" and escolha_final == "1") or \
       ("Bardo" in classe and status_anterior == "ameaca_realizada" and escolha_final == "2"):
        print("\nCom bravura e estratégia, você derrota o Rei Lich Necros e liberta Eldoria de sua escuridão!")
        print("Os reinos o aclamam como um verdadeiro herói. A paz retorna, e lendas são cantadas sobre seus feitos.")
        print("\nFINAL DE GLÓRIA: Seu nome ecoa pelos séculos. Eldoria está salva.")
        return "gloria"
    
    # Lógica para o Final de Ruína
    elif ("Guerreiro" in classe and status_anterior == "aliados_fama" and escolha_final == "2") or \
         ("Mago" in classe and status_anterior == "tempo_investigar" and escolha_final == "2") or \
         ("Arqueiro" in classe and status_anterior == "rota_comprometida" and escolha_final == "2") or \
         ("Ladino" in classe and status_anterior == "moral_inimiga_baixa" and escolha_final == "1") or \
         ("Bardo" in classe and status_anterior == "aldeões_confiam" and escolha_final == "2"):
        print("\nSuas táticas falham, ou o poder de Necros se mostra invencível. Eldoria sucumbe à escuridão.")
        print("O reino é consumido pelo caos, e seu nome se torna um lamento nas histórias de derrota.")
        print("\nFINAL DE RUÍNA: A escuridão prevaleceu. A esperança se perdeu.")
        return "ruina"

    # Lógica para o Final de Futuro Incerto
    else:
        print("\nVocê consegue deter Necros, mas a um custo elevado, ou o futuro de Eldoria permanece incerto.")
        print("Vitórias parciais ou sacrifícios deixam cicatrizes no reino. A luta por um futuro verdadeiramente pacífico continua.")
        print("\nFINAL DE FUTURO INCERTO: A ameaça imediata foi superada, mas a paz ainda é frágil.")
        return "incerto"

def jogar_novamente():
    """Pergunta ao jogador se deseja jogar novamente."""
    while True:
        resposta = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if resposta == "s":
            return True
        elif resposta == "n":
            return False
        else:
            print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")

# --- Loop Principal do Jogo ---
if __name__ == "__main__":
    while True:
        introducao()
        
        classe_escolhida = escolher_classe()
        
        # O Capítulo 1 retorna uma escolha que determinará o 'status_cap_1'
        escolha_cap_1 = capitulo_um(classe_escolhida)
        # O 'resultado_capitulo_um' pega a classe e a escolha para gerar um novo 'status' para o próximo capítulo
        status_cap_2 = resultado_capitulo_um(classe_escolhida, escolha_cap_1)
        
        # Se o resultado do capítulo 1 foi uma "derrota", o jogo para ou reinicia
        if status_cap_2 == "derrota":
            print("\nSeus esforços foram em vão no primeiro confronto. Necros consolidou seu poder.")
            if not jogar_novamente():
                break
            else:
                continue # Reinicia o loop principal do jogo
        
        # O Capítulo 2 usa o 'status_cap_2' para apresentar novas escolhas e retorna a escolha final
        escolha_final = capitulo_dois(status_cap_2)
        
        # Se a escolha final foi "0", indica um caminho inesperado ou derrota no cap 2
        if escolha_final == "0":
            print("\nSuas últimas ações não foram suficientes para deter Necros. Eldoria caiu na escuridão.")
            if not jogar_novamente():
                break
            else:
                continue

        # O final do jogo é determinado pela classe, status anterior e escolha final
        final_jogo = final(classe_escolhida, status_cap_2, escolha_final)
        
        # Pergunta se o jogador quer jogar novamente
        if not jogar_novamente():
            break

    print("\nObrigado por jogar Ecos de Eldoria!")
