import pathlib
from enum import Enum

class Opponent(Enum):
    A='Rock'
    B='Paper'
    C='Scissors'

class Player(Enum):
    X='Rock'
    Y='Paper'
    Z='Scissors'

class GameOutcome(Enum):
    X='Lose'
    Y='Draw'
    Z='Win'

class ShapeScore(Enum):
    Rock=1
    Paper=2
    Scissors=3

class RoundScore(Enum):
    Win=6
    Draw=3
    Loss=0

winner = {
    'Rock': 'Paper',
    'Scissors': 'Rock',
    'Paper': 'Scissors'
}

def calculate_winner(opponent: str, player: str) -> str:
    if opponent == player:
        return 'Draw'

    if opponent == 'Rock':
        if player == 'Scissors':
            return 'Loss'
        else:
            return 'Win'
    
    if opponent == 'Paper':
        if player == 'Rock':
            return 'Loss'
        else:
            return 'Win'
    
    if opponent == 'Scissors':
        if player == 'Paper':
            return 'Loss'
        else:
            return 'Win'


def calculate_player_shape(opponent: str, outcome: str) -> Player:
    if outcome == 'Draw':
        return Player(opponent).value

    if opponent == 'Rock':
        if outcome == 'Win':
            return 'Paper'
        else:
            return 'Scissors'
    
    if opponent == 'Paper':
        if outcome == 'Win':
            return 'Scissors'
        else:
            return 'Rock'
    
    if opponent == 'Scissors':
        if outcome == 'Win':
            return 'Rock'
        else:
            return 'Paper'
        

def scoring(opponent: Opponent, player: Player) -> int:
    shape1, shape2 = opponent.value, player.value
    player_shape_score = ShapeScore[shape2].value
    winner = calculate_winner(shape1, shape2)
    return RoundScore[winner].value + player_shape_score


def scoring_forced_outcome(opponent: Opponent, gameresult: GameOutcome) -> int:
    opponent_shape = opponent.value
    gameresult = gameresult.value
    playershape = calculate_player_shape(opponent_shape, gameresult)
    print(f"player shape: {playershape}")
    return scoring(opponent, Player(playershape))

        



root_path = pathlib.Path(__file__).parent.resolve()
filename = 'input.txt'
# print((pathlib.Path(__file__).parent).joinpath(filename))
with open((pathlib.Path(__file__).parent).joinpath(filename)) as file:
    data = file.read().splitlines()

normal_rounds = []
forced_rounds = []

for round in data:
    round = round.split(' ')
    # print(Opponent(round0))
    normal_rounds.append([Opponent[round[0]], Player[round[1]]])
    forced_rounds.append([Opponent[round[0]], GameOutcome[round[1]]])
    # print(scoring(round[0], round[1]))

# for round in rounds:
total_score = [(scoring(round[0], round[1])) for round in normal_rounds]
forced_total_score = [(scoring_forced_outcome(round[0], round[1])) for round in forced_rounds]

print(f"Maximum score if everything goes exactly according to your strategy guide: {sum(total_score)}")
print(f"Maximum score for the given outcomes of each game: {sum(forced_total_score)}")
