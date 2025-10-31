import random
from name_gen import name_make
from food_groups import *


class Traits():
    def __init__(self, creature, parent_traits=None, dose_speciate=True):

        self.creature = creature

        if parent_traits == None:
            self.diet_scale = 0
            self.diet_range = 0
            self.defensive_spikes = 0
            self.diet = self.find_diet()
        else:
            # 0-100 herbivore to carnivore
            self.diet_scale = parent_traits.diet_scale
            self.diet_range = parent_traits.diet_range
            self.defensive_spikes = parent_traits.defensive_spikes
            self.diet = parent_traits.diet

        self.traits = [self.diet_scale, self.diet_range, self.defensive_spikes]

        if dose_speciate == True:
            self.speciate()


    def speciate(self):
        for trait in range(len(self.traits)):
            if random.randint(0,100*len(self.traits)) == 1:

                self.traits[trait] = self.traits[trait] + random.randint(-10,10)

                if self.traits[trait] > 100:
                    self.traits[trait] = 99
                elif self.traits[trait] < 0:
                    self.traits[trait] = 1

                species = self.creature.species
                species_name = self.creature.species_name
                subspecies_name = self.creature.subspecies_name
                name = ((species_name)+"_"+str(len(species[species_name][1])))
                #print(f"{str(name)} about to be created")

                species[species_name][1][str(name)] = [1, {self.creature.id: self.creature}]
                self.creature.subspecies_name = name
                #print(f"{str(name)} created")
                #subspecies = {joe_suaruas_with_horns: [over_all_pop = int, members = [guy2]]}

        self.diet_scale, self.diet_range, self.defensive_spikes = self.traits
        self.diet = self.find_diet()

    def find_diet(self):

        diet_key = int(self.diet_scale / (100 / len(foods)))
        diet_keys = []
        diet = []
        diet_clean = []

        if self.diet_range > 90:
            diet_keys = [0,1,2,3,4,5,6,7,8,9,10]
        elif self.diet_range > 60:
            for i in range(diet_key-3,diet_key+4):
                if i >= 0:
                    diet_keys.append(i)
        elif self.diet_range > 30:
            for i in range(diet_key-2,diet_key+3):
                if i >= 0:
                    diet_keys.append(i)
        elif self.diet_range > 10:
            for i in range(diet_key-1,diet_key+2):
                if i >= 0:
                    diet_keys.append(i)
        else:
            diet_keys = [diet_key]

        if self.creature.size >= 20:
            for i in diet_keys:
                try:
                    diet.append(foods[i])
                except IndexError:
                    pass
            diet.append(2)
        elif 20 > self.creature.size >= 10:
            for i in diet_keys:
                try:
                    diet.append(foods[i])
                except IndexError:
                    pass
            diet.append(1)
        else:
            for i in diet_keys:
                try:
                    diet.append(foods[i])
                except IndexError:
                    pass
            diet.append(1)
        return diet

    def get_stats(self, creature, age_group):

        if age_group == "child":
            grand_multiplyer_pos = .5
            grand_multiplyer_neg = 1.5
        elif age_group == "adult":
            grand_multiplyer_pos = 1
            grand_multiplyer_neg = 1
        else:
            grand_multiplyer_pos = 1.5
            grand_multiplyer_neg = .5

        creature.adult_age = 3
        creature.elderly_age = 8
        creature.lifespan = 10
        creature.size = 15 * grand_multiplyer_pos
        creature.nutritinal_need = 5 * grand_multiplyer_pos
        creature.nutritinal_output = 10 * grand_multiplyer_pos

        # stats for encounters
        #speed needs to be an int for sum
        creature.speed = int(5 * grand_multiplyer_neg)
        creature.hiding_power = 1 * grand_multiplyer_neg
        creature.sight_power = 1 * grand_multiplyer_neg

        creature.aquatic_speed = int(2 * grand_multiplyer_neg)
        creature.regular_speed = int(5 * grand_multiplyer_neg)
        creature.mountainous_speed = int(2 * grand_multiplyer_neg)

        creature.sharp_attacking_power = 5 * grand_multiplyer_pos
        creature.blunt_attacking_power = 5 * grand_multiplyer_pos
        creature.piercing_attacking_power = 5 * grand_multiplyer_pos

        creature.pure_defensive_power = 1 * grand_multiplyer_pos
        creature.blunt_defensive_power = 1 * grand_multiplyer_pos

        creature.reach = 1 * (creature.size/15)

        creature.attack_moves = ["bite"]

        creature.tempature_resistance = [20, 90]

        creature.list_priority = creature.speed / creature.nutritinal_need
