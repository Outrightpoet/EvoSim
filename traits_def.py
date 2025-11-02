from name_gen import name_make
from random_store import get_randint_neg_ten_ten, get_randint_zero_five_hundred, get_randint_zero_hundred
from food_groups import foods


class Traits():
    def __init__(self, creature, parent_traits=None, dose_speciate=True):

        self.creature = creature

        self.nutrition_adder = 0

        self.diet_scale = getattr(parent_traits, "diet_scale", 0)
        self.diet_range = getattr(parent_traits, "diet_range", 0)
        self.defensive_spikes = getattr(parent_traits, "defensive_spikes", 0)
        self.diet = getattr(parent_traits, "diet", self.find_diet())
        self.size = getattr(parent_traits, "size", 0)

        self.claws = getattr(parent_traits, "claws", 0)
        self.sharp_teeth = getattr(parent_traits, "sharp_teeth", 0)
        self.thick_skin = getattr(parent_traits, "thick_skin", 0)
        self.bone_plates = getattr(parent_traits, "bone_plates", 0)
        self.scales = getattr(parent_traits, "scales", 0)
        self.tail = getattr(parent_traits, "tail", 0)
        self.club_tail = getattr(parent_traits, "club_tail", 0)
        self.horns = getattr(parent_traits, "horns", 0)
        self.webbed_feet = getattr(parent_traits, "webbed_feet", 0)
        self.hoofs = getattr(parent_traits, "hoofs", 0)
        self.soft_feet = getattr(parent_traits, "soft_feet", 0)
        self.hearing = getattr(parent_traits, "hearing", 0)
        self.camouflage = getattr(parent_traits, "camouflage", 0)
        self.sight = getattr(parent_traits, "sight", 0)

        #not gonna add these rn cuase im lazy
        self.venom = getattr(parent_traits, "venom", 0)
        self.poison = getattr(parent_traits, "poison", 0)
        self.venom_resistance = getattr(parent_traits, "venom_resistance", 0)
        self.poison_resistance = getattr(parent_traits, "poison_resistance", 0)


        self.long_legs = getattr(parent_traits, "long_legs", 0)
        self.dense_muscles = getattr(parent_traits, "dense_muscles", 0)

        #self.place_holder = getattr(parent_traits, "place_holder", 0)

        self.traits = [
            self.diet_scale,
            self.diet_range,
            self.defensive_spikes,
            self.size,
            self.claws,
            self.sharp_teeth,
            self.thick_skin,
            self.bone_plates,
            self.scales,
            self.tail,
            self.club_tail,
            self.horns,
            self.webbed_feet,
            self.hoofs,
            self.soft_feet,
            self.hearing,
            self.camouflage,
            self.sight,

            self.long_legs,
            self.dense_muscles
        ]

        if dose_speciate == True:
            self.speciate()


    def speciate(self):
        for trait in range(len(self.traits)):
            if get_randint_zero_hundred() == 1:

                self.traits[trait] = self.traits[trait] + get_randint_neg_ten_ten()

                if self.traits[trait] > 100:
                    self.traits[trait] = 99
                elif self.traits[trait] < 0:
                    self.traits[trait] = 1

                species = self.creature.species
                species_name = self.creature.species_name
                subspecies_name = self.creature.subspecies_name
                species[species_name][1][subspecies_name][0] -= 1
                name = ((species_name)+"_"+str(len(species[species_name][1])))
                #print(f"{str(name)} about to be created")

                species[species_name][1][str(name)] = [1, {self.creature.id: self.creature}]
                self.creature.subspecies_name = name
                #print(f"{str(name)} created")
                #subspecies = {joe_suaruas_with_horns: [over_all_pop = int, members = [guy2]]}

        (
            self.diet_scale,
            self.diet_range,
            self.defensive_spikes,
            self.size,
            self.claws,
            self.sharp_teeth,
            self.thick_skin,
            self.bone_plates,
            self.scales,
            self.tail,
            self.club_tail,
            self.horns,
            self.webbed_feet,
            self.hoofs,
            self.soft_feet,
            self.hearing,
            self.camouflage,
            self.sight,

            self.long_legs,
            self.dense_muscles
        ) = self.traits

        self.diet = self.find_diet()

    def find_diet(self):

        diet_key = int(self.diet_scale / (100 / len(foods)))
        diet_keys = []
        diet = []

        if self.diet_range > 90:
            diet_keys = [0,1,2,3,4,5,6,7,8,9,10]
            self.nutrition_adder = 3
        elif self.diet_range > 60:
            self.nutrition_adder = 2
            for i in range(diet_key-3,diet_key+4):
                if i >= 0:
                    diet_keys.append(i)
        elif self.diet_range > 30:
            self.nutrition_adder = 1
            for i in range(diet_key-2,diet_key+3):
                if i >= 0:
                    diet_keys.append(i)
        elif self.diet_range > 10:
            self.nutrition_adder = 0
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
            diet.append(0)
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
        creature.size = 15 * grand_multiplyer_pos * ((self.size / 100) if self.size != 0 else .15)
        creature.nutritinal_need = (5 + self.nutrition_adder + (self.defensive_spikes / 200) + (self.size / 100) + (self.claws / 300) + (self.sharp_teeth / 400) +
                                    (self.thick_skin / 100) + (self.bone_plates / 100) + (self.scales / 200) + (self.tail / 200) + (self.horns / 200)
                                    + (self.webbed_feet / 300) + (self.hoofs / 300) + (self.soft_feet / 300) + (self.hearing / 300) + (self.camouflage / 300) + (self.sight / 200)
                                    + (self.long_legs / 100) + (self.dense_muscles / 150) + (self.club_tail / 200)) * grand_multiplyer_pos
        creature.nutritinal_output = 10 * grand_multiplyer_pos

        # stats for encounters
        #speed needs to be an int for sum
        creature.speed = int(5 * grand_multiplyer_neg)
        creature.hiding_power = 1 * grand_multiplyer_neg
        creature.sight_power = 1 * grand_multiplyer_neg

        creature.aquatic_speed = int(2 * grand_multiplyer_neg) * (1 + self.webbed_feet / 150) * (1 + self.tail / 100) / (1 + self.thick_skin / 200) / (1 + self.bone_plates / 50) / (1 + self.scales / 300)
        creature.regular_speed = int(5 * grand_multiplyer_neg) * (1 + self.long_legs / 100) * (1 + self.tail / 150) / (1 + self.thick_skin / 300) / (1 + self.bone_plates / 100) / (1 + self.scales / 200)
        creature.mountainous_speed = int(2 * grand_multiplyer_neg) * (1 + self.hoofs / 50) / (1 + self.thick_skin / 300) / (1 + self.bone_plates / 75) / (1 + self.scales / 100)

        creature.sharp_attacking_power = 5 * grand_multiplyer_pos * (1 + self.claws / 200)  * (1 + self.sharp_teeth / 150) * (1 + self.horns / 300) * (1 + self.dense_muscles / 200)
        creature.blunt_attacking_power = 5 * grand_multiplyer_pos * (1 + self.club_tail / 100) * (1 + self.dense_muscles / 200)
        creature.piercing_attacking_power = 5 * grand_multiplyer_pos * (1 + self.horns / 100) * (1 + self.dense_muscles / 200)

        creature.reach = 1 * (creature.size/15) * (1 + self.horns / 50)

        creature.attack_moves = ["bite"]
        if self.claws >= 30:
            creature.attack_moves.append("claw")
        if self.tail >= 40:
            creature.attack_moves.append("tail whip")
        elif self.tail >= 40 and self.claws >= 30:
            creature.attack_moves.append("club")
        if self.horns >= 30:
            creature.attack_moves.append("horn stab")
        if self.long_legs > 40:
            creature.attack_moves.append("stomp")




        creature.tempature_resistance = [20, 90]

        creature.list_priority = creature.speed / creature.nutritinal_need
