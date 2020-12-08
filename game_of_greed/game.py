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
        roll = self.roller(self.remaining_dice)
        # print(','.join([str(i) for i in roll]))
        return roll

    def zilch_method(self):
        my_bank = Banker()
        print('Zilch!!! Round over')
        print(f'You banked 0 points in round {self.round}')
        print(f'Total score is {my_bank.balance} points')
        self.remaining_dice = 6
        self.round+=1

    
    # def check_cheater(self,tup,npt): 
    #     elem =[]

    #     for i in npt:
    #         if tuple(tup).count(i) >= tuple(npt).count(i):
    #             elem.append(i)
    #     if len(elem) != len(list(npt)):
    #         return True
            
    #     else:
    #         return False    
     

    def play(self):
        score = 0
        my_bank = Banker()
        res = self.welcom()
        if res == 'n' or res == 'no':
            print('OK. Maybe another time')
        elif res == 'y' or res == 'yes':
                print(f'Starting round {self.round}')
                print(f'Rolling {self.remaining_dice} dice...')
                rounds = self.rounds()
                print(','.join([str(i) for i in rounds]))

               
                

                while GameLogic.calculate_score(Game.input_dice(rounds)) == 0 :
                    # print(' zilch ----1 ')
                    self.zilch_method()
                    print(f'Starting round {self.round}')
                    print(f'Rolling {self.remaining_dice} dice...')
                    print(','.join([str(i) for i in self.rounds()]))
                    break

                    
                   
                  
                
                while True:
                    dice_to_keep = input(
                        'Enter dice to keep (no spaces), or (q)uit: ').lower()

                    if GameLogic.calculate_score((Game.input_dice(dice_to_keep)) == 1500 and len(dice_to_keep) == 6 :

                    # inp = Game.input_dice(dice_to_keep)    
                    # new_roll=self.roller(self.remaining_dice)
                    # # cheater= self.check_cheater(new_roll,inp)
                    # # while cheater:
                    # #     print('Cheater!!! Or possibly made a typo...')
                    # #     print(','.join([str(i) for i in new_roll]))
                    # #     break
                    # flag=True  
                    # while flag:
                    #     flag2 = False
                    #     elem =[]
                    #     for i in inp:
                    #         if tuple(new_roll).count(i) >= tuple(inp).count(i):
                    #             elem.append(i)
                    #     if len(elem) != len(list(inp)):
                    #         print('Cheater!!! Or possibly made a typo...')
                    #         print(','.join([str(i) for i in new_roll]))
                    #         # dice_to_keep = input(
                    #         # 'Enter dice to keep (no spaces), or (q)uit: ').lower()
                    #         # if dice_to_keep == 'q' or dice_to_keep == 'quit':
                    #         #     Game.quit_masseg(my_bank.balance)
                    #         flag2 = True
                    #     flag=False 
                    
                    # if flag2:
                    #     print('continue here ...')
                    #     continue
                    
                        
                       
                    if dice_to_keep == 'q' or dice_to_keep == 'quit':
                        Game.quit_masseg(my_bank.balance)
                        break           
                   
                    else:
                        
                        result = Game.input_dice(dice_to_keep)
                        my_bank.shelf(GameLogic.calculate_score(result))
                        self.remaining_dice -= len(dice_to_keep)
                        print(f'You have {my_bank.shelved} unbanked points and {self.remaining_dice} dice remaining')
                
  
                    options = input('(r)oll again, (b)ank your points or (q)uit ').lower()

                    if options == 'q' or options == 'quit':
                        Game.quit_masseg(my_bank.balance)
                        break
                    elif options =='r' or options =='roll':
                        # while options: 
                            print(f'Rolling {self.remaining_dice} dice...')
                            round2 = self.rounds()
                            print(','.join([str(i) for i in round2]))





                            while GameLogic.calculate_score(Game.input_dice(round2)) == 0 :
                                # print(' zilch ----2 ')

                                self.zilch_method()
                                print(f'Starting round {self.round}')
                                print(f'Rolling {self.remaining_dice} dice...')
                                print(','.join([str(i) for i in self.rounds()]))
                                
                                break
                            # status=True



                    elif options == 'b' or options == 'bank':
                        print(f'You banked {my_bank.shelved} points in round {self.round}')
                        my_bank.bank()
                        print(f'Total score is {my_bank.balance} points')
                        self.round += 1
                        self.remaining_dice = 6
                        print(f'Starting round {self.round}')
                        print(f'Rolling {self.remaining_dice} dice...')
                        print(','.join([str(i) for i in self.rounds()]))            


if __name__ == '__main__':
    game = Game()
    game.play()



