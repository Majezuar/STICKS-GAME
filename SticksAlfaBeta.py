import math
import random

class StickGame:
    def __init__(self, num_sticks):
        self.num_sticks = num_sticks
        self.max = 3
        self.min = 1
    
    def removeSticks(self, sticks):
        self.num_sticks -= sticks
    
    def printSticks(self):
        for _ in range(self.num_sticks):
            print("|", end=" ")

    def computerTurn(self):
        player = "1" 
        position = self.minimax(player, -math.inf, math.inf)['count']
        return position

    def minimax(self, player, alpha, beta):
        computer = "1"
        player2 = "1" if player == "0" else "0"
        
        if self.num_sticks == 0:
            return {'count': None, 'score': -1 if player2 == computer else 1} 
        
        if player == computer:
            best_result = {'count': None, 'score': -math.inf}
        else:
            best_result = {'count': None, 'score': math.inf}

        for i in range(self.min, min(self.max, self.num_sticks) + 1):
            self.num_sticks -= i 
            temp_val = self.minimax(player2, alpha, beta)
            self.num_sticks += i

            temp_val['count'] = i
            
            if player == computer:
                if temp_val['score'] > best_result['score']:
                    best_result = temp_val
                alpha = max(alpha, best_result['score'])
            else:
                if temp_val['score'] < best_result['score']:
                    best_result = temp_val
                beta = min(beta, best_result['score'])
            
            if beta <= alpha:
                break

        return best_result

    def playGame(self):
        result = 0
        while self.num_sticks > 0:    
            self.printSticks()
            while True:
                result = int(input(f"\nEnter the number of sticks to remove between {self.min} and {self.max}: "))        
                if self.max >= result >= self.min and result <= self.num_sticks:
                    break 
            self.removeSticks(result)
            print(f"The player has removed {result} stick(s)") 
            if self.num_sticks == 0:
                print("\nThe computer wins!")
                break
            self.printSticks()   
            computer = self.computerTurn()
            self.removeSticks(computer)
            print(f"\nThe computer has removed {computer} stick(s)")
            if self.num_sticks == 0:
                print("\nThe player wins!")
            if self.num_sticks < self.max:
                self.max = self.num_sticks

num_sticks = random.randint(10, 20)
game_board = StickGame(num_sticks)

game_board.playGame()

