A python program to simulate the snakes and ladders games</br>
The program currently takes input in the format</br>
s -> number of snakes</br>
head, tail -> head and tail positions of s snakes</br>
l -> number of ladders</br>
start, end -> start and end positions of l ladders</br>
p -> number of players</br>
name -> name of n players</br>


Example Input:
<code> 9
62 5
33 6
49 9
88 16
41 20
56 53
98 64
93 73
95 75
8
2 37
27 46
10 32
51 68
61 79
65 84
71 91
81 100
2
Gaurav
Sagar
</code>

Example output:
<code>
Player Gaurav rolled a 5 has moved from 0 to 5
Player Sagar rolled a 3 has moved from 0 to 3
Player Gaurav rolled a 1 has moved from 5 to 6
Player Sagar rolled a 4 has moved from 3 to 7
Player Gaurav rolled a 1 has moved from 6 to 7
Player Sagar rolled a 5 has moved from 7 to 12
Player Gaurav rolled a 5 has moved from 7 to 12
Player Sagar rolled a 4 has moved from 12 to 16
Player Gaurav rolled a 4 has moved from 12 to 16
Player Sagar rolled a 6 has moved from 16 to 22
Player Gaurav rolled a 5 has moved from 16 to 21
Player Sagar rolled a 4 has moved from 22 to 26
Player Gaurav rolled a 1 has moved from 21 to 22
Player Sagar rolled a 5 has moved from 26 to 31
Player Gaurav rolled a 3 has moved from 22 to 25
Player Sagar rolled a 3 has moved from 31 to 34
Player Gaurav rolled a 3 has moved from 25 to 28
Player Sagar rolled a 2 has moved from 34 to 36
Player Gaurav rolled a 1 has moved from 28 to 29
Player Sagar rolled a 6 has moved from 36 to 42
Player Gaurav rolled a 4 has moved from 29 to 6
Player Sagar rolled a 3 has moved from 42 to 45
Player Gaurav rolled a 6 has moved from 6 to 12
Player Sagar rolled a 4 has moved from 45 to 9
Player Gaurav rolled a 2 has moved from 12 to 14
Player Sagar rolled a 2 has moved from 9 to 11
Player Gaurav rolled a 3 has moved from 14 to 17
Player Sagar rolled a 6 has moved from 11 to 17
Player Gaurav rolled a 4 has moved from 17 to 21
Player Sagar rolled a 1 has moved from 17 to 18
Player Gaurav rolled a 1 has moved from 21 to 22
Player Sagar rolled a 5 has moved from 18 to 23
Player Gaurav rolled a 2 has moved from 22 to 24
Player Sagar rolled a 4 has moved from 23 to 46
Player Gaurav rolled a 1 has moved from 24 to 25
Player Sagar rolled a 3 has moved from 46 to 9
Player Gaurav rolled a 6 has moved from 25 to 31
Player Sagar rolled a 4 has moved from 9 to 13
Player Gaurav rolled a 6 has moved from 31 to 37
Player Sagar rolled a 5 has moved from 13 to 18
Player Gaurav rolled a 3 has moved from 37 to 40
Player Sagar rolled a 2 has moved from 18 to 20
Player Gaurav rolled a 5 has moved from 40 to 45
Player Sagar rolled a 6 has moved from 20 to 26
Player Gaurav rolled a 1 has moved from 45 to 46
Player Sagar rolled a 6 has moved from 26 to 32
Player Gaurav rolled a 1 has moved from 46 to 47
Player Sagar rolled a 6 has moved from 32 to 38
Player Gaurav rolled a 1 has moved from 47 to 48
Player Sagar rolled a 5 has moved from 38 to 43
Player Gaurav rolled a 1 has moved from 48 to 9
Player Sagar rolled a 5 has moved from 43 to 48
Player Gaurav rolled a 4 has moved from 9 to 13
Player Sagar rolled a 6 has moved from 48 to 54
Player Gaurav rolled a 1 has moved from 13 to 14
Player Sagar rolled a 5 has moved from 54 to 59
Player Gaurav rolled a 2 has moved from 14 to 16
Player Sagar rolled a 1 has moved from 59 to 60
Player Gaurav rolled a 5 has moved from 16 to 21
Player Sagar rolled a 1 has moved from 60 to 79
Player Gaurav rolled a 1 has moved from 21 to 22
Player Sagar rolled a 1 has moved from 79 to 80
Player Gaurav rolled a 6 has moved from 22 to 28
Player Sagar rolled a 6 has moved from 80 to 86
Player Gaurav rolled a 1 has moved from 28 to 29
Player Sagar rolled a 5 has moved from 86 to 91
Player Gaurav rolled a 5 has moved from 29 to 34
Player Sagar rolled a 1 has moved from 91 to 92
Player Gaurav rolled a 3 has moved from 34 to 37
Player Sagar rolled a 2 has moved from 92 to 94
Player Gaurav rolled a 1 has moved from 37 to 38
Player Sagar rolled a 4 has moved from 94 to 64
Player Gaurav rolled a 1 has moved from 38 to 39
Player Sagar rolled a 2 has moved from 64 to 66
Player Gaurav rolled a 1 has moved from 39 to 40
Player Sagar rolled a 4 has moved from 66 to 70
Player Gaurav rolled a 2 has moved from 40 to 42
Player Sagar rolled a 3 has moved from 70 to 73
Player Gaurav rolled a 4 has moved from 42 to 46
Player Sagar rolled a 4 has moved from 73 to 77
Player Gaurav rolled a 6 has moved from 46 to 52
Player Sagar rolled a 2 has moved from 77 to 79
Player Gaurav rolled a 2 has moved from 52 to 54
Player Sagar rolled a 1 has moved from 79 to 80
Player Gaurav rolled a 6 has moved from 54 to 60
Player Sagar rolled a 4 has moved from 80 to 84
Player Gaurav rolled a 1 has moved from 60 to 79
Player Sagar rolled a 2 has moved from 84 to 86
Player Gaurav rolled a 4 has moved from 79 to 83
Player Sagar rolled a 3 has moved from 86 to 89
Player Gaurav rolled a 1 has moved from 83 to 84
Player Sagar rolled a 4 has moved from 89 to 73
Player Gaurav rolled a 6 has moved from 84 to 90
Player Sagar rolled a 3 has moved from 73 to 76
Player Gaurav rolled a 2 has moved from 90 to 92
Player Sagar rolled a 1 has moved from 76 to 77
Player Gaurav rolled a 6 has moved from 92 to 64
Player Sagar rolled a 6 has moved from 77 to 83
Player Gaurav rolled a 2 has moved from 64 to 66
Player Sagar rolled a 4 has moved from 83 to 87
Player Gaurav rolled a 1 has moved from 66 to 67
Player Sagar rolled a 2 has moved from 87 to 89
Player Gaurav rolled a 4 has moved from 67 to 91
Player Sagar rolled a 2 has moved from 89 to 91
Player Gaurav rolled a 1 has moved from 91 to 92
Player Sagar rolled a 2 has moved from 91 to 73
Player Gaurav rolled a 4 has moved from 92 to 96
Player Sagar rolled a 6 has moved from 73 to 79
Player Gaurav rolled a 5 to move from 96 to 96
Player Sagar rolled a 3 has moved from 79 to 82
Player Gaurav rolled a 5 to move from 96 to 96
Player Sagar rolled a 3 has moved from 82 to 85
Player Gaurav rolled a 2 has moved from 96 to 64
Player Sagar rolled a 6 has moved from 85 to 91
Player Gaurav rolled a 4 has moved from 64 to 68
Player Sagar rolled a 5 has moved from 91 to 96
Player Gaurav rolled a 2 has moved from 68 to 70
Player Sagar rolled a 6 to move from 96 to 96
Player Gaurav rolled a 3 has moved from 70 to 73
Player Sagar rolled a 1 has moved from 96 to 97
Player Gaurav rolled a 3 has moved from 73 to 76
Player Sagar rolled a 4 to move from 97 to 97
Player Gaurav rolled a 2 has moved from 76 to 78
Player Sagar rolled a 3 has moved from 97 to 100
Player Sagar has won the game
</code>

Important points:
1. Game is played until one player remains to win
2. the number of dice to be used can be specified, default is one.
3. The size of board can be specified, default is 100