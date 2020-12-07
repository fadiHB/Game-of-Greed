from collections import Counter
import random


class Banker:

    def __init__(self):
      self.balance = 0
      self.shelved = 0

    def shelf(self,num):
        '''
        Will temporarily store unbanked points
        Argument:
            num{int} --  is the amount of points (integer) to add to shelf. 
        output:
            num{int} -- add the num to the shelved
        '''
        self.shelved += num
        return self.shelved

    def bank(self):
        """
        Add any points on the shelf to total and reset shelf    
        """
        self.balance += self.shelved
        self.clear_shelf()
        return self.balance


    def clear_shelf(self):
        '''
        clear the shelved
         '''
        self.shelved = 0

class GameLogic:

    @staticmethod
    def calculate_score(result_dices):

        '''
        Returns an integer representing the roll’s score according to rules of game.
        Arguments:
            calc {tuple} -- is a tuple of integers that represent a dice roll.
        Output:
            Returns the score according to rules of the game
        '''

        score = 0
        count = Counter(result_dices).most_common()

        if (len(count) == 3 and count[0][1] == count[1][1] == count[2][1]):
            score += 1500
            return score

        if (len(count) == 6):
            score += 1500
            return score

        # if (count == [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1)]):
        #     score += 1500
        #     return score

        for i in range(len(count)):

            if (count[i][0] == 1):
                # print(count[i][0])
                if count[i][1] == 1:
                    score += 100
                if count[i][1] == 2:
                    score += 200
                if count[i][1] == 3:
                    score += 1000
                if count[i][1] == 4:
                    score += 2000
                if count[i][1] == 5:
                    score += 3000
                if count[i][1] == 6:
                    score += 4000

            if (count[i][0] == 5):
                # print(count[i][0])
                if count[i][1] == 1:
                    score += 50
                if count[i][1] == 2:
                    score += 100
                if count[i][1] == 3:
                    score += 500
                if count[i][1] == 4:
                    score += 1000
                if count[i][1] == 5:
                    score += 1500
                if count[i][1] == 6:
                    score += 2000

            if (count[i][0] == 2):
                # print(count[i][0])
                if count[i][1] == 1 or 2:
                    score += 0
                if count[i][1] == 3:
                    score += 200
                if count[i][1] == 4:
                    score += 400
                if count[i][1] == 5:
                    score += 600
                if count[i][1] == 6:
                    score += 800

            if (count[i][0] == 3):
                # print(count[i][0])
                if count[i][1] == 1 or 2:
                    score += 0
                if count[i][1] == 3:
                    score += 300
                if count[i][1] == 4:
                    score += 600
                if count[i][1] == 5:
                    score += 900
                if count[i][1] == 6:
                    score += 1200

            if (count[i][0] == 4):
                # print(count[i][0])
                if count[i][1] == 1 or 2:
                    score += 0
                if count[i][1] == 3:
                    score += 400
                if count[i][1] == 4:
                    score += 800
                if count[i][1] == 5:
                    score += 1200
                if count[i][1] == 6:
                    score += 1600

            if (count[i][0] == 6):
                # print(count[i][0])
                if count[i][1] == 1 or 2:
                    score += 0
                if count[i][1] == 3:
                    score += 600
                if count[i][1] == 4:
                    score += 1200
                if count[i][1] == 5:
                    score += 1800
                if count[i][1] == 6:
                    score += 2400
        return score

    @staticmethod
    def roll_dice(number):
        '''
        Rolls the dice num times
        Arguments:
            num {integer} -- how many times to roll the dice
        
        Output:
            Returns a tuple of length num
        '''
        my_list = []
        for i in range(number):
            my_list.append(random.randint(1,number))
        return tuple(my_list)


if __name__ == "__main__":
    pass

    # result_dices = [1, 2, 3, 4, 5, 6]
    # count = Counter(result_dices).most_common()
    # print(count)

    # x = GameLogic.calculate_score(result_dices)
    # print(x)


