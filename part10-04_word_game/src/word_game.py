# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            return 0

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        vowel_1 = 0
        vowel_2 = 0

        for el in player1_word:
            if el in ('a', 'e', 'i', 'o', 'u'):
                vowel_1 += 1
            
        for el in player2_word:
            if el in ('a', 'e', 'i', 'o', 'u'):
                vowel_2 += 1

        if vowel_2 > vowel_1:
            return 2
        elif vowel_1 > vowel_2:
            return 1
        else:
            return 0
            

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        
        valid_1 = True
        valid_2 = True

        if player1_word not in ('rock', 'scissors', 'paper'):
            valid_1 = False

        if player2_word not in ('rock', 'scissors', 'paper'):
            valid_2 = False
        
        if not valid_1 and valid_2:
            return 2
        elif not valid_2 and valid_1:
            return 1
        elif not valid_1 and not valid_2:
            return 0
        
        if player1_word == 'rock' and player2_word == 'scissors':
            return 1
        elif player2_word == 'rock' and player1_word == 'scissors':
            return 2
        elif player2_word == 'rock' and player1_word == 'paper':
            return 1
        elif player1_word == 'rock' and player2_word == 'paper':
            return 2
        elif player2_word == 'paper' and player1_word == 'scissors':
            return 1
        elif player1_word == 'paper' and player2_word == 'scissors':
            return 2
        else:
            return 0