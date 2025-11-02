from random_store import get_randint_zero_one
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
            "seeds": [25, 0, 0],
            "roots": [25, 0, 0],
            "detritus": [25, 0, 0],
            "fish": [25, 0, 0],
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
                "seeds": [10, 5, 0],
                "roots": [10, 5, 0],
                "detritus": [20, 0, 0],
                "fish": [80, 80, 80]
            }
        elif new_terrain == "plains":
            self.max_foods = {
                "plants": [30, 40, 0],
                "leaves": [30, 40, 0],
                "fruits": [5, 0, 0],
                "nuts": [10, 0, 0],
                "fungi": [10, 5, 0],
                "insects": [20, 10, 0],
                "seeds": [20, 10, 0],
                "roots": [10, 10, 0],
                "detritus": [30, 0, 0],
                "fish": [0, 0, 0]
            }
        elif new_terrain == "forests":
            self.max_foods = {
                "plants": [20, 40, 60],
                "leaves": [20, 40, 60],
                "fruits": [10, 20, 40],
                "nuts": [10, 20, 30],
                "fungi": [30, 20, 20],
                "insects": [25, 10, 15],
                "seeds": [20, 10, 0],
                "roots": [20, 10, 0],
                "detritus": [30, 0, 0],
                "fish": [0, 0, 0]
            }
        elif new_terrain == "mountains":
            self.max_foods = {
                "plants": [10, 20, 30],
                "leaves": [10, 20, 30],
                "fruits": [5, 10, 0],
                "nuts": [15, 10, 20],
                "fungi": [20, 10, 10],
                "insects": [20, 10, 10],
                "seeds": [10, 10, 0],
                "roots": [5, 10, 0],
                "detritus": [10, 0, 0],
                "fish": [0, 0, 0]
            }
        elif new_terrain == "savanna":
            self.max_foods = {
                "plants": [10, 10, 10],
                "leaves": [0, 0, 10],
                "fruits": [0, 0, 0],
                "nuts": [0, 0, 0],
                "fungi": [0, 0, 0],
                "insects": [10, 10, 5],
                "seeds": [5, 2, 0],
                "roots": [0, 0, 0],
                "detritus": [10, 0, 0],
                "fish": [0, 0, 0]
            }
        elif new_terrain == "desert":
            self.max_foods = {
                "plants": [5, 5, 0],
                "leaves": [0, 0, 0],
                "fruits": [5, 5, 5],
                "nuts": [0, 0, 0],
                "fungi": [0, 0, 0],
                "insects": [5, 5, 0],
                "seeds": [0, 0, 0],
                "roots": [0, 0, 0],
                "detritus": [5, 0, 0],
                "fish": [0, 0, 0]
            }

    def grow(self):
        for item in self.foods:
            if item != "detritus":
                for i in range(0,len(self.foods[item])-1):
                    self.foods[item][i] += self.max_foods[item][i] / 10
                    if self.foods[item][i] == 0:
                        if get_randint_zero_one == 1:
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
        #random.shuffle(foods)

        for food_group in foods:
            if food_group != "creatures":

                if self.foods[food_group][height_key] >= nutritinal_need:
                    self.foods[food_group][height_key] -= nutritinal_need
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

