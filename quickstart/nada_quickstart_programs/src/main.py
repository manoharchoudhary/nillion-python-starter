from nada_dsl import *

def nada_main():
    # Define parties
    player = Party(name="Player")
    game_master = Party(name="GameMaster")
    result_party = Party(name="ResultParty")

    # Game master provides the position of the ball (randomly decided outside of this code)
    ball_position = SecretInteger(Input(name="BallPosition", party=game_master))  # 1, 2, or 3
    guess = SecretInteger(Input(name="Guess", party=player))  # Player's guess (1, 2, or 3)

    # Check if the guess is correct
    is_correct = guess == ball_position

    # Output the result
    result = Output(is_correct, "GuessResult", result_party)
    
    return [result]
