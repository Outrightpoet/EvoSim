import random
from hunt_def import hunt

class Location():
    def __init__(self,area_map, row_col):


        self.foods = {
            # Plants / Fungi / Insects with abundance levels [high, medium, low]
            "plants": [25, 25, 25],
            "leaves": [25, 25, 25],
            "fruits": [25, 25, 25],
            "nuts": [25, 25, 25],
            "fungi": [25, 25, 25],
            "insects": [25, 25, 25],

            # Single abundance / low only
            "seeds": [25],
            "roots": [25],
            "detritus": [25],
            "fish": [25],
        }

        # Maximum values
        self.max_foods = {
            "plants": [20, 40, 60],
            "leaves": [20, 40, 60],
            "fruits": [10, 30, 50],
            "nuts": [20, 30, 40],
            "fungi": [50, 40, 30],
            "insects": [50, 20, 10],
            "seeds": [30],
            "roots": [20],
            "detritus": [30],
            "fish": [20],
        }


        self.area_map = area_map
        self.row_col = row_col
        self.inhabitants = {}
        self.climate = 60
        self.terrain = "none"
        #terrain value for heat map
        self.terrain_value = -1
        #for the start its just going to be plant growth but i can add things like terrain as well
		#for example mountainous or swampy

    def change_terrain(self, new_terrain, new_terrain_value):
        self.terrain = new_terrain
        self.terrain_value = new_terrain_value
        if new_terrain == "marshes":
            self.max_foods = {
                "plants": [20, 30, 0],
                "leaves": [10, 20, 0],
                "fruits": [0, 0, 0],
                "nuts": [0, 0, 0],
                "fungi": [20, 10, 0],
                "insects": [60, 30, 0],
                "seeds": [10],
                "roots": [10],
                "detritus": [20],
                "fish": [80]
            }
        elif new_terrain == "plains":
            self.max_foods = {
                "plants": [20, 40, 60],
                "leaves": [20, 40, 60],
                "fruits": [10, 30, 50],
                "nuts": [20, 30, 40],
                "fungi": [50, 40, 30],
                "insects": [50, 20, 10],
                "seeds": [30],
                "roots": [20],
                "detritus": [30],
                "fish": [0]
            }
        elif new_terrain == "forests":
            self.max_foods = {
                "plants": [40, 60, 80],
                "leaves": [40, 60, 80],
                "fruits": [20, 40, 70],
                "nuts": [20, 30, 40],
                "fungi": [50, 40, 40],
                "insects": [50, 20, 30],
                "seeds": [40],
                "roots": [40],
                "detritus": [40],
                "fish": [0]
            }
        elif new_terrain == "mountains":
            self.max_foods = {
                "plants": [10, 20, 30],
                "leaves": [10, 20, 30],
                "fruits": [5, 10, 0],
                "nuts": [15, 10, 20],
                "fungi": [20, 10, 10],
                "insects": [20, 10, 10],
                "seeds": [10],
                "roots": [5],
                "detritus": [10],
                "fish": [0]
            }
        elif new_terrain == "savanna":
            self.max_foods = {
                "plants": [10, 10, 10],
                "leaves": [0, 0, 10],
                "fruits": [0, 0, 0],
                "nuts": [0, 0, 0],
                "fungi": [0, 0, 0],
                "insects": [10, 10, 5],
                "seeds": [5],
                "roots": [0],
                "detritus": [10],
                "fish": [0]
            }
        elif new_terrain == "desert":
            self.max_foods = {
                "plants": [5, 5, 0],
                "leaves": [0, 0, 0],
                "fruits": [5, 5, 5],
                "nuts": [0, 0, 0],
                "fungi": [0, 0, 0],
                "insects": [5, 5, 0],
                "seeds": [0],
                "roots": [0],
                "detritus": [5],
                "fish": [0]
            }

    def grow(self):
        for item in self.foods:
            if item != "detritus":
                for i in range(0,len(self.foods[item])-1):
                    self.foods[item][i] += self.max_foods[item][i] / 10
                    if self.foods[item][i] == 0:
                        if random.randint(0,1) == 1:
                            self.foods[item][i] = 5
                    elif self.foods[item][i] > self.max_foods[item][i]:
                        self.foods[item][i] = self.max_foods[item][i]
            else:
                self.foods[item][0] = self.foods[item][0] / 2
                if self.foods[item][0] > self.max_foods[item][0]:
                    self.foods[item][0] = self.max_foods[item][0]


    def check_for_food(self, foods, nutritinal_need, creature):

        height_key = foods[len(foods)-1]
        foods = list(foods)
        foods.pop(len(foods)-1)
        random.shuffle(foods)

        for food_group in foods:
            if food_group != "creatures":
                try:
                    if self.foods[food_group][height_key] >= nutritinal_need:
                        self.foods[food_group][height_key] -= nutritinal_need
                        return True
                except IndexError:
                    if self.foods[food_group][0] >= nutritinal_need:
                        self.foods[food_group][0] -= nutritinal_need
                        return True
            else:
                possible_eating_list = []
                for target in self.inhabitants.values():
                    if target.species_name != creature.species_name:
                        if target.nutritinal_output >= creature.nutritinal_need:
                            try:
                                if target.traits == None:
                                    pass
                                possible_eating_list.append(target)
                                if len(possible_eating_list) >= 3:
                                    break
                            except AttributeError:
                                pass
                for target in possible_eating_list:
                    if hunt(creature, target):
                        return True

        return False

