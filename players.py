
class Defence:
    def __init__(self, reaction:float, block:float, headplay:float):
        self.reaction=reaction
        self.block=block
        self.headplay=headplay

class Attack:
    def __init__(self, speed:float, shoot:float, marksman:float):
        self.speed=speed
        self.shoot=shoot
        self.marksman=marksman

class Phisical:
    def __init__(self, endurance:float, hight:int, weight:int):
        self.endurance=endurance
        self.hight=hight
        self.weight=weight

class Player:
    def __init__(self, name:str, number:int, attack:Attack, defence:Defence, phisical:Phisical):
        self.name=name
        self.number=number
        self.defence=Defence
        self.attack=Attack
        self.phisical=Phisical