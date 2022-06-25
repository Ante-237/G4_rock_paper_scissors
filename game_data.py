# file contains game data and text for rock paper scissors while cooking the functions for
# easy use by anyone.


# function returns game rules by reading from rules.txt file , return type is a list
def get_game_rules(point):
    input_file = open('rules.txt', 'r')
    game_rules = input_file.read(10)

    while len(game_rules):
        output_rules = input_file.read(10)
    input_file.close()
    return output_rules[point]



