from funcoes import *

game=new_game()
# Partida
while True:
    # Desenha o tabuleiro
    create_board(game[1])
    # Pede/Caputra a jogada do jogador
    game[1]=catch_play(game[0], game[1])
    # Verifica se a jogada é vitoriosa
    win=check_win(game[1])
    # Verifica se ainda há campos em branco
    no_empty_field=check_empty_fields(game[1])
    # Caso haja vitório ou não haja mais campos em branco
    if win or no_empty_field:
        # Perguntar se desejam um novo jogo
        start_new_game=ask_new_game()
        # Se sim
        if start_new_game:
            # Reinicia o jogo
            game=new_game()
        # Se não
        else:
            # Para de jogar
            break
    # Caso não
    else:
        # Inverte o jogador
        game[0]=not game[0] 