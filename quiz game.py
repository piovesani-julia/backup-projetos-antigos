import random

# ============================================================
#  QUIZ DE JOGOS  🎮
# ============================================================

perguntas = [
    {
        "pergunta": "Em qual jogo o personagem principal se chama Geralt de Rívia?",
        "opcoes": ["The Witcher 3", "Dragon Age", "Dark Souls", "Skyrim"],
        "resposta": 0,
    },
    {
        "pergunta": "Qual empresa criou o Minecraft?",
        "opcoes": ["EA Games", "Mojang", "Ubisoft", "Bethesda"],
        "resposta": 1,
    },
    {
        "pergunta": "Em qual ano foi lançado o primeiro GTA (Grand Theft Auto)?",
        "opcoes": ["1995", "2001", "1997", "1999"],
        "resposta": 2,
    },
    {
        "pergunta": "Qual desses personagens pertence ao jogo Super Mario Bros?",
        "opcoes": ["Link", "Sonic", "Bowser", "Mega Man"],
        "resposta": 2,
    },
    {
        "pergunta": "No jogo Among Us, qual é o objetivo dos impostores?",
        "opcoes": [
            "Completar tarefas",
            "Eliminar tripulantes sem ser descoberto",
            "Fugir da nave",
            "Consertar o reator",
        ],
        "resposta": 1,
    },
    {
        "pergunta": "Qual jogo ficou famoso pela frase 'It's dangerous to go alone! Take this.'?",
        "opcoes": ["Pokémon Red", "The Legend of Zelda", "Final Fantasy", "Metroid"],
        "resposta": 1,
    },
    {
        "pergunta": "Em League of Legends, como se chama o mapa principal?",
        "opcoes": ["Summoner's Rift", "Crystal Scar", "Howling Abyss", "Twisted Treeline"],
        "resposta": 0,
    },
    {
        "pergunta": "Qual é o nome do protagonista de The Last of Us?",
        "opcoes": ["Nathan Drake", "Joel", "Ellie", "Marcus Fenix"],
        "resposta": 1,
    },
    {
        "pergunta": "Em qual jogo você captura criaturas selvagens com Pokébolas?",
        "opcoes": ["Digimon World", "Monster Hunter", "Pokémon", "Temtem"],
        "resposta": 2,
    },
    {
        "pergunta": "Qual desses jogos é um battle royale?",
        "opcoes": ["FIFA 24", "Stardew Valley", "Fortnite", "The Sims 4"],
        "resposta": 2,
    },
]


def exibir_separador():
    print("-" * 50)


def exibir_titulo():
    print("=" * 50)
    print("          🎮  QUIZ DE JOGOS  🎮")
    print("=" * 50)


def fazer_pergunta(numero, total, item):
    exibir_separador()
    print(f"Pergunta {numero}/{total}")
    print(f"\n{item['pergunta']}\n")

    for i, opcao in enumerate(item["opcoes"]):
        print(f"  {i + 1}. {opcao}")

    print()

    while True:
        entrada = input("Sua resposta (1-4): ").strip()
        if entrada in ("1", "2", "3", "4"):
            return int(entrada) - 1
        print("  Digite apenas 1, 2, 3 ou 4.")


def avaliar_resultado(pontuacao, total):
    percentual = pontuacao / total

    exibir_separador()
    print(f"\n  Você acertou {pontuacao} de {total} perguntas!\n")

    if percentual == 1.0:
        print("  🏆  LENDÁRIO! Você é um mestre dos games!")
    elif percentual >= 0.7:
        print("  🥇  VETERANO! Você manja bastante de jogos.")
    elif percentual >= 0.4:
        print("  🎯  INICIANTE! Nada mal, continue jogando.")
    else:
        print("  🕹️  NOVATO! Continue jogando e aprendendo!")

    print()
    exibir_separador()


def jogar():
    exibir_titulo()
    print("\nBem-vindo ao Quiz de Jogos!")
    print("Responda cada pergunta digitando o número da opção.\n")

    embaralhar = input("Embaralhar a ordem das perguntas? (s/n): ").strip().lower()
    lista = perguntas[:]
    if embaralhar == "s":
        random.shuffle(lista)

    pontuacao = 0
    total = len(lista)

    for i, item in enumerate(lista, start=1):
        escolha = fazer_pergunta(i, total, item)
        correta = item["resposta"]

        if escolha == correta:
            print("\n  ✅  Correto!")
            pontuacao += 1
        else:
            print(f"\n  ❌  Errado! A resposta certa era: {item['opcoes'][correta]}")

    avaliar_resultado(pontuacao, total)

    jogar_novamente = input("Jogar novamente? (s/n): ").strip().lower()
    if jogar_novamente == "s":
        jogar()
    else:
        print("\nObrigado por jogar! Até a próxima! 🎮\n")


# Ponto de entrada
if __name__ == "__main__":
    jogar()