import random

import requests


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return{
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'order': pokemon['order'],
    }


def random_stat():
    random_number = random.randint(1, 4)
    if random_number == 1:
        stat = 'id'
    elif random_number == 2:
        stat = 'height'
    elif random_number == 3:
        stat = 'weight'
    else:
        stat = 'order'
    return stat


def my_round():

    my_score = 0
    opponent_score = 0

    random_pokemon_1 = random_pokemon()
    random_pokemon_2 = random_pokemon()
    random_pokemon_3 = random_pokemon()

    print('Your pokemon choices are: {}, {}, {} '.format(random_pokemon_1['name'], random_pokemon_2['name'], random_pokemon_3['name']))
    pokemon_choice = input('Which pokemon do you want to use? ')

    if pokemon_choice == random_pokemon_1['name']:
        my_pokemon = random_pokemon_1
    elif pokemon_choice == random_pokemon_2['name']:
        my_pokemon = random_pokemon_2
    elif pokemon_choice == random_pokemon_3['name']:
        my_pokemon = random_pokemon_3

    print('Your stats are: id: {}, height: {}, weight: {}, order: {} '.format(my_pokemon['id'],my_pokemon['height'],my_pokemon['weight'],my_pokemon['order']))
    stat_choice = input('Which stat do you want to use? (id, height, weight, order) ')

    opponent_pokemon = random_pokemon()
    print('The opponent chose {}'.format(opponent_pokemon['name']))

    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]

    if my_stat > opponent_stat:
        print('You Win!')
        my_score = my_score + 1
    elif my_stat < opponent_stat:
        print('You Lose!')
        opponent_score = opponent_score + 1
    else:
        print('Draw!')

    print("The result of this round is: You {}, Opponent {} ".format(my_score, opponent_score))

    return my_score, opponent_score


def opponent_round():

    my_score = 0
    opponent_score = 0

    random_pokemon_1 = random_pokemon()
    random_pokemon_2 = random_pokemon()
    random_pokemon_3 = random_pokemon()

    print('Your pokemon choices are: {}, {}, {} '.format(random_pokemon_1['name'], random_pokemon_2['name'], random_pokemon_3['name']))
    pokemon_choice = input('Which pokemon do you want to use? ')

    if pokemon_choice == random_pokemon_1['name']:
        my_pokemon = random_pokemon_1
    elif pokemon_choice == random_pokemon_2['name']:
        my_pokemon = random_pokemon_2
    elif pokemon_choice == random_pokemon_3['name']:
        my_pokemon = random_pokemon_3

    opponent_pokemon = random_pokemon()
    print('The opponent chose {}'.format(opponent_pokemon['name']))

    opponent_stat_choice = random_stat()
    print('The opponent chose {} as their stat choice'.format(opponent_stat_choice))

    opponent_stat = opponent_pokemon[opponent_stat_choice]

    my_stat = my_pokemon[opponent_stat_choice]

    if my_stat > opponent_stat:
        print('You Win!')
        my_score = my_score + 1
    elif my_stat < opponent_stat:
        print('You Lose!')
        opponent_score = opponent_score + 1
    else:
        print('Draw!')

    print("The result of this round is: You {}, Opponent {} ".format(my_score, opponent_score))

    return my_score, opponent_score


def run():
    with open("scores.txt", "w+") as scores_file:

        scores_list = []

        for rounds in range(2):
            my_round_scores = my_round()
            opponent_round_scores = opponent_round()
            scores_list.append(my_round_scores)
            scores_list.append(opponent_round_scores)

        for score in scores_list:
            scores_file.write('(My Score, Opponent Score):' + '%s\n' % str(score))


run()





