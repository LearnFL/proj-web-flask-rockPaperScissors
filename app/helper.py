import random

alist = ['rock','paper', 'scissors']

adict = {
    'paper': {
        'scissors': 0,
        'paper': 1,
        'rock': 2
    },
    'rock': {
        'paper': 0,
        'rock': 1,
        'scissors': 2
    },
    'scissors': {
        'rock': 0,
        'scissors': 1,
        'paper': 2
    }
}

winner = ['Human Wins!', 'Good job, you have won!', 'And human wins again!', 'Winner-winner chicken dinner!',
            'Alright, human wins!', 'Congrats you won!', 'You are the winner!', 'Woohooo you won!', 'Computer is in tears, human wins!']
loser = ['Computer wins!', 'AI wins!', 'Skynet wins!', 'Cyber brain wins!', 'There is no shame in loosing! YOU LOST!',
            'Ha-ha you lost!', 'Better luck next time, you lost buddy!', 'You lost!', 'Skynet is rising, T1000 has won!', 'No one is perfect, you lost!']

count_human = 0
count_computer = 0

class Game:
    def __init__(self, human_choice, alist, adict, winner, loser, game=None):
        self.game = game
        self.alist = alist
        self.adict = adict
        self.winner = winner
        self.loser = loser
        self.human_choice = human_choice
        self.computer_choice = None
        self.message = None
        self.who_won = None
  
    def rule(self, h, c, winner, loser):
        human = adict.get(h)
        computer = adict.get(c)
        hum = computer.get(h)
        comp = human.get(c)
        if hum < comp:
            self.message = random.choice(winner)
            self.who_won = 'human'
        elif comp < hum:
            self.message = random.choice(loser)
            self.who_won = "computer"
        else:
            self.message = 'DRAW'
    
    def depict (self, x):
        rock = "./images/rock.png"

        paper = "./images/paper.png"

        scissors = "./images/scissors.png"

        if x == 0:
            self.computer_choice = rock
        elif x == 1:
            self.computer_choice = paper
        elif x == 2:
            self.computer_choice = scissors

        return self.computer_choice

    def __call__(self):
        if self.game is None:
            self.human = self.human_choice
            self.comp = random.randint(0, 2)
            print(f'Computer:  {alist[self.comp]}')
            self.depict(self.comp)
            self.human_score = alist[int(self.human)]
            self.computer_score = alist[self.comp]
            self.rule(self.human_score, self.computer_score, self.winner, self.loser)

# game = Game(alist, adict, winner, loser, game=None)
# for i in range(10):
#     game()