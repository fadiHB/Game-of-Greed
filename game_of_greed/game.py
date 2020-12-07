from game_of_greed.game_logic import *


class Game:
    def __init__(self, roller=None):
        self.roller = roller or GameLogic.roll_dice
        self.round = 1
        self.remaining_dice= 6

    @staticmethod
    def input_dice(dice_to_keep):
        new = (int(i) for i in dice_to_keep)
        return new

    @staticmethod
    def quit_masseg(score):
        print(f'Total score is {score} points')
        print(f'Thanks for playing. You earned {score} points')

    @staticmethod
    def welcom():
        print('Welcome to Game of Greed')
        res = input('Wanna play?').lower()
        return res  
    def rounds(self):
        print(f'Starting round {self.round}')
        print(f'Rolling {self.remaining_dice} dice...')
        roll = self.roller(self.remaining_dice)
        print(','.join([str(i) for i in roll]))


                

    def play(self):
        score = 0
        my_bank = Banker()
        res = self.welcom()
        if res == 'n' or res == 'no':
            print('OK. Maybe another time')
        elif res == 'y' or res == 'yes':
            self.rounds()
            dice_to_keep = input(
                'Enter dice to keep (no spaces), or (q)uit: ').lower()
            if dice_to_keep == 'q' or dice_to_keep == 'quit':
                Game.quit_masseg(score)
            else:
                
                result = Game.input_dice(dice_to_keep)
                my_bank.shelf(GameLogic.calculate_score(result))
                self.remaining_dice -= len(dice_to_keep)
                print(f'You have {my_bank.shelved} unbanked points and {self.remaining_dice} dice remaining')
               
                while True:
                    options = input('(r)oll again, (b)ank your points or (q)uit ').lower()

                    if options == 'q' or options == 'quit':
                        Game.quit_masseg(score)
                        break

                    elif options == 'b' or options == 'bank':
                        print(f'You banked {my_bank.shelved} points in round {self.round}')
                        my_bank.bank()
                        print(f'Total score is {my_bank.balance} points')
                        self.round += 1
                        self.remaining_dice = 6
                        self.rounds()

                        dice_to_keep = input('Enter dice to keep (no spaces), or (q)uit: ').lower()
                        if dice_to_keep == 'q' or dice_to_keep == 'quit':
                            Game.quit_masseg(my_bank.balance)
                            # status = True
                            break
                        else:
                            result = Game.input_dice(dice_to_keep)
                            my_bank.shelf(
                                GameLogic.calculate_score(result))
                            self.remaining_dice -= len(dice_to_keep)
                            print(
                                f'You have {my_bank.shelved} unbanked points and {self.remaining_dice} dice remaining')

                          


if __name__ == '__main__':
    game = Game()
    game.play()
