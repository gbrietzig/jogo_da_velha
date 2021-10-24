
from visual import *

def new_game():
    """
        Objetivo: Começar um novo jogo
        Retorno: O jogador um, e o tabuleiro
    """
    # Retorna o jogador um e um novo tabuleiro
    return [
        True,
        {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None,
            9: None
        }
    ]

def player_name(player1):
    """
        Objetivo: Dar nomenclatura ao jogador
        Recebe: O booleano de jogador
        Processamento: Verifica se é o jogador 1 ou o jogador 2
        Retorno: Nome do jogador
    """

    # Verifica o jogador e retorna o nome dele.
    if player1:
        return '1 (O)'
    else:
        return '2 (X)' 

def catch_play(player1, board):
    """
        Objetivo: Capturar a jogada do jogador e atualizar o tabuleiro
        Recebe: O jogador e o tabuleiro antes da jogada
        Processamento: Pede e valida a jogada
        -quando inválida: pede novamente
        -quando válido atualiza o tabuleiro
        Retorno: Tabuleiro atualizado
    """

    # Definição da nomenclatura do jogador
    player=player_name(player1)
    
    # Nomeia os campos vazios para auxiliar o jogador se necessário
    empty_fields=''
    for field in board:
        if board[field]==None:
            empty_fields=empty_fields+str(field)+', '
    empty_fields=empty_fields[:-2]
    
    # Define a mensagem da primeira solicitação
    message=f'Jogador {player} é a sua vez. Insira um dos números disponíveis para selecionar a posição do jogo: '

    while True:
        # Caso não informe um número: ERRO
        # Caso informe um número fora do tabuleiro: ERRO
        # Caso informe um número já jogado: ELSE
        # Caso informe um número corretamente: RETURN
        try:
            play=int(input(message))
            if board[play]==None:
                board[play]=player1
                return board
            else:
                message=f'Jogador {player} essa posição já está ocupada, tente um campo disponível ({empty_fields}): '
        except:
            message=f'Jogador {player} não identifiquei a jogada, tente um campo disponível ({empty_fields}): '

def create_board(board, win=None):
    """
        Objetivo: Trocar o tabuleiro (dicionário) para uma matriz 3x3 e definir os caracteres de cada posição
        Recebe: Recebe o tabuleiro (dicionário) e possíveis dados de uma vitória
        Processamento: Cria um novo dicionário para trocar os caracteres, os organiza em uma matriz 3x3 e chama a função de desenho
    """

    # Novo dicionario vazio
    internal_board={}

    # Em cada um dos campos
    for field in board:
        # Se verdadeiro é jogador 1, substitui por O
        if board[field]:
            internal_board[field]='O'
        # Se falso é jogador 2, substitui por X
        elif board[field]==False:
            internal_board[field]='X'
        # Se nenhum jogador jogou nesse campo (none), substitui pelo número do campo
        else:
            internal_board[field]=field

    # Organizar o tabuleiro em 3x3
    order_board=[]
    for index_row in range(3):
        order_line=[]
        for index_cow in range(3):
            order_line.append(internal_board[index_row*3+index_cow+1])
        order_board.append(order_line)

    # Chama a função de desenho
    draw_board(order_board, win)

def draw_board(board, win):
    """
        Objetivo: Desenhar o tabuleiro para os jogadores
        Recebe: Recebe o tabuleiro (matriz) e possíveis dados de uma vitória
        Processamento: Substitui os caracteres pelos desenhos armazenados fora das funções, em caso de vitória risca a sequencia vitoriosa e desenha o quadro para os jogadores
    """

    # Cria uma nova matriz com os desenhos de cada campo
    board_to_print=[]
    # Para cada linha na matriz
    for order_row in board:
        # Para cada linha dos desenhos pré-definidos manda informa index
        for index_line_in_field in range(len(field[order_row[0]])):
            # Nova matriz recebe a linha index dos 3 desenhos da linha separados pelo delimitador de coluna.
            board_to_print.append(field[order_row[0]][index_line_in_field][0]+delimiter_cols+field[order_row[1]][index_line_in_field][0]+delimiter_cols+field[order_row[2]][index_line_in_field][0])
        # Quando terminar de desenhar a linha cria um novo divisor de linha
        board_to_print.append(delimiter_rows)
    # Apaga a linha divisória excedente
    board_to_print=board_to_print[:-1]

    # Em caso de vitória desenhe a linha sobre os campos que deram a vitória ao jogador
    if win!=None:
        # Se a vitória for horizontal
        if win[1]=='-':
            start_row=None
            if win[0]==1:
                start_row=3
            elif win[0]==4:
                start_row=11
            elif win[0]==7:
                start_row=19
            start_col=6
            final_col=38
            prefix=board_to_print[start_row][:start_col]
            sufix=board_to_print[start_row][final_col+1:]
            new_pixels=''
            for d in range(len(board_to_print[start_row])-len(prefix)-len(sufix)):
                new_pixels=new_pixels+win[1]
            board_to_print[start_row]=prefix+new_pixels+sufix
        # Se a vitória for vertical
        elif win[1]=='|':
            start_col=None
            if win[0]==1:
                start_col=6
            elif win[0]==2:
                start_col=22
            elif win[0]==3:
                start_col=38
            start_row=4
            final_row=20
            for i in range(start_row-1, final_row):
                prefix=board_to_print[i][:start_col]
                sufix=board_to_print[i][start_col+1:]
                board_to_print[i]=prefix+'|'+sufix
        # Se a vitória for diagonal
        elif win[1]=='/':
            start_row=3
            final_row=19
            start_col=None
            marc=None
            if win[0]==1:
                start_col=6
                final_col=38
                marc='\\'
            elif win[0]==3:
                start_col=38
                final_col=6
                marc='/'
            edited_line=0
            for index_row in range(len(board_to_print)):
                if start_row<=index_row<=final_row:
                    if marc=='\\':
                        col=start_col+edited_line*2
                    elif marc=='/':
                        col=start_col-edited_line*2
                    prefix=board_to_print[index_row][:col]
                    sulfix=board_to_print[index_row][col+2:]
                    board_to_print[index_row]=prefix+marc+' '+sulfix
                    edited_line=edited_line+1

    # Desenhar o tabuleiro
    for row_to_print in board_to_print:
        print(row_to_print)

def check_win(board):
    """
        Objetivo: Verificar a jogada é vitoriosa
        Recebe: O tabuleiro
        Processamento: Verifica com a última jogada houve vitória com base em campos chaves.
        -quando há vitória chama a função para desenhar e informa a vitória
        Retorno: Verdadeiro se houver vitório, falso se não houver
    """
    field_reference=None
    orientation=None

    # Vitória com o primeiro campo
    if ((board[1] == board[2] == board[3]) or (board[1] == board[4] == board[7]) or (board[1] == board[5] == board[9])) and board[1] !=None:
        field_reference=1
        # Na orizontal
        if board[1] == board[2]:
            orientation='-'
        # Na vertical
        elif board[1] == board[4]:
            orientation='|'
        # Na diagonal
        elif board[1] == board[5]:
            orientation='/'
    
    # Vitória com o segundo campo
    elif (board[2] == board[5] == board[8]) and board[2] !=None:
        field_reference=2
        # Na vertical
        orientation = '|'

    # Vitória com o terceiro campo
    elif ((board[3] == board[6] == board[9]) or (board[3] == board[5] == board[7])) and board[3] !=None:
        field_reference=3
        # Na vertical
        if board[3] == board[6]:
            orientation='|'
        # Na diagonal
        elif board[3] == board[5]:
            orientation='/'

    # Vitória com o quarto campo
    elif (board[4] == board[5] == board[6]) and board[4] !=None:
        field_reference=4
        # Na orizontal
        orientation='-'

    # Vitória com o sétimo campo
    elif (board[7] == board[8] == board[9]) and board[7] !=None:
        field_reference=7
        # Na orizontal
        orientation='-'
    
    # Se houve vitória, o campo referencia está preenchido
    if field_reference:
        # Desenha o tabuleiro vitorioso
        create_board(board, [field_reference, orientation])
        # Informa a vitória
        print(f'PARABÉNS JOGADOR {player_name(board[field_reference])}. A VITÓRIA É SUA...')
        return True
    return False

def check_empty_fields(board):
    """
        Objetivo: Verificar se acabaram os campos livres
        Recebe: O tabuleiro
        Processamento: Verifica com a última jogada ainda há campos disponíveis
        Retorno: Falso se houver, verdadeiro se não houver
    """
    # Para cada campo no tabuleiro
    for field in board:
        # Se existir campo livre
        if board[field]==None:
            return False
    # Não existe campo livre
    create_board(board)
    print('Acabaram as jogadas disponíveis. A partida terminou em empate...')
    return True

def ask_new_game():
    """
        Objetivo: Verificar se os jogadores desejam jogar um novo jogo
        Processamento: Pergunta se os jogadores deseja jogar um novo jogo e processam a resposta para booleano
        Retorno: booleano
    """
    
    # Define a mensagem da solicitação
    message=f'Jogadores, desejam jogar mais uma partida? (1-Sim / 2-Não): '

    while True:
        # Caso não informe um número: ERRO
        # Caso informe um número diferente: ELSE
        # Caso informe um número corretamente: RETURN
        try:
            reply=int(input(message))
            if reply == 1:
                return True
            if reply==2:
                return False
            else:
                message=f'Jogadores, utilizem apenas os numerais 1 e 2 para responder a pergunta: '
        except:
            message=f'Jogadores, utilizem apenas os numerais 1 e 2 para responder a pergunta: '
