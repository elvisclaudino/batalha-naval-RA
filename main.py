#------------------------------------------- Variaveis gobais ------------------------------------------------
nLinhas = 20    #Numeros de linhas do tabuleiro
nColunas = 20   #Numero de colunas do tabuleiro
tabuleiro = [0] * nLinhas      #Gerando tabuleiro do jogador 1 (posicionar)
for linha in range(nLinhas):
    tabuleiro[linha] = ['  '] * nColunas

tabuleiro_tiros = [0] * nLinhas     #Gerando tabuleiro do jogador 2 (atirar)
for linha in range(nLinhas):
    tabuleiro_tiros[linha] = [' '] * nColunas

letras_para_numeros = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
                       'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19}  #Substituindo numeros por letras no tabuleiro

contador_tiros_certos = 0   #Contador de tiros certos
pontos = 0  #Pontos de tiros
contador_p1 = 0     #Contador do primeiro porta aviao
contador_p2 = 0     #Contador do segundo porta aviao
contador_p3 = 0     #Contador do terceiro porta aviao
contador_c1 = 0     #Contador do primeiro cruzador
contador_c2 = 0     #Contador do segundo cruzador
contador_c3 = 0     #Contador do terceiro cruzador
contador_c4 = 0     #Contador do quarto cruzador
contador_f1 = 0     #Contador da primeira fragata
contador_f2 = 0     #Contador da segunda fragata
contador_f3 = 0     #Contador da terceira fragata
contador_f4 = 0     #Contador da quarta fragata
contador_f5 = 0     #Contador da quinta fragata
#------------------------------------------------ Funcoes ---------------------------------------------------
def tabuleiro_ilustrado():      #Tabuleiro para o jogador 1 e jogador 2 idetificarem onde posicionar ou atirar
    print('\033[36m'' ', 0, '', 1, '', 2, '', 3, '', 4, '', 5, '', 6, '', 7, '', 8, '', 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
          19)
    print('A|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|A')
    print('B|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|B')
    print('C|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|C')
    print('D|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|D')
    print('E|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|E')
    print('F|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|F')
    print('G|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|G')
    print('H|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|H')
    print('I|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|I')
    print('J|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|J')
    print('L|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|L')
    print('M|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|M')
    print('N|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|N')
    print('O|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|O')
    print('P|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|P')
    print('Q|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|Q')
    print('R|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|R')
    print('S|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|S')
    print('T|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|T')
    print(' ', 0, '', 1, '', 2, '', 3, '', 4, '', 5, '', 6, '', 7, '', 8, '', 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
          19)

def print_tabuleiro():      #Printar linha por linha da matriz do tabuleiro do jogador 1 (posicoes)
    print('-=' * 32)
    for linha in tabuleiro:
        print(linha)
    print('-=' * 32)

def print_tabuleiro_tiros():        #Printar linha por linha da matriz do tabuleiro do jogador 2 (tiros)
    print('-=' * 32)
    for linha in tabuleiro_tiros:
        print(linha)
    print('-=' * 32)

def condLinha():
    linha = input("Escolha uma linha (A até T): ").upper()      #Informar a linha onde deseja posicionar o elemento
    while linha > 'T' or linha < 'A':       #Validar linha informada de A a T
        print('Linha inválida')
        print('-=' * 32)
        linha = input("Escolha uma linha válida (A até T): ").upper()
    return linha

def condColuna(limite, infoLimite):     #Parametros que mudam conforme o elemento posicionado(o limite de espaço e seu print no final)
    coluna = int(input(infoLimite))     #Informar a coluna onde deseja posicionar o elemento
    while coluna > limite or coluna < 0:    #Validar coluna informada de 0 até seu limite
        print('Coluna inválida')
        print('-=' * 32)
        coluna = int(input(infoLimite))
    return coluna

def imprimir_porta_aviao(cont, p):  #Parametro que muda conforme o numero do elemento (EX: porta aviao 1, porta aviao 2)
    if porta_aviao == cont:
        tabuleiro[numero_linha][numero_coluna] = p  #Altera o tabuleiro conforme as posicoes ordenadas, e automaticamente posicionando 3 à sua frente
        tabuleiro[numero_linha][numero_coluna + 1] = p
        tabuleiro[numero_linha][numero_coluna + 2] = p
        tabuleiro[numero_linha][numero_coluna + 3] = p

def imprimir_cruzadores(cont, c):   #Parametro que muda conforme o numero do elemento (EX: cruzador 1, cruzador 2)
    if cruzador == cont:
        tabuleiro[numero_linha][numero_coluna] = c  #Altera o tabuleiro conforme as posicoes ordenadas, e automaticamente posicionando 2 à sua frente
        tabuleiro[numero_linha][numero_coluna + 1] = c
        tabuleiro[numero_linha][numero_coluna + 2] = c

def imprimir_fragatas(cont, f):     #Parametro que muda conforme o numero do elemento (EX: fragata 1, fragata 2)
    if fragata == cont:
        tabuleiro[numero_linha][numero_coluna] = f      #Altera o tabuleiro conforme as posicoes ordenadas, e automaticamente posicionando 1 à sua frente
        tabuleiro[numero_linha][numero_coluna + 1] = f

def portaAviaoPontos(contadorSelect):   #Parametro que muda conforme o numero do elemento (EX: porta aviao 1, porta aviao 2)
    if contadorSelect == 1:     
        contadorp1 = 0
    elif contadorSelect == 2:
        contadorp2 = 0
    elif contadorSelect == 3:
        contadorp3 = 0
    print('Voce derrubou um porta-aviao inteiro!')
    print('-=' * 32)
    print('Ganhou 30 pontos') 
    return 30   #Retorna a quantidade de pontos obtidos

def cruzadorPontos(contadorSelect):     #Parametro que muda conforme o numero do elemento (EX: cruzador 1, cruzador 2)
    if contadorSelect == 1:
        contadorc1 = 0
    elif contadorSelect == 2:
        contadorc2 = 0
    elif contadorSelect == 3:
        contadorc3 = 0
    elif contadorSelect == 4:
        contadorc4 = 0
    print('Voce derrubou um cruzador inteiro!')
    print('-=' * 32)
    print('Ganhou 20 pontos')
    return 20   #Retorna a quantidade de pontos obtidos

def fragataPontos(contadorSelectFrag):      #Parametro que muda conforme o numero do elemento (EX: fragata 1, fragata 2)
    if contadorSelectFrag == 1:
        contadorf1 = 0
    if contadorSelectFrag == 2:
        contadorf2 = 0
    if contadorSelectFrag == 3:
        contadorf3 = 0
    if contadorSelectFrag == 4:
        contadorf4 = 0
    if contadorSelectFrag == 5:
        contadorf5 = 0
    print('Voce derrubou uma fragata inteira!')
    print('-=' * 32)
    print('Ganhou 10 pontos')
    return 10   #Retorna a quantidade de pontos obtidos
#------------------------------------------------ Inicio -------------------------------------------------
while True:     #Enquanto o programa estiver rodando
    print('\033[35m========================= BEM VINDO AO BATALHA NAVAL =========================')     #Regras
    print()
    print('- REGRAS')
    print(
        'Um jogador dispõe seus navios (sempre na horizontal) e outro tenta acertá-los informando o código de uma célula.')
    print('As Linhas devem ser selecionadas do A até o T')
    print('As colunas devem ser selecionadas do 0 até o limite do elemento')
    print(
        'O jogador tem direito a três Porta-Aviões de quatro partes, quatro Cruzadores de três partes e cinco Fragatas de duas partes')
    print('Um elemento é considerado abatido se todas as suas partes são atingidas.')
    print()
    print('- PONTUAÇÃO')
    print('Porta-Aviões: 30 pontos após o Naufrágio')
    print('Cruzador: 20 pontos após o Naufrágio')
    print('Porta-Aviões: 10 pontos após o Naufrágio')
    print('\033[35m')

    print('Deseja iniciar o jogo?')     #Se o jogador deseja iniciar ou finalizar o jogo
    inicio = str(input('S/N? ')).upper()
    while inicio != 'S' and inicio != 'N':  #Valida a resposta
        print('Seleção inválida!')
        inicio = str(input('Digite (S) para iniciar ou (N) para fechar o jogo: ')).upper()
    print('-=' * 32)

    if inicio == 'S':   #Se o jogador escolher iniciar
        tabuleiro_ilustrado()
        for porta_aviao in range(3):    #Posiciona seus 3 porta avioes
            print('-=' * 32)
            print("\033[34m'Escolha a posição do seu", porta_aviao + 1, '° Porta-Aviões')   #Identifica qual porta aviao esta posicionando
            print('-=' * 32)
            numero_linha = letras_para_numeros[condLinha()]     #Transforma as letras para numeros, podendo escolher inves de 0 o A
            numero_coluna = int(condColuna(16, "Escolha uma coluna (0 até 16): "))    #Guarda a informação da funcao condColuna

            while tabuleiro[numero_linha][numero_coluna] != '  ' or tabuleiro[numero_linha][numero_coluna + 3] != '  ':     #Verifica se a posição desejada ocupa espaço no tabuleiros
                print("Essa posição está ocupada!")
                print('-=' * 32)
                numero_linha = letras_para_numeros[condLinha()]
                numero_coluna = int(condColuna(16, "Escolha uma coluna (0 até 16): "))

            imprimir_porta_aviao(0, 'P1')   #Altera o tabuleiro conforme as posicoes ordenadas, e automaticamente posicionando 3 à sua frente
            imprimir_porta_aviao(1, 'P2')   #Altera o tabuleiro conforme as posicoes ordenadas, e automaticamente posicionando 3 à sua frente
            imprimir_porta_aviao(2, 'P3')   #Altera o tabuleiro conforme as posicoes ordenadas, e automaticamente posicionando 3 à sua frente

        print_tabuleiro()   #Imprime tabuleiro
        tabuleiro_ilustrado()   #Imprime tabuleiro para o jogador indetificar onde posicionar

        for cruzador in range(4):   #Posiciona seus 4 cruzadores
            print('-=' * 32)
            print('\033[32m'"Escolha a posição do seu", cruzador + 1, '° Cruzador')     #Identifica qual cruzador esta posicionando
            print('-=' * 32)
            numero_linha = letras_para_numeros[condLinha()]     #Transforma as letras para numeros, podendo escolher inves de 0 o A
            numero_coluna = int(condColuna(17, "Escolha uma coluna (0 até 17): "))      #Guarda a informação da funcao condColuna

            while tabuleiro[numero_linha][numero_coluna] != '  ' or tabuleiro[numero_linha][
                numero_coluna + 2] != '  ':     #Verifica se a posição desejada ocupa espaço no tabuleiros
                print("Essa posição está ocupada!")
    
                numero_linha = letras_para_numeros[condLinha()]
                numero_coluna = int(condColuna(17, "Escolha uma coluna (0 até 17): "))

            imprimir_cruzadores(0, 'C1')    #Altera o tabuleiro conforme as posicoes ordenadas, e automaticamente posicionando 2 à sua frente
            imprimir_cruzadores(1, 'C2')    #Altera o tabuleiro conforme as posicoes ordenadas, e automaticamente posicionando 2 à sua frente
            imprimir_cruzadores(2, 'C3')    #Altera o tabuleiro conforme as posicoes ordenadas, e automaticamente posicionando 2 à sua frente
            imprimir_cruzadores(3, 'C4')    #Altera o tabuleiro conforme as posicoes ordenadas, e automaticamente posicionando 2 à sua frente

        print_tabuleiro()   #Imprime tabuleiro
        tabuleiro_ilustrado()   #Imprime tabuleiro para o jogador indetificar onde posicionar

        for fragata in range(5):    #Posicona suas 5 fragatas
            print('-=' * 32)
            print("Escolha a posição da sua", fragata + 1, '° Fragata')     #Identifica qual fragata esta posicinando
            print('-=' * 32)
            numero_linha = letras_para_numeros[condLinha()]     #Transforma as letras para numeros, podendo escolher inves de 0 o A
            numero_coluna = int(condColuna(18, "Escolha uma coluna (0 até 18): "))      #Guarda a informação da funcao condColuna

            while tabuleiro[numero_linha][numero_coluna] != '  ' or tabuleiro[numero_linha][
                numero_coluna + 1] != '  ':     #Verifica se a posição desejada ocupa espaço no tabuleiros
                print("Essa posição está ocupada!")

                numero_linha = letras_para_numeros[condLinha()]
                numero_coluna = int(condColuna(18, "Escolha uma coluna (0 até 18): "))

            imprimir_fragatas(0, 'F1')      #Altera o tabuleiro conforme as posicoes ordenadas, e automaticamente posicionando 1 à sua frente
            imprimir_fragatas(1, 'F2')      #Altera o tabuleiro conforme as posicoes ordenadas, e automaticamente posicionando 1 à sua frente
            imprimir_fragatas(2, 'F3')      #Altera o tabuleiro conforme as posicoes ordenadas, e automaticamente posicionando 1 à sua frente
            imprimir_fragatas(3, 'F4')      #Altera o tabuleiro conforme as posicoes ordenadas, e automaticamente posicionando 1 à sua frente
            imprimir_fragatas(4, 'F5')      #Altera o tabuleiro conforme as posicoes ordenadas, e automaticamente posicionando 1 à sua frente

        print_tabuleiro()   #Imprime tabuleiro
        tabuleiro_ilustrado()   #Imprime tabuleiro para o jogador indetificar onde posicionar

        while contador_tiros_certos < 34:   #Enquanto o contador de tiros não chegar a 34 (total de posicoes de elementos) o jogador 2 continua atirando
            print('-=' * 32)
            tiro_linha = (input('Escolha uma linha (A até T) para atirar:')).upper()    #Informar a linha onde deseja posicionar o elemento
            while tiro_linha > 'T' or tiro_linha < 'A':     #Valida se a linha esta no limite de A a T
                print('Linha inválida')
                print('-=' * 32)
                tiro_linha = (input('Escolha uma linha (A até T) para atirar:')).upper()

            tiro_coluna = int(input('Escolha uma coluna (0 até 19) para atirar:'))       #Informar a coluna onde deseja posicionar o elemento
            while tiro_coluna > 19 or tiro_coluna < 0:      #Valida se a coluna esta no limite de 0 a 19
                print('Coluna inválida')
                print('-=' * 32)
                tiro_coluna = int(input('Escolha uma coluna (0 até 19) para atirar:'))

            numero_tiro_linha = letras_para_numeros[tiro_linha]     #Transforma as letras para numeros, podendo escolher inves de 0 o A
            numero_tiro_coluna = int(tiro_coluna)   #Guarda a informação da funcao condColuna

            if tabuleiro_tiros[numero_tiro_linha][numero_tiro_coluna] != ' ':   #Verifica se a posicao nao foi atirada anteriormente
                print('Você já atirou no mesmo lugar anteriormente!')

            elif tabuleiro[numero_tiro_linha][numero_tiro_coluna] == 'P1':  #Caso a posicao seja igual ao primeiro porta aviao
                tabuleiro_tiros[numero_tiro_linha][numero_tiro_coluna] = 'A'    #Coloca na matriz do jogador 2 que ele acertou e a posiciona onde ele acertou
                contador_tiros_certos += 1  #Adiciona ao contador de tiros certos
                print_tabuleiro_tiros()     #Imprime o tabuleiro do jogador 2 com as informacoes atualizadas
                print('Você acertou uma parte de um Elemento')
                contador_p1 += 1    #Adicina ao contador do primeiro porta aviao
                if contador_p1 == 4:    #Se o contador chegar em 4, ele derrubou todo o primeiro porta aviao
                    pontos += portaAviaoPontos(contador_p1)
                    print('voce tem ', pontos, 'pontos')    #Mostra na tela seu total de pontos

            elif tabuleiro[numero_tiro_linha][numero_tiro_coluna] == 'P2':  #Caso a posicao seja igual ao segundo porta aviao
                tabuleiro_tiros[numero_tiro_linha][numero_tiro_coluna] = 'A'    #Coloca na matriz do jogador 2 que ele acertou e a posiciona onde ele acertou
                contador_tiros_certos += 1  #Adiciona ao contador de tiros certos
                print_tabuleiro_tiros()     #Imprime o tabuleiro do jogador 2 com as informacoes atualizadas
                print('Você acertou uma parte de um Elemento')
                contador_p2 += 1    #Adicina ao contador do segundo porta aviao
                if contador_p2 == 4:    #Se o contador chegar em 4, ele derrubou todo o segundo porta aviao
                    pontos += portaAviaoPontos(contador_p2)
                    print('voce tem ', pontos, 'pontos')    #Mostra na tela seu total de pontos
                    
            elif tabuleiro[numero_tiro_linha][numero_tiro_coluna] == 'P3':  #Caso a posicao seja igual ao terceiro porta aviao
                tabuleiro_tiros[numero_tiro_linha][numero_tiro_coluna] = 'A'    #Coloca na matriz do jogador 2 que ele acertou e a posiciona onde ele acertou
                contador_tiros_certos += 1  #Adiciona ao contador de tiros certos
                print_tabuleiro_tiros()     #Imprime o tabuleiro do jogador 2 com as informacoes atualizadas
                print('Você acertou uma parte de um Elemento')
                contador_p3 += 1    #Adicina ao contador do terceiro porta aviao
                if contador_p3 == 4:    #Se o contador chegar em 4, ele derrubou todo o segundo porta aviao
                    pontos += portaAviaoPontos(contador_p3)
                    print('voce tem ', pontos, 'pontos')    #Mostra na tela seu total de pontos

            elif tabuleiro[numero_tiro_linha][numero_tiro_coluna] == 'C1':  #Caso a posicao seja igual ao primeiro cruzador
                tabuleiro_tiros[numero_tiro_linha][numero_tiro_coluna] = 'A'    #Coloca na matriz do jogador 2 que ele acertou e a posiciona onde ele acertou
                contador_tiros_certos += 1  #Adiciona ao contador de tiros certos
                print_tabuleiro_tiros()     #Imprime o tabuleiro do jogador 2 com as informacoes atualizadas
                print('Você acertou uma parte de um Elemento')
                contador_c1 += 1    #Adicina ao contador do primeiro cruzador
                if contador_c1 == 3:    #Se o contador chegar em 3, ele derrubou todo o primeiro cruzador
                    pontos += cruzadorPontos(contador_c1)
                    print('voce tem ', pontos, 'pontos')    #Mostra na tela seu total de pontos

            elif tabuleiro[numero_tiro_linha][numero_tiro_coluna] == 'C2':  #Caso a posicao seja igual ao segundo cruzador
                tabuleiro_tiros[numero_tiro_linha][numero_tiro_coluna] = 'A'    #Coloca na matriz do jogador 2 que ele acertou e a posiciona onde ele acertou
                contador_tiros_certos += 1  #Adiciona ao contador de tiros certos
                print_tabuleiro_tiros()     #Imprime o tabuleiro do jogador 2 com as informacoes atualizadas
                print('Você acertou uma parte de um Elemento')
                contador_c2 += 1    #Adicina ao contador do segundo cruzador
                if contador_c2 == 3:    #Se o contador chegar em 3, ele derrubou todo o segundo cruzador
                    pontos += cruzadorPontos(contador_c2)
                    print('voce tem ', pontos, 'pontos')    #Mostra na tela seu total de pontos

            elif tabuleiro[numero_tiro_linha][numero_tiro_coluna] == 'C3':  #Caso a posicao seja igual ao terceiro cruzador
                tabuleiro_tiros[numero_tiro_linha][numero_tiro_coluna] = 'A'    #Coloca na matriz do jogador 2 que ele acertou e a posiciona onde ele acertou
                contador_tiros_certos += 1  #Adiciona ao contador de tiros certos
                print_tabuleiro_tiros()     #Imprime o tabuleiro do jogador 2 com as informacoes atualizadas
                print('Você acertou uma parte de um Elemento')
                contador_c3 += 1    #Adicina ao contador do terceiro cruzador
                if contador_c3 == 3:    #Se o contador chegar em 3, ele derrubou todo o terceiro cruzador
                    pontos += cruzadorPontos(contador_c3)
                    print('voce tem ', pontos, 'pontos')    #Mostra na tela seu total de pontos

            elif tabuleiro[numero_tiro_linha][numero_tiro_coluna] == 'C4':  #Caso a posicao seja igual ao quarto cruzador
                tabuleiro_tiros[numero_tiro_linha][numero_tiro_coluna] = 'A'     #Coloca na matriz do jogador 2 que ele acertou e a posiciona onde ele acertou
                contador_tiros_certos += 1  #Adiciona ao contador de tiros certos
                print_tabuleiro_tiros()     #Imprime o tabuleiro do jogador 2 com as informacoes atualizadas
                print('Você acertou uma parte de um Elemento')
                contador_c4 += 1    #Adicina ao contador do quarto cruzador
                if contador_c4 == 3:    #Se o contador chegar em 3, ele derrubou todo o quarto cruzador
                    pontos += cruzadorPontos(contador_c4)
                    print('Voce tem ', pontos, 'pontos!')   #Mostra na tela seu total de pontos

            elif tabuleiro[numero_tiro_linha][numero_tiro_coluna] == 'F1':  #Caso a posicao seja igual a primeira fragata
                tabuleiro_tiros[numero_tiro_linha][numero_tiro_coluna] = 'A'    #Coloca na matriz do jogador 2 que ele acertou e a posiciona onde ele acertou
                contador_tiros_certos += 1  #Adiciona ao contador de tiros certos
                print_tabuleiro_tiros()     #Imprime o tabuleiro do jogador 2 com as informacoes atualizadas
                print('Você acertou uma parte de um Elemento')
                contador_f1 += 1    #Adicina ao contador da primeira fragata
                if contador_f1 == 2:    #Se o contador chegar em 3, ele derrubou toda a primeira fragata
                    pontos += fragataPontos(contador_f1)
                    print('voce tem ', pontos, 'pontos')    #Mostra na tela seu total de pontos

            elif tabuleiro[numero_tiro_linha][numero_tiro_coluna] == 'F2':  #Caso a posicao seja igual a segunda fragata
                tabuleiro_tiros[numero_tiro_linha][numero_tiro_coluna] = 'A'    #Coloca na matriz do jogador 2 que ele acertou e a posiciona onde ele acertou
                contador_tiros_certos += 1  #Adiciona ao contador de tiros certos
                print_tabuleiro_tiros()     #Imprime o tabuleiro do jogador 2 com as informacoes atualizadas
                print('Você acertou uma parte de um Elemento')
                contador_f2 += 1    #Adicina ao contador da segunda fragata
                if contador_f2 == 2:    #Se o contador chegar em 3, ele derrubou toda a segunda fragata
                   pontos += fragataPontos(contador_f2)
                   print('voce tem ', pontos, 'pontos')     #Mostra na tela seu total de pontos
                
            elif tabuleiro[numero_tiro_linha][numero_tiro_coluna] == 'F3':  #Caso a posicao seja igual a terceira fragata
                tabuleiro_tiros[numero_tiro_linha][numero_tiro_coluna] = 'A'    #Coloca na matriz do jogador 2 que ele acertou e a posiciona onde ele acertou
                contador_tiros_certos += 1  #Adiciona ao contador de tiros certos
                print_tabuleiro_tiros()     #Imprime o tabuleiro do jogador 2 com as informacoes atualizadas
                print('Você acertou uma parte de um Elemento')
                contador_f3 += 1    #Adicina ao contador da terceira fragata
                if contador_f3 == 2:     #Se o contador chegar em 3, ele derrubou toda a terceira fragata
                    pontos += fragataPontos(contador_f3)
                    print('voce tem ', pontos, 'pontos')    #Mostra na tela seu total de pontos

            elif tabuleiro[numero_tiro_linha][numero_tiro_coluna] == 'F4':  #Caso a posicao seja igual a quarta fragata
                tabuleiro_tiros[numero_tiro_linha][numero_tiro_coluna] = 'A'    #Coloca na matriz do jogador 2 que ele acertou e a posiciona onde ele acertou
                contador_tiros_certos += 1  #Adiciona ao contador de tiros certos
                print_tabuleiro_tiros()     #Imprime o tabuleiro do jogador 2 com as informacoes atualizadas
                print('Você acertou uma parte de um Elemento')
                contador_f4 += 1    #Adicina ao contador da quarta fragata
                if contador_f4 == 2:    #Se o contador chegar em 3, ele derrubou toda a quarta fragata
                    pontos += fragataPontos(contador_f4)
                    print('voce tem ', pontos, 'pontos')    #Mostra na tela seu total de pontos

            elif tabuleiro[numero_tiro_linha][numero_tiro_coluna] == 'F5':  #Caso a posicao seja igual a quinta fragata
                tabuleiro_tiros[numero_tiro_linha][numero_tiro_coluna] = 'A'    #Coloca na matriz do jogador 2 que ele acertou e a posiciona onde ele acertou
                contador_tiros_certos += 1  #Adiciona ao contador de tiros certos
                print_tabuleiro_tiros()     #Imprime o tabuleiro do jogador 2 com as informacoes atualizadas
                print('Você acertou uma parte de um Elemento')
                contador_f5 += 1    #Adicina ao contador da quinta fragata
                if contador_f5 == 2:    #Se o contador chegar em 3, ele derrubou toda a quinta fragata
                    pontos += fragataPontos(contador_f5)
                    print('voce tem ', pontos, 'pontos')    #Mostra na tela seu total de pontos

            if tabuleiro[numero_tiro_linha][numero_tiro_coluna] == '  ':    #Caso a posicao do tabuleiro esteja vazia
                tabuleiro_tiros[numero_tiro_linha][numero_tiro_coluna] = 'X'    #O jogador errou o tiro e coloca na matriz do jogador 2 onde ele errou
                print_tabuleiro_tiros()
                print('Você atirou no mar!')

        print('-=' * 32)
        print('Você acertou todas as partes do návio!')     #finalizaou o jogo
        print('-=' * 32)

    else:   #Caso o jogador deseja encerrar o jogo
        break