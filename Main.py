#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Aluno Lorenzzo Deboni


# Importando as biblioteceas externas 
from random import randint

# definindo as funções.
def pegarDadosVerde():
    return ("C", "P", "C", "T", "P", "C")

def pegarDadosAmarelo():
    return ("T", "P", "C", "T", "P", "C")

def pegarDadosVermelhos():
    return ("T", "P", "T", "C", "P", "T")

def initCopo(copo):
    # colocar dados verdes no copo
    for i in range(0, 6):
        copo.append(pegarDadosVerde())

        # colocar dados amarelos no copo
    for i in range(0, 4):
        copo.append(pegarDadosAmarelo())

    # colocar dados vermelhos no copo
    for i in range(0, 3):
        copo.append(pegarDadosVermelhos())

        return copo

def pegarDadosCopo(copo):
    # Quantidade de dados no copo
    if len(copo) != 0:
        numDados = (len(copo) - 1)
        index = randint(0, numDados)
        dado = copo[index]
        del (copo[index])
        return dado, copo
    else:
        print("Copo Vazio!!")
        return -1, copo

def lancarDado(dado):
    faceDado = randint(0, 5)
    if dado[faceDado] == "C":
            print("Cerebro!!!")
            return 'C'
    elif dado[faceDado] == "T":
            print("Tiro!!!")
            return 'T'
    else:
            print("Passos!!!")
            return 'P'

def mostrarDadosCopo(copo):
    listDado = []
    for dado in copo:
        if dado == ("C", "P", "C", "T", "P", "C"):
                listDado.append("verde")
        elif dado == ("T", "P", "C", "T", "P", "C"):
                listDado.append("amarelo")
        else:
                listDado.append("vermelho")
                print(listDado)

def mostrarDado(dado):
    if dado == ("C", "P", "C", "T", "P", "C"):
        print("verde")
    elif dado == ("T", "P", "C", "T", "P", "C"):
        print("amarelo")
    else:
        print("vermelho")

def verificarScore(primeiro, segundo, terceiro):
    tiro = 0
    cerebro = 0
    passos = 0
    # primeiro dado
    if primeiro == "C":
        cerebro += 1
    elif primeiro == "T":
        tiro += 1
    else:
        passos += 1

    # segundo dado
    if segundo == "C":
        cerebro += 1
    elif segundo == "T":
        tiro += 1
    else:
        passos += 1

    # terceiro dado
    if terceiro == "C":
        cerebro += 1
    elif terceiro == "T":
        tiro += 1
    else:
        passos += 1
    return cerebro, tiro, passos

#Apresentação do jogo
print("Bem vindos ao zombie dice!!")

# Iniciando o código
copo = []
copo = initCopo(copo)
jogadores = []

# Verificando quantidade de jogadores
while True:
    qnt_jogadores = int(input('Insira a quantidade de jogadores: '))
    if qnt_jogadores < 2 or qnt_jogadores > 8:
        print('Insira uma quantidade válida de jogadores.')
    else:
        break
        
# Instanciando os jogadores        
for ind in range(qnt_jogadores):
    nome = input('Insira o nome do jogador: ')
    cerebro = 0
    tiro = 0
    player = [ind,nome, cerebro, tiro]
    jogadores.append(player)


play = True
while (play):
        for player in jogadores:
            cod = player[0]
            nome = player[1]
            print(f"*-*-*-*-*-*-*-*-*-- {nome} --*-*-*-*-*-*-*-*-*")
            mostrarDadosCopo(copo)
            turno = True
            # Para os dados com face "passos"
            blockDado1 = True
            blockDado2 = True
            blockDado3 = True

            primeiroDado = -1
            segundoDado = -1
            terceiroDado = -1
            # Começando o turno
            while (turno):
                playGame = input("Pressione 'S' para jogar? [S/N]").upper()
                if playGame == "S":
                    pass
                else:
                    turno = False
                    play = False
                    break
                    
                print("Dados Sorteados:")
                if blockDado1:
                    primeiroDado, copo = pegarDadosCopo(copo)
                mostrarDado(primeiroDado)
                if blockDado2:
                    segundoDado, copo = pegarDadosCopo(copo)
                mostrarDado(segundoDado)
                if blockDado3:
                    terceiroDado, copo = pegarDadosCopo(copo)
                mostrarDado(terceiroDado)

                print("Mostrar Dados Copo:")
                mostrarDadosCopo(copo)

                one = ""
                two = ""
                three = ""
                # play dice
                if primeiroDado != -1:
                    one = lancarDado(primeiroDado)
                if segundoDado != -1:
                    two = lancarDado(segundoDado)
                if terceiroDado != -1:
                    three = lancarDado(terceiroDado)

                # Para os dados com face "passos"
                blockDado1 = True
                blockDado2 = True
                blockDado3 = True

                cerebro, tiro, passos = verificarScore(one, two, three)

                # Verificar se a vítima escapou
                if passos > 0:
                    if one == "P":
                        blockDado1 = False
                    if two == "P":
                        blockDado2 = False
                    if three == "P":
                        blockDado3 = False

                jogadores[cod][2] = player[2] + cerebro
                jogadores[cod][3] = player[3] + tiro
                print("Player: " + jogadores[cod][1])
                print("Cerebro: " + str(jogadores[cod][2]))
                print("Tiro: " + str(jogadores[cod][3]))

                if jogadores[player[0]][3] > 2:
                    print("Voce morreu!")
                    jogadores[player[0]][2] = 0
                    jogadores[player[0]][3] = 0
                    copoReset = []
                    copo = initDadosCopo(copoReset)
                    mostrarDadosCopo(copo)
                    turno = False

                if jogadores[player[0]][2] > 12:
                        print("Parabens, voce venceu!!")
                        play = False
                        turno = False

                if turno:
                        continueTurno = input("Voce deseja continuar? [S/N]").upper()
                        if continueTurno == "S":
                            pass
                        else:
                            jogadores[player[0]][3] = 0
                            copoReset = []
                            copo = initDadosCopo(copoReset)
                            mostrarDadosCopo(copo)
                            turno = False

