import random
class Field:
    def __init__(self):
        self.grid = []
        for _ in range(5):
            self.grid.append(["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"])

    def printGrid(self):
        for x in range(5):
            print(''.join(self.grid[x]))


class Animal:
    def __init__(self, field):
        self.positionY = 0
        self.positionX = 0
        self.Field = field

    def walk(self, name):
        while True:
            newY, newX = self.positionY + random.choice([-1, 0, 1]), self.positionX + random.choice([-1, 0, 1])
            if 0 <= newY < 5 and 0 <= newX < 5 and self.Field.grid[newY][newX] == "[ ]":
                break

        self.Field.grid[self.positionY][self.positionX] = "[ ]"
        self.positionY, self.positionX = newY, newX
        self.Field.grid[self.positionY][self.positionX] = name

class Predator(Animal):
    def __init__(self, field):
        super().__init__(field)
        self.state = 0
        self.Field.grid[0][0] = "[T]"
        self.TargetY = 0
        self.TargetX = 0
        self.done = False

    def printState(self):
        if self.state == 0:
            print("Тигр охотится")
        elif self.state == 1:
            print("Тигр атакует!")
        else:
            print("Тигр поймал добычу и идёт в своё логово")

    def act(self):
        if self.state == 0:
            self.hunt()
        elif self.state == 1:
            self.attack()
        else:
            self.goHome()

    def hunt(self):
        self.walk("[T]")
        for closeY in range(self.positionY - 1, self.positionY + 2):
            for closeX in range(self.positionX - 1, self.positionX + 2):
                if (closeX < 0 or closeY < 0) or (closeX > 4 or closeY > 4):
                    continue
                if self.Field.grid[closeY][closeX] == "[З]":
                    self.state = 1
                    self.TargetY = closeY
                    self.TargetX = closeX

    def attack(self):
        self.done = bool(random.randint(0, 1))
        if self.done:
            self.Field.grid[self.TargetY][self.TargetX] = "[ ]"
            self.state = 2
        if not self.done:
            self.state = 0
            print("Тигр промахнулся")

    def goHome(self):
        self.Field.grid[self.positionY][self.positionX] = "[ ]"
        self.positionY, self.positionX = 0, 0
        self.Field.grid[self.positionY][self.positionX] = "[T]"




class Prey(Animal):
    def __init__(self, field):
        super().__init__(field)
    def Spawn(self):
        while True:
            self.positionY = random.randint(0,4)
            self.positionX = random.randint(0, 4)
            if self.positionY > 1 and self.positionX > 1 and self.Field.grid[self.positionY][self.positionX] == "[ ]":
                self.Field.grid[self.positionY][self.positionX] = "[З]"
                break


    def Hop(self):
        self.walk("[З]")



class Simulation:
    def __init__(self):
        self.HuntingGrounds = Field()
        self.Tiger = Predator(self.HuntingGrounds)
        self.Rabbit1 = Prey(self.HuntingGrounds)
        self.Rabbit2 = Prey(self.HuntingGrounds)

    def Start(self):
        print("Начало симуляции")
        self.Rabbit1.Spawn()
        self.Rabbit2.Spawn()
        self.HuntingGrounds.printGrid()
        self.Tiger.printState()
        proceed = input()
        self.Loop()

    def Loop(self):
        while not self.Tiger.done:
            if not self.Tiger.state == 1:
                self.Rabbit1.Hop()
                self.Rabbit2.Hop()
            self.Tiger.act()
            self.HuntingGrounds.printGrid()
            self.Tiger.printState()
            proceed = input()
        self.End()

    def End(self):
        self.Tiger.act()
        self.HuntingGrounds.printGrid()
        print("Конец симуляции")
        proceed = input()



Simulator = Simulation()
Simulator.Start()