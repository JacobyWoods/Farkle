import random
from collections import Counter

class Round:

    def __init__(self):
        self.score = 0
        self.initial_rolls = 0


class Hand:

    def __init__(self):
        self.score = 0
        self.hand_dice = []
        self.max_dice = 6

    def add_dice(self, dice_to_add):
        for dice in dice_to_add:
            self.hand_dice.append(dice)


class Roll:

    def __init__(self, number_dice_to_roll):
        self.roll_dice = []
        self.max_dice = 6
        self.roll_dice = [random.randint(1, 6) for x in range(number_dice_to_roll)]


def create_scoring_combinations_dict():

    scoring_combinations = {1: 100,
                            5: 50,
                            (1, 1, 1): 300,
                            (2, 2, 2): 200,
                            (3, 3, 3): 300,
                            (4, 4, 4): 400,
                            (5, 5, 5): 500,
                            (6, 6, 6): 600,
                            (1, 2, 3, 4, 5, 6): 1500}
    for i in range(4, 7):
        scoring_combinations[(i, i, i, i)] = 1000
        scoring_combinations[(i, i, i, i, i)] = 2000
        scoring_combinations[(i, i, i, i, i, i)] = 3000

    for i in range(1, 7):
        for j in range(i + 1, 7):
            scoring_combinations[(i, i, i, j, j, j)] = 2500

    for i in range(1, 7):
        for j in range(i + 1, 7):
            for k in range(j + 1, 7):
                scoring_combinations[(i, i, j, j, k, k)] = 1500

    for i in range(1, 7):
        for j in range(1, 7):
            if i != j:
                scoring_combinations[(i, i, i, i, j, j)] = 1500

    return scoring_combinations


def check_for_score(kept_dice_to_check=(1, 3, 3, 1, 3, 1)):

    scoring_combinations = create_scoring_combinations_dict()

    dice_to_check_counter = Counter(kept_dice_to_check)

    roll_score, pair_count, triple_count, quad_count = 0, 0, 0, 0
    for die_number in range(6):
        dice_count = dice_to_check_counter[die_number]
        if die_number == 1:
            if sorted(kept_dice_to_check) == [1, 2, 3, 4, 5, 6]:
                roll_score += 1500
            elif dice_to_check_counter[die_number] < 4:
                if dice_to_check_counter[die_number] == 2:
                    pair_count += 1
                elif dice_to_check_counter[die_number] == 3:
                    triple_count += 1
                roll_score += 100 * dice_to_check_counter[die_number]
            elif dice_to_check_counter[die_number] >= 4:
                roll_score += 1000 * (dice_to_check_counter[die_number] - 3)
                if dice_to_check_counter[die_number] == 4:
                    quad_count += 1
        elif die_number == 5 and dice_to_check_counter[die_number] <= 2:
            roll_score += dice_to_check_counter[die_number] * 50
            if dice_to_check_counter[die_number] == 2:
                pair_count += 1
        else:
            if dice_to_check_counter[die_number] == 2:
                pair_count += 1
            elif dice_to_check_counter[die_number] == 3:
                roll_score += die_number * 100
                triple_count += 1
            elif dice_to_check_counter[die_number] > 3:
                roll_score += 1000 * (dice_to_check_counter[die_number] - 3)
                quad_count += 1
    if pair_count == 3:
        roll_score = 1500
    elif triple_count == 2:
        roll_score = 2500
    elif quad_count == 1 and pair_count == 1:
        roll_score == 1500

    print(dice_to_check_counter)
    print(sorted(kept_dice_to_check))
    print(roll_score)
    print(pair_count, triple_count, quad_count)


def main_script_for_now():

    print('Welcome to Farkle game!')
    print('Current ')
    user_play_y_n = input('Play (y/n)?: ')

    if user_play_y_n == 'y':
        roll_or_hold = input('Roll or hold (r/h)?: ')
        number_of_dice_to_roll = 6
        hand = Hand()
        while roll_or_hold == 'r':
            current_roll = Roll(number_of_dice_to_roll)
            print(f'Dice rolled: {current_roll.roll_dice}')
            dice_to_hold_index = [int(x) for x in input('Index of dice to hold separated by space (0 is first index): ').split()]
            dice_to_hold = [current_roll.roll_dice[x] for x in dice_to_hold_index]
            hand.add_dice(dice_to_hold)
            print('*' * 25)
            print(f'Hand dice: {hand.hand_dice}')
            number_of_dice_to_roll = 6 - len(hand.hand_dice)
            print(f'Number of dice to roll: {number_of_dice_to_roll}')
            print('*' * 25)
            roll_or_hold = input('Roll or hold (r/h)?: ')

    else:
        check_for_score()


if __name__ == '__main__':

    check_for_score()