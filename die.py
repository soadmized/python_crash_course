import random

class Die():

    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        result = random.randint(1, self.sides)
        print("There is a {}!!".format(result))
        return result

if __name__ == "__main__":

    die = Die(10)
    for i in range(1, 10):
        die.roll_die()