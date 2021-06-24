def comeco():
    # zeraJogo()
    jogos = 1
    print ("Deseja Jogar? - S/n")
    jogar = input()
    if (jogar.upper == "S" or jogar == ''):
        jogo()


def zeraJogo():
    global mapa 
    global jogoExecutando
    mapa = [[0,0,0], [0,0,0], [0,0,0]]
    jogoExecutando = 0


def jogo():
    zeraJogo()
    global jogoExecutando
    global empates
    jogada=0
    # print (str(soma))
    print ("Placar: " + str(placar))
    print ("Empates: " + str(empates))
    while (jogoExecutando == 0):
        print("Jogador ", jogada%2 + 1)
        exibe()
        while True:
            try:
                linha  = int(input("Linha :"))
                coluna = int(input("Coluna:"))
                break
            except ValueError:
                print("Favor preencher os campos")

        if mapa[linha-1][coluna-1] == 0:
            if (jogada%2+1)==1:
                mapa[linha-1][coluna-1]=1
            else:
                mapa[linha-1][coluna-1]=-1
        else:
            print("Campo preenchido, por favor escolha outro")
            jogada -=1
        
        jogoExecutando = ganhou()
        if (jogoExecutando == 1):
            # mapa = [[0,0,0], [0,0,0], [0,0,0]]
            exibe()
            print("Jogador ",jogada%2 + 1," ganhou apos ", jogada+1," rodadas")
            comeco()
        else:
            jogada +=1

        if(jogada == 9):
            print("Empatou!")
            exibe()
            empates += 1
            comeco()
        
    
def ganhou():
    if (checaLinha() == 1):
        return 1
    if (checaColuna() == 1):
        return 1
    if (checaDiagonal() == 1):
        return 1
    return 0


def checaLinha():
    for i in range(3):
        soma = mapa[i][0]+mapa[i][1]+mapa[i][2]
        if (soma == 3):
            placar[0] += 1
            return 1
        if (soma == -3):
            placar[1] += 1
            return 1
    return 0


def checaColuna():
    for i in range(3):
        soma = mapa[0][i]+mapa[1][i]+mapa[2][i]
        if (soma == 3):
            placar[0] += 1
            return 1
        if (soma == -3):
            placar[1] += 1
            return 1
    return 0


def checaDiagonal():
    #checando diagonais
    diagonal1 = mapa[0][0]+mapa[1][1]+mapa[2][2]
    diagonal2 = mapa[0][2]+mapa[1][1]+mapa[2][0]
    if diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3:
        if (diagonal1 == 3 or diagonal2 == 3):
            placar[0] += 1
            return 1
        if (diagonal1 == -3 or diagonal2 == -3):
            placar[1] += 1
            return 1
    return 0


def exibe():
    for i in range(3):
        for j in range(3):
            if mapa[i][j] == 0:
                print(" _ ", end=' ')
            elif mapa[i][j] == 1:
                print(" X ", end=' ')
            elif mapa[i][j] == -1:
                print(" O ", end=' ')

        print() 


partida = 0
placar = [0, 0]
empates = 0
mapa = [[0,0,0], [0,0,0], [0,0,0]]
jogoExecutando = 0
zeraJogo()
comeco()