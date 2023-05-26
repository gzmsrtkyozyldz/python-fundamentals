# A popular dice game is Craps.
# In this project you will handle the rolling of dice and wagers while a user plays the game.
# A player rolls two dice. Each die has six faces. These faces contain 1, 2, 3, 4, 5, and 6 spots.
# After the dice have come to rest, the sum of the spots on the two upward faces is calculated.
# If the sum is 7 or 11 on the first throw, the player wins (this is called a “Natural win”).
# If the sum is 2, 3, or 12 on the first throw (called "craps"), the player loses (i.e. the "house" wins).

import random


def roll_dice():
    return random.randint(1, 6)


def game_craps():
    user_dict = {
        'Harry Potter': 100,
        'Lord Voldemort': 100,
        'Rubeus Hagrid': 100
    }

    bots = ['Bot1', 'Bot2', 'Bot3']

    while True:
        for user in user_dict:
            print(f'\nPlayer: {user}')
            bet = int(input('Enter your bet: '))


            # Roll the dice
            dice1 = roll_dice()
            dice2 = roll_dice()
            sum_dice = dice1 + dice2
            print(f'\nDice 1: {dice1}, Dice 2: {dice2}, Total: {sum_dice}')

            if sum_dice in (7, 11):
                print('You win!')
                user_dict[user] += bet
            elif sum_dice in (2, 3, 12):
                print('You lose!')
                user_dict[user] -= bet
            else:
                point = sum_dice
                print(f'Point is set to {point}')

                while True:
                    dice1 = roll_dice()
                    dice2 = roll_dice()
                    sum_dice = dice1 + dice2
                    print(f'\nDice 1: {dice1}, Dice 2: {dice2}, Total: {sum_dice}')

                    if sum_dice == point:
                        print('You win!')
                        user_dict[user] += bet
                        break
                    elif sum_dice == 7:
                        print('You lose!')
                        user_dict[user] -= bet
                        break

            print(f'Your balance: {user_dict[user]}')

        # Botlar için
        for bot in bots:
            bot_bet = random.randint(1, user_dict[bot])
            dice1 = roll_dice()
            dice2 = roll_dice()
            sum_dice = dice1 + dice2

            if sum_dice in (7, 11):
                print(f'\n{bot} wins!')
                user_dict[bot] += bot_bet
            elif sum_dice in (2, 3, 12):
                print(f'\n{bot} loses!')
                user_dict[bot] -= bot_bet
            else:
                point = sum_dice
                print(f'\nPoint is set to {point}')

                while True:
                    dice1 = roll_dice()
                    dice2 = roll_dice()
                    sum_dice = dice1 + dice2
                    print(f'\nDice 1: {dice1}, Dice 2: {dice2}, Total: {sum_dice}')

                    if sum_dice == point:
                        print(f'{bot} wins!')
                        user_dict[bot] += bot_bet
                        break
                    elif sum_dice == 7:
                        print(f'{bot} loses!')
                        user_dict[bot] -= bot_bet
                        break

            print(f"{bot}'s balance: {user_dict[bot]}")


game_craps()
