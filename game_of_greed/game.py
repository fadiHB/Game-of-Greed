from game_of_greed.game_logic import *
import sys

class Game:
    def __init__(self, roller=None):
        self.roller = roller or GameLogic.roll_dice
        self.round = 1
        self.remaining_dice= 6
        self.dice=[]

    # @staticmethod
    # def input_dice(dice_to_keep):

    #     try:
    #         newdice = [int(i) for i in dice_to_keep]
    #         # print(tuple(newdice))
    #         return tuple(newdice)
    #     except:
    #         my_bank = Banker()
    #         Game.quit_masseg(my_bank.balance)
    #         sys.exit()



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
        return roll

    def zilch_method(self):
        my_bank = Banker()
        print('Zilch!!! Round over')
        print(f'You banked 0 points in round {self.round}')
        print(f'Total score is {my_bank.balance} points')
        self.remaining_dice = 6
        self.round+=1

     

    def play(self):
        score = 0
        my_bank = Banker()
        res = self.welcom()
          
        def input_dice(dice_to_keep):

            try:
                newdice = [int(i) for i in dice_to_keep]
                # print(tuple(newdice))
                return tuple(newdice)
            except:
                # my_bank = Banker()
                Game.quit_masseg(my_bank.balance)
                sys.exit()


        if res == 'n' or res == 'no':
            print('OK. Maybe another time')
        elif res == 'y' or res == 'yes':
                print(f'Starting round {self.round}')
                print(f'Rolling {self.remaining_dice} dice...')
                rounds = self.rounds()
                print(','.join([str(i) for i in rounds]))

               
                

                while GameLogic.calculate_score(input_dice(rounds)) == 0 :
                    self.zilch_method()
                    print(f'Starting round {self.round}')
                    print(f'Rolling {self.remaining_dice} dice...')
                    print(','.join([str(i) for i in self.rounds()]))
                    break

                    
                   
                  
                
                while True:
                    dice_to_keep = input(
                        'Enter dice to keep (no spaces), or (q)uit: ').lower()

                    inp = input_dice(dice_to_keep) 
                    
                    # if dice_to_keep == 'q' or dice_to_keep == 'quit':
                    #     flag=False  
                       
                    flag=True  
                    while flag:
                        flag2 = False
                        elem =[]
                        for i in inp:
                           
                            if tuple(rounds).count(i) >= tuple(inp).count(i):
                                elem.append(i)
                            
                        if len(elem) != len(list(inp)):
                           
                            print('Cheater!!! Or possibly made a typo...')
                            if self.dice==[]:
                                self.dice=rounds
                            
                            print(','.join([str(i) for i in self.dice]))
                           

                            flag2 = True
                        flag=False 

                    if flag2:
                        continue
 
                    if dice_to_keep == 'q' or dice_to_keep == 'quit':
                        Game.quit_masseg(my_bank.balance)
                        break           
                   
                    else:
                        
                        result =input_dice(dice_to_keep)
                        my_bank.shelf(GameLogic.calculate_score(result))
                        self.remaining_dice -= len(dice_to_keep)
                        print(f'You have {my_bank.shelved} unbanked points and {self.remaining_dice} dice remaining')
                
  
                    options = input('(r)oll again, (b)ank your points or (q)uit ').lower()

                    if options == 'q' or options == 'quit':
                        Game.quit_masseg(my_bank.balance)
                        break
                    elif options =='r' or options =='roll':
                  
                            print(f'Rolling {self.remaining_dice} dice...')
                            # round2 = self.rounds()
                            self.dice=self.rounds()
                            print(','.join([str(i) for i in self.dice]))





                            while GameLogic.calculate_score(input_dice(self.dice)) == 0 :
                               

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
                        self.dice=self.rounds()
                        print(','.join([str(i) for i in self.dice]))
                        
                                    


if __name__ == '__main__':
    game = Game()
    game.play()



