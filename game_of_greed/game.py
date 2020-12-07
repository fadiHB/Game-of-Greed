from game_of_greed.game_logic import *


class Game:
    def __init__(self, roller=None):
        self.roller = roller or GameLogic.roll_dice

    @staticmethod
    def input_dice(dice_to_keep):
        new = (int(i) for i in dice_to_keep)
        return new

    @staticmethod
    def quit_masseg(score):
        print(f'Total score is {score} points')
        print(f'Thanks for playing. You earned {score} points')
  
            

    def play(self):
        round = 1
        remaining_dice = 6
        score = 0
        my_bank = Banker()
        banked = my_bank.bank()

        print('Welcome to Game of Greed')
        res = input('Wanna play?').lower()
        if res == 'n' or res == 'no':
            print('OK. Maybe another time')
        elif res == 'y' or res == 'yes':
            

            print(f'Starting round {round}')
            print(f'Rolling {remaining_dice} dice...')
            roll = self.roller(remaining_dice)

            print(','.join([str(i) for i in roll]))
            dice_to_keep = input(
                'Enter dice to keep (no spaces), or (q)uit: ').lower()
            if dice_to_keep == 'q' or dice_to_keep == 'quit':
                Game.quit_masseg(score)
            else:
                status = False
                
                result = Game.input_dice(dice_to_keep)
                my_bank.shelf(GameLogic.calculate_score(result))
                remaining_dice -= len(dice_to_keep)
                print(f'You have {my_bank.shelved} unbanked points and {remaining_dice} dice remaining')
               
                while True:
                    options = input('(r)oll again, (b)ank your points or (q)uit ').lower()

                    

                    if options == 'q' or options == 'quit':
                        Game.quit_masseg(score)
                        break

                    elif options == 'b' or options == 'bank':
                        

                        print(f'You banked {my_bank.shelved} points in round {round}')
                        my_bank.bank()
                        print(f'Total score is {my_bank.balance} points')
                        round += 1
                        remaining_dice = 6

                        print(f'Starting round {round}')
                        print(f'Rolling {remaining_dice} dice...')
                        roll = self.roller(remaining_dice)

                        print(','.join([str(i) for i in roll]))
                        dice_to_keep = input('Enter dice to keep (no spaces), or (q)uit: ').lower()
                        if dice_to_keep == 'q' or dice_to_keep == 'quit':
                            Game.quit_masseg(my_bank.balance)
                            status = True
                            break
                        else:
                            result = Game.input_dice(dice_to_keep)
                            my_bank.shelf(
                                GameLogic.calculate_score(result))
                            remaining_dice -= len(dice_to_keep)
                            print(
                                f'You have {my_bank.shelved} unbanked points and {remaining_dice} dice remaining')

                          


if __name__ == '__main__':
    game = Game()
    game.play()
