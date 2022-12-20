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
        self.max_roll_score = check_for_score(self.roll_dice)


def check_for_straight(dice_combo_to_check):

    if sorted(list(dice_combo_to_check)) == [1, 2, 3, 4, 5, 6]:
        return True


def print_round_status(round_object):
    pass


def check_for_score(kept_dice_to_check=(3, 3, 1, 5, 1, 5)):

    dice_to_check_counter = Counter(kept_dice_to_check)

    roll_score, pair_count, triple_count, quad_count = 0, 0, 0, 0
    for die_number in range(6):
        dice_count = dice_to_check_counter[die_number]
        if die_number == 1:
            if dice_count < 4:
                if dice_count == 2:
                    pair_count += 1
                elif dice_count == 3:
                    triple_count += 1
                roll_score += 100 * dice_count
            elif dice_count >= 4:
                roll_score += 1000 * (dice_count - 3)
                if dice_count == 4:
                    quad_count += 1
        elif die_number == 5 and dice_count <= 2:
            roll_score += dice_count * 50
            if dice_count == 2:
                pair_count += 1
        else:
            if dice_count == 2:
                pair_count += 1
            elif dice_count == 3:
                roll_score += die_number * 100
                triple_count += 1
            elif dice_count > 3:
                roll_score += 1000 * (dice_count - 3)
                quad_count += 1
    if pair_count == 3:
        roll_score = 1500
    elif triple_count == 2:
        roll_score = 2500
    elif quad_count == 1 and pair_count == 1:
        roll_score = 1500
    elif check_for_straight(kept_dice_to_check):
        roll_score = 1500

    return roll_score


def check_for_no_score_dice(dice_to_check=(2, 1, 3, 4, 5, 6)):

    dice_to_check_counter = Counter(dice_to_check)
    non_score_pair_count = 0
    pair_count = 0
    quad_count = 0

    for die_number in (2, 3, 4, 6):
        if dice_to_check_counter[die_number] == 1:
            if not check_for_straight(dice_to_check):
                return True
        if dice_to_check_counter[die_number] == 2:
            non_score_pair_count += 1
            pair_count += 1
        if dice_to_check_counter[die_number] == 4:
            quad_count += 1

    for die_number in (1, 5):
        if dice_to_check_counter[die_number] == 2:
            pair_count += 1
        if dice_to_check_counter[die_number] == 4:
            quad_count += 1

    if non_score_pair_count == 1 and quad_count != 1 and pair_count != 3:
        return True


def main_script_for_now():

    print('Welcome to Farkle game!')
    user_play_y_n = input('Play (y/n)?: ')

    if user_play_y_n == 'y':
        roll_or_hold = input('Roll or hold (r/h)?: ')
        number_of_dice_to_roll = 6
        hand = Hand()
        round_score = 0
        roll_number = 0
        while roll_or_hold == 'r':
            roll_number += 1
            current_roll = Roll(number_of_dice_to_roll)
            print(f'Dice rolled: {current_roll.roll_dice}')
            max_roll_score = check_for_score(current_roll.roll_dice)
            print(f'Roll max score: {current_roll.max_roll_score}')
            if current_roll.max_roll_score == 0:
                round_score = 0
                print('Sorry, you Farkle!')
                break
            dice_to_hold_index = [int(x) for x in input('Index of dice to hold separated by space (0 is first index): ').split()]
            dice_to_hold = [current_roll.roll_dice[x] for x in dice_to_hold_index]
            while check_for_no_score_dice(dice_to_hold):
                print('Sorry, you can only keep scoring dice. Try again.')
                dice_to_hold_index = [int(x) for x in input('Index of dice to hold separated by space (0 is first index): ').split()]
                dice_to_hold = [current_roll.roll_dice[x] for x in dice_to_hold_index]
            if check_for_score(dice_to_hold) > 0:
                hand.add_dice(dice_to_hold)
                round_score += check_for_score(dice_to_hold)
            print('*' * 35)
            print(f'Roll Number: {roll_number} | Round Score: {round_score}')
            print(f'Hand dice: {hand.hand_dice}')
            number_of_dice_to_roll = 6 - len(hand.hand_dice)
            if number_of_dice_to_roll != 0:
                print(f'Number of dice to roll: {number_of_dice_to_roll}')
                print('*' * 35)
                roll_or_hold = input('Roll or hold (r/h)?: ')
            else:
                print('Congrats, new roll!')
                number_of_dice_to_roll = 6
                hand = Hand()
        print('*' * 35)
        print(f'Total round score: {round_score}')


if __name__ == '__main__':

    main_script_for_now()