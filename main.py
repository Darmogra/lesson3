import random
class Human:
    def __init__(self, name= "Andriy", job= None, home= None, car= None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.gladness = 50
        self.stiety = 50
    def get_home(self):
        pass
    def get_car(self):
        pass
    def get_job(self):
        pass
    def eat(self):
        pass
    def work(self):
        pass
    def shopping(self):
        pass
    def chill(self):
        pass
    def clear_home(self):
        pass
    def days_indexes(self, day):
        pass
    def is_alive(self):
        pass
    def live(self, day):
        pass
class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']
brands_of_car = {'тазік':{'fuel': 2, 'strength': 180, 'consumption' : 10},
                'корито':{'fuel': 5, 'strength': 174, 'consumption' : 17},
                'феррарі':{'fuel': 70, 'strength': 2000, 'consumption' : 233}},
