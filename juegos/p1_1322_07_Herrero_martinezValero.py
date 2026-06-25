from game import (
    TwoPlayerGameState,
)
from tournament import (
    StudentHeuristic,
)

from reversi import from_dictionary_to_array_board

def stable_positions(board, player, oponent) -> int:
        """
            Funcion para calcular las piezas en posiciones estables (no pueden cambiar de color) de un jugador
        """
        stable_pos = 0
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for i in range(8):
            for j in range(8):
                if board[i][j] == player:
                    stable = True
                    for x, y in directions:
                        dispx, disply = i + x, j + y
                        # the position is stable if all directions are blocked or occupied by the player
                        if 0 <= dispx < 8 and 0 <= disply < 8:
                            if board[dispx][disply] == oponent or(board[dispx][disply] != oponent and board[dispx][disply] != player) :
                                stable = False
                                break
                    if stable:
                        stable_pos += 1
        return stable_pos
 
""" 
    Funciones privadas de reversi adaptadas: 
    capture_enemy_in_dir
    enemy_captured_by_move
    get_valid_moves
"""
def capture_enemy_in_dir(board: dict, move, player_label, enemy, delta_x_y) -> list:
        (delta_x, delta_y) = delta_x_y
        x, y = move
        x, y = x + delta_x, y + delta_y
        enemy_list_0 = []
        while board.get((x, y)) == enemy:
            enemy_list_0.append((x, y))
            x, y = x + delta_x, y + delta_y
        if board.get((x, y)) != player_label:
            del enemy_list_0[:]
        x, y = move
        x, y = x - delta_x, y - delta_y
        enemy_list_1 = []
        while board.get((x, y)) == enemy:
            enemy_list_1.append((x, y))
            x, y = x - delta_x, y - delta_y
        if board.get((x, y)) != player_label:
            del enemy_list_1[:]
        return enemy_list_0 + enemy_list_1

def enemy_captured_by_move(board: dict, move, player_label, enemy_label) -> list:
    return capture_enemy_in_dir(board, move, player_label, enemy_label, (0, 1)) \
            + capture_enemy_in_dir(board, move, player_label, enemy_label, (1, 0)) \
            + capture_enemy_in_dir(board, move, player_label, enemy_label, (1, -1)) \
            + capture_enemy_in_dir(board, move, player_label, enemy_label, (1, 1))

def get_valid_moves(board: dict, player_label, enemy_label) -> int:
    """Returns a list of valid moves for the player judging from the board."""
    # Get all positions adjacent to existing pieces
    candidates = set()
    # Check all 8 directions around each occupied position
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                    (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for (x, y) in board.keys():
        for dx, dy in directions:
            adj_x, adj_y = x + dx, y + dy
            # Only consider positions within board bounds and not occupied
            if (1 <= adj_x <= 8 and
                1 <= adj_y <= 8 and
                    (adj_x, adj_y) not in board):
                candidates.add((adj_x, adj_y))
    # Now check only these candidate positions for valid moves
    valid_moves = 0
    for pos in candidates:
        if enemy_captured_by_move(board, pos, player_label, enemy_label):
            valid_moves += 1

    return valid_moves

class Solution1(StudentHeuristic):
    def get_name(self) -> str:
        return "PrimeraSoluciónGrupo07"

    def evaluation_function(self, state: TwoPlayerGameState) -> float:
        """
        Heurística simple basada únicamente en la diferencia de fichas.
        Positiva si el jugador actual tiene más fichas que el oponente,
        negativa si tiene menos.
        """
        board = state.board
        player = state.next_player.label

        # Inferimos la etiqueta del oponente
        labels = set(board.values())
        if len(labels) == 1:
            opponent = (labels - {player}).pop() if player in labels else list(labels)[0]
        elif len(labels) == 2:
            opponent = (labels - {player}).pop()
        else:
            opponent = None  # caso raro: tablero vacío

        # Contamos fichas
        player_coins = sum(1 for v in board.values() if v == player)
        opponent_coins = sum(1 for v in board.values() if v == opponent) if opponent else 0

        # Calculamos la diferencia normalizada
        if (player_coins + opponent_coins) > 0:
            value = 100 * (player_coins - opponent_coins) / (player_coins + opponent_coins)
        else:
            value = 0

        return value

class Solution2(StudentHeuristic):
    def get_name(self) -> str:
        return "SegundaSoluciónGrupo07"

    def evaluation_function(self, state: TwoPlayerGameState) -> float:
        """
        Heurística basada en la suma de los puntos establecidos por nosotros en points_for_board
        y la diferencia de estos dependiendo de si la posicion esta ocupada por el jugador o el oponente
        """
        board_array = from_dictionary_to_array_board(state.board, 8, 8) # Inicializamos el tablero
        heuristica = 0

        #los puntos estan puestos en base a la importancia que tiene cada posicion en el tablero para tableros de 8x8
        points_for_board = [[4, -3, 2, 2, 2, 2, -3, 4], [-3, -4, -1, -1, -1, -1, -4, -3], [2, -1, 1, 0, 0, 1, -1, 1], [2, -1, 0, 1, 1, 0, -1, 2],
                            [2, -1, 0, 1, 1, 0, -1, 2], [2, -1, 1, 0, 0, 1, -1, 2], [-3, -4, -1, -1, -1, -1, -4, -3], [4, -3, 2, 2, 2, 2, -3, 4]]

        # Comprobamos si somos jugador MAX o jugador MIN
        if state.is_player_max(state.next_player): 
            player = state.next_player.label
            oponent = state.previous_player.label
        else:
            player = state.previous_player.label
            oponent = state.next_player.label

        player_coins = 0
        oponent_coins = 0

        for i in range(8):
            for j in range(8):
                if board_array[i][j] == player:
                    player_coins += points_for_board[i][j]
                elif board_array[i][j] == oponent:  
                    oponent_coins += points_for_board[i][j]
        
        heuristica = player_coins - oponent_coins

        return heuristica
    
class Solution3(StudentHeuristic):
    def get_name(self) -> str:
        return "3rd Sol 07"

    def evaluation_function(self, state: TwoPlayerGameState) -> float:
        h = 0.0
        board_array = from_dictionary_to_array_board(state.board, 8, 8)

        if state.is_player_max(state.next_player): 
            player = state.next_player.label
            oponent = state.previous_player.label
        else:
            player = state.previous_player.label
            oponent = state.next_player.label

        filled = 0        
        for i in range(8):
            for j in range(8):
                if board_array[i][j] == player or board_array[i][j] == oponent:  
                   filled += 1

        if filled <= 22: #opening
            weights = [0.2, 0.3, 0.2, 0.3]
        elif filled <= 45: #middle game
            weights = [0.3, 0.1, 0.2, 0.4]
        else: #end game
            weights = [0.5, 0.1, 0.1, 0.1]

        stable_player = stable_positions(board_array, player, oponent)
        stable_oponent = stable_positions(board_array, oponent, player)
        s = 100 * (stable_player - stable_oponent) / (stable_player + stable_oponent + 1)

        mob_player = get_valid_moves(state.board, player, oponent)
        mob_oponent = get_valid_moves(state.board, oponent, player)
        m = 100 * (mob_player - mob_oponent) / (mob_player + mob_oponent + 1)

        cor_player = 0
        cor_oponent = 0
        for x, y in [(0, 0), (0, 7), (7, 0), (7, 7)]:
            if (board_array[x][y] == player):
                cor_player += 1
            if (board_array[x][y] == oponent):
                cor_oponent += 1
        c = 25 * (cor_player - cor_oponent)

        player_coins = 0
        oponent_coins = 0

        points_for_board = [[4, -3, 2, 2, 2, 2, -3, 4], 
                            [-3, -4, -1, -1, -1, -1, -4, -3], 
                            [2, -1, 1, 0, 0, 1, -1, 1],
                            [2, -1, 0, 1, 1, 0, -1, 2],
                            [2, -1, 0, 1, 1, 0, -1, 2], 
                            [2, -1, 1, 0, 0, 1, -1, 2], 
                            [-3, -4, -1, -1, -1, -1, -4, -3], 
                            [4, -3, 2, 2, 2, 2, -3, 4]]
        for i in range(8):
            for j in range(8):
                if board_array[i][j] == player:
                    player_coins += points_for_board[i][j]
                elif board_array[i][j] == oponent:  
                    oponent_coins += points_for_board[i][j]
        pos_eval = 100 * (player_coins - oponent_coins)

        h += weights[0] * s + weights[1] * m + weights[2] * c + pos_eval * weights[3]
        return h