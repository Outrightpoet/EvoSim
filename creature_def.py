from traits_def import Traits
from name_gen import name_make
from id_getter import gen_id
from group_def import Group
from random_store import get_randint_zero_hundred, get_randint_zero_thirty, get_randint_neg_one_one

class Creature():
    __slots__ = (
        "age", "age_group", "adult_age", "elderly_age", "lifespan", "size",
        "nutritinal_need", "nutritinal_output", "malnurished", "list_priority",
        "speed", "hiding_power", "sight_power",
        "aquatic_speed", "regular_speed", "mountainous_speed",
        "sharp_attacking_power", "blunt_attacking_power", "piercing_attacking_power", "reach",
        "attack_moves", "combat_effects", "tempature_resistance",
        "group", "parent", "location", "species_name", "species", "subspecies_name",
        "id", "parent_list", "traits"
    )
    def __init__(self, id, parent_list, species_name, species, location, subspecies_name, parent=None, speciate=True):
        #these are all the basic stat templates and are subject to change
        self.age = 0
        self.age_group = "child"
        self.adult_age = 3
        self.elderly_age = 8
        self.lifespan = 10
        self.size = 15
        self.nutritinal_need = 5
        self.nutritinal_output = 10
        self.malnurished = False
        self.list_priority = 0

        #stats for encounters
        self.speed = 5
        self.hiding_power = 1
        self.sight_power = 1

        self.aquatic_speed = 2
        self.regular_speed = 5
        self. mountainous_speed = 2

        self.sharp_attacking_power = 5
        self.blunt_attacking_power = 5
        self.piercing_attacking_power = 5

        self.reach = 1

        self.attack_moves = ["bite"]
        #ideas for this are like defensive spike and thick skin
        self.combat_effects = []

        self.tempature_resistance = [20,90]


        #testing stats
        #TODO
        #group implmentation will be for pack hunting and child protection
        self.group = Group(self)


        self.parent=parent
        self.location=location
        self.species_name=species_name
        self.species=species
        self.subspecies_name = subspecies_name
        self.id=id
        self.parent_list=parent_list
        self.location.inhabitants[self.id] = self

        self.species[self.species_name][2][id] = self

        if self.parent != None:
            self.traits = Traits(self, self.parent.traits, speciate)
        else:
            self.traits = Traits(self, self.parent, speciate)

        self.traits.get_stats(self, "child")


    def identify(self):
        print(f"self.id = {self.id}\nself.species_name = {self.species_name}\nself.age = {self.age}\nself.traits = ")


    def cycle(self):
        if self.health_check():
            self.find_food()


    def check_and_split(self):

        pop_needed_for_divergence = 10

        if self.subspecies_name != "base_strain" and len(self.species[self.species_name][1][self.subspecies_name][1]) >= pop_needed_for_divergence:

            name = name_make()
            creatures_moveing = {}
            old_species = self.species_name
            old_subspecies = self.subspecies_name

            for i in self.species[self.species_name][1][self.subspecies_name][1]:
                creatures_moveing[i] = self.species[self.species_name][1][self.subspecies_name][1][i]


            self.species[self.species_name][0] -= pop_needed_for_divergence
            self.species[self.species_name][1][self.subspecies_name][0] -= pop_needed_for_divergence


            self.species[name] = [pop_needed_for_divergence,{"base_strain": [pop_needed_for_divergence, creatures_moveing]}, creatures_moveing]

            for creature in self.species[name][2].values():
                del self.species[old_species][2][creature.id]
                creature.species_name = name
                creature.subspecies_name = "base_strain"

            self.species[old_species][1][old_subspecies] = [0, [], f"Seperated to {name}"]

            if self.species[old_species][0] == 0:
                del self.species[old_species]





    def health_check(self):
        self.age += 1
        if self.age == self.adult_age:
            self.age_group = "adult"
            self.traits.get_stats(self, self.age_group)
        elif self.age == self.elderly_age:
            self.age_group = "elder"
            self.traits.get_stats(self, self.age_group)

        ran = get_randint_zero_hundred()
        if self.age >= self.elderly_age and ran < (50 * (self.age/self.lifespan)):
            self.die()
            return False
        return True


    def find_food(self):

        food_avalible = self.location.check_for_food(self.traits.diet, self.nutritinal_need, self)

        if food_avalible == True:
            if self.malnurished == True:
                self.malnurished = False
            else:
                if self.age_group == "adult":
                    self.freaky()
            if get_randint_zero_thirty == 30:
                self.random_move()
        else:
            self.random_move()
            if self.location.check_for_food(self.traits.diet, self.nutritinal_need, self):
                if self.malnurished == True:
                    self.malnurished = False
                else:
                    if self.age_group == "adult":
                        self.freaky()
            else:
                if self.malnurished == True:
                    self.die()
                else:
                    self.malnurished = True


    def freaky(self):
        id = gen_id()
        child = Creature(id, self.parent_list, self.species_name, self.species, self.location, self.subspecies_name, self)
        # def __init__(self, id, parent_list, species_name, species, location, subspecies_name, parent=None, speciate=True):
        child.parent_list[id] = child
        child.species[child.species_name][2][id] = child
        child.species[child.species_name][0] += 1
        child.species[child.species_name][1][child.subspecies_name][1][id] = child
        child.species[child.species_name][1][child.subspecies_name][0] += 1
        child.check_and_split()


    def die(self, decompose=None):
        #self.parent = None
        if decompose == None:
            self.location.foods["detritus"][0] += self.nutritinal_output / 10
        else:
            self.location.foods["detritus"][0] += decompose

        del self.parent_list[self.id]
        del self.location.inhabitants[self.id]

        if len(self.species[self.species_name][2]) == 1:
            del self.species[self.species_name]

        else:
            self.species[self.species_name][0] -= 1
            self.species[self.species_name][1][self.subspecies_name][0] -= 1
            del self.species[self.species_name][1][self.subspecies_name][1][self.id]
            del self.species[self.species_name][2][self.id]
            #delet list, parent list, species list, subspecies list, location inhabitant

    def try_to_move(self, row, col):
        try:
            try_map = self.location.area_map[row][col]
            del self.location.inhabitants[self.id]
            self.location = try_map
            self.location.inhabitants[self.id] = self
            if self.location.terrain == "marshes":
                self.speed = self.aquatic_speed
            elif self.location.terrain == "mountains":
                self.speed = self.mountainous_speed
            else:
                self.speed = self.regular_speed
            return True
        except IndexError:
            return False

    def random_move(self):
        while True:
            row, col = self.location.row_col
            row += get_randint_neg_one_one()
            col += get_randint_neg_one_one()
            if self.try_to_move(row, col):
                break

