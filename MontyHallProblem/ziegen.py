import random

doors = []

class Door(object):
    def __init__(self, id):
        self.car = False #random.choise
        self.chosen = False #
        self.id = id #number of a door

class MontyHall(object):
    def __init__(self, door_count):  #initialisierung alle Tueren
        del doors[:]
        for i in range(door_count):
            doors.append(Door("" + str(i + 1)))
        self.prize_door = random.choice(doors)
        self.prize_door.car = True

    def choose(self, id):   #change chosen = true
        doors[int(id) - 1].chosen = True
        self.chosen_door = doors[int(id) - 1]

    def choose_random(self):    #fuer beliebige Tuer
        self.chosen_door = random.choice(doors)
        self.chosen_door.chosen = True

    def open_empty_doors(self): #moderator opened all the doors except 2
        doors_to_open = set()
        if (self.prize_door == self.chosen_door): #1
            self.second_door = random.choice(doors) #2
            while self.second_door == self.chosen_door:
                self.second_door = random.choice(doors)
            for i in range(len(doors)):
                if (doors[i] != self.second_door and doors[i] != self.chosen_door):
                    doors_to_open.add(doors[i].id)# all the rest adding to set
        else:
            self.second_door = self.prize_door
            for i in range(len(doors)):
                if(doors[i] != self.chosen_door and doors[i] != self.prize_door): #1 and 2
                    doors_to_open.add(doors[i].id) # all the rest adding to set

        return doors_to_open

    def open_door(self, swap):  # chosen_door, second_door
        if swap == True:
            alternative_door = self.chosen_door
            self.chosen_door = self.second_door
            self.second_door = alternative_door
            self.chosen_door.chosen = True
            self.second_door.chosen = False
        return self.chosen_door.car



def simulate(doornumber = 5, runs = 100, swap = True):        #simulate the always-Swap-Strategy
    guess_count_true = 0
    guess_count_false = 0
    for i in range(runs):
        my_game = MontyHall(doornumber)
        my_game.choose("5")
        my_game.open_empty_doors()
        if my_game.open_door(swap) == True:
            guess_count_true = guess_count_true + 1
        else:
            guess_count_false = guess_count_false + 1

    print "Gewinnt: " + str(guess_count_true) + " Lost: " + str(guess_count_false)





def play(doornumber = 3):
    my_game = MontyHall(doornumber)



if __name__ == "__main__":
    print str(simulate())
    print "test"