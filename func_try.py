# using list and functions returns while passing in an argument


player_Age = [21, 22, 23, 24, 25]
player_name = ['nicolas', 'Isaac', 'princess']


def use_list(list_index):
    print(player_Age[list_index])


def return_to_list(list_index):
    value = player_name[list_index]
    return value
