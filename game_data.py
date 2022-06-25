# file contains game data and text for rock paper scissors while cooking the functions for
# easy use by anyone.
game_rules = []
game_text = []

# function returns game rules by reading from rules.txt file , return type is a list


def get_game_rules():
    input_file = open('rules.txt', 'r')
    for line in input_file:
        game_rules.append(line)
    input_file.close()
    return game_rules


def get_game_info(index_game_data):
    input_file = open('gametext.txt')
    for line in input_file:
        game_text.append(line)
    input_file.close()
    return game_text[index_game_data]










