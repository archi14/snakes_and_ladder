import random
from Board       import Board
from Snake       import Snake
from Ladder      import Ladder
from Player      import Player
from Board       import Board


class PlayService():
    multiple_sixes=False
    def __init__(self, board_size, snakes_positions=dict(), ladders_positions=dict(), players=[], number_of_dices=1):
        
        self.snakes = []
        self.ladders = []
        self.players = []
        self.snakes_positions = snakes_positions
        self.ladders_positions = ladders_positions
        self.board_size = board_size
        self.number_of_players = len(players)
        self.number_of_dices = number_of_dices

        for head,tail in snakes_positions.items():
            snake = Snake(head, tail)
            self.snakes.append(snake)

        for start,end in ladders_positions.items():
            ladder = Ladder(start, end)
            self.ladders.append(ladder)
        
        for player_name in players:
            player = Player(player_name)
            self.players.append(player)

        self.board = Board(self.board_size, self.snakes, self.ladders,  self.players)
       

    def roll_dice(self):
        dice_value = 0
        for i in range(self.number_of_dices):
            dice_value+=int(random.random()*6+1)
        return dice_value

    def check_win(self, player):
        if player.get_position()==self.board_size:
            return True
        
        return False

    def is_snake(self, position):

        if position in self.snakes_positions.keys():
            return True
        return False

    def is_ladder(self, position):
        if position in self.ladders_positions.keys():
            return True
        
        return False

    def move_player(self, current_position, dice_value):
        next_position = current_position + dice_value
        if next_position > self.board_size:
            return current_position
            while(True):
                snake_or_ladder = False
                if(self.is_snake(next_position)):
                    next_position = self.snakes_positions[next_position]
                    snake_or_ladder = True
                    
                if(self.is_ladder(next_position)):
                    next_position = self.ladders_positions[next_position]
                    snake_or_ladder = True
                    
                if not snake_or_ladder:
                    break
        
        return next_position

    def play(self):

        while self.number_of_players>1:
            for player in self.players:
                current_position = player.get_position()
                dice_value = self.roll_dice()
                if(dice_value==6 and PlayService.multiple_sixes):
                    count=1
                    while(True):
                        value = self.roll_dice()
                        dice_value+=value
                        if value == 6:
                            count+=1
                        else:
                            break    
                        if count==3:
                            dice_value=0
                            break

                         
                next_position = self.move_player(current_position, dice_value)
                player.updatePosition(next_position)
                print(f'Player {player.name} rolled a {dice_value} has moved from {current_position} to {next_position}')
                if(self.check_win(player)):
                    print(f'Player {player.name} has won the game')
                    self.number_of_players-=1
                    self.players.remove(player)
                
                if self.number_of_players==1:
                    break
                

