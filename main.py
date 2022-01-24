from PlayService import  PlayService

BOARD_SIZE = 100

def get_input():
    number_of_snakes = int(input())
    snakes_positions = dict()
    for i in range(number_of_snakes):
        head, tail = [int(x) for x in input().split()]
        snakes_positions[head] = tail

    number_of_ladders = int(input())
    ladders_positions = dict()
    for i in range(number_of_ladders):
        start,end = [int(x) for x in input().split()]
        ladders_positions[start] = end

    number_of_players = int(input())
    players = []
    for i in range(number_of_players):
        name = input()
        players.append(name)
    
    return (snakes_positions,ladders_positions,players)


def play_game(snakes_positions, ladders_positions, players):

    service = PlayService(BOARD_SIZE, snakes_positions, ladders_positions, players)
    service.play()

if __name__ == '__main__':
    snakes_positions, ladders_positions, players = get_input()
    play_game(snakes_positions, ladders_positions, players)
    
     