
import random
from random_store import get_randint_neg_ten_ten
from location_tiles import Location
from creature_def import Creature
from name_gen import name_make
from id_getter import gen_id
import numpy as np
from plottin import plot_data
from map_maker import make_map_terrain


memory_collection = True
time_tracking = True

if time_tracking:
    import cProfile, pstats
    import io

    pr = cProfile.Profile()
    pr.enable()

if memory_collection == True:
    import tracemalloc
    import psutil
    import os
    map_memory = 0
    creature_memory = 0
    plot_memory = 0
    process = psutil.Process(os.getpid())
    initial_memory = int(process.memory_info().rss / 1e6)
    print(f"Memory used: {process.memory_info().rss / 1e6:.2f} MB")
    #control panel
    temp_memory = int(process.memory_info().rss / 1e6)

map_width = 30
map_height = 30
initial_pop = 100
run_time = 100001 #100001
display_per_year = 100
plant_intro = 0
creature_intro = 0
meat_eater_intro = 500


area_map = []

for i in range(0,map_width):
	area_map.append([])
	for i2 in range(0,map_height):
		area_map[i].append(Location(area_map, [i,i2]))

map = area_map[random.randint(0,map_width-1)][random.randint(0,map_height-1)]
#map = area_map[5][5]

scattered_map = []

make_map_terrain(area_map)

if memory_collection == True:
    process = psutil.Process(os.getpid())
    map_memory = int(process.memory_info().rss / 1e6) - temp_memory
    temp_memory = int(process.memory_info().rss / 1e6)

first_species_name = name_make()

time = []
plots = {}
names = []
max_value_y = 10000
max_value_x = 10

sleep = 1

#more complicated list of species
species = {first_species_name: [initial_pop, {"base_strain": [initial_pop, {}]}, {}]}
#simple list full list of people use for easy iteration
life = {}


#start of real code


if memory_collection == True:
    process = psutil.Process(os.getpid())
    creature_memory = int(process.memory_info().rss / 1e6) - temp_memory

while True:
    try:

        for i in range(0,run_time):

            keys = list(life.keys())
            keys.sort(key=lambda c: life[c].list_priority+get_randint_neg_ten_ten(), reverse=True)


            if memory_collection == True:
                process = psutil.Process(os.getpid())
                temp_memory = int(process.memory_info().rss / 1e6)

            cycle = Creature.cycle
            for id in keys:
                try:
                    cycle(life[id])
                except KeyError:
                    pass

            if memory_collection == True:
                process = psutil.Process(os.getpid())
                creature_memory += int(process.memory_info().rss / 1e6) - temp_memory
                temp_memory = int(process.memory_info().rss / 1e6)

            grow = Location.grow
            for col in area_map:
                for cell in col:
                    grow(cell)

            if memory_collection == True:
                process = psutil.Process(os.getpid())
                map_memory = int(process.memory_info().rss / 1e6) - temp_memory
                print(f"Memory used: {process.memory_info().rss / 1e6:.2f} MB")

            #add creatures at year creature_intro
            if i == creature_intro:
                for i in range(0, initial_pop):
                    id = gen_id()
                    map = area_map[random.randint(0, map_width - 1)][random.randint(0, map_height - 1)]
                    creature = Creature(id, life, first_species_name, species, map, "base_strain", None, False)
                    # def __init__(self, id, parent_list, species_name, species, location, subspecies_name, parent=None, speciate=True):
                    life[id] = creature
                    species[first_species_name][2][id] = creature
                    species[first_species_name][1]["base_strain"][1][id] = creature
                    species[first_species_name][1]["base_strain"][0] += 1
                    # life = {joe_suaruas: [overall_pop_val=int, subspecies={joe_suaruas_with_horns: [over_all_pop=int, members=[guy2]]}, members=[guy1,guy2,guy3]]}

            #add carnisuars at year meat_eater_intro
            if i == meat_eater_intro:
                add_pop = 100
                species_name = "meaty_ryans"
                species["meaty_ryans"] = [add_pop, {"base_strain": [add_pop, {}]}, {}]
                for i2 in range(1,add_pop):
                    id = gen_id()
                    map = area_map[random.randint(0, map_width - 1)][random.randint(0, map_height - 1)]
                    creature = Creature(id, life, species_name, species, map, "base_strain", None, False)
                    # def __init__(self, id, parent_list, species_name, species, location, subspecies_name, parent=None, speciate=True):
                    life[id] = creature
                    species[species_name][2][id] = creature
                    species[species_name][1]["base_strain"][1][id] = creature
                    species[species_name][1]["base_strain"][0] += 1
                    life[id].traits.diet_scale = 100


            print(f"\n{i}\namount of pop {len(life)}\n", end='')


            if i  % display_per_year == 0:

                if memory_collection == True:
                    process = psutil.Process(os.getpid())
                    temp_memory = int(process.memory_info().rss / 1e6)
                #data = np.array([[cell.plants for cell in row] for row in area_map])
                #plot_data(data, "amount of plants")
                data1 = np.array([[cell.terrain_value for cell in row] for row in area_map])
                data2 = np.array([[len(cell.inhabitants) for cell in row] for row in area_map])

                time.append(i)
                for i2 in species.keys():
                    if i2 in plots:
                        if species[i2][0] <= max_value_y:
                            plots[i2].append(species[i2][0])
                        elif species[i2][0] <= 0:
                            del plots[i2]
                        else:
                            plots[i2].append(max_value_y)
                    else:
                        plots[i2] = [0] * (len(time)-1)
                        if species[i2][0] <= max_value_y:
                            plots[i2].append(species[i2][0])
                        else:
                            plots[i2].append(max_value_y)

                temp_plots = list(plots.keys())
                for i2 in temp_plots:
                    if len(plots[i2]) != len(time):
                        del plots[i2]

                if len(time) > max_value_x:
                    count = 0
                    time.pop(0)
                    for data in plots.values():
                        data.pop(0)

                plots_for_bar={}
                for i2 in species.keys():
                    plots_for_bar[i2] = species[i2][0]



                plot_data(data1, "Terrain Map", data2, "Number of Inhabitants", plots, time, topn_dict=plots_for_bar, species=species)

                if memory_collection == True:
                    process = psutil.Process(os.getpid())
                    plot_memory += int(process.memory_info().rss / 1e6) - temp_memory

        break
    except KeyboardInterrupt:
        break


print(f"\nbroke\n")


for i in species.keys():
    print(i, end = " ")
    print(species[i][0])
    if species[i][0] != len(species[i][2]):
        print(f"INACCURACY ERROR BY: {len(species[i][2])-species[i][0]}")
    print(f"id: {species[i][2][list(species[i][2])[0]].id}")
    for trait in species[i][2][list(species[i][2])[0]].traits.traits:
        print(trait)
    print(f"diet: {species[i][2][list(species[i][2])[0]].traits.diet}")
    print()



print()
print()

av = 0
oldest = 0

for i in life.keys():
    av += life[i].age
    if life[i].age > oldest:
        oldest = life[i].age
print(f"average age all species: {av / len(life)}")
print(f"oldest creature alive: {oldest}")
print(f"ending pop: {len(life)}")

if memory_collection == True:
    process = psutil.Process(os.getpid())
    print(f"Memory used: {process.memory_info().rss / 1e6:.2f} MB")

    other_memory = int(process.memory_info().rss / 1e6) - (map_memory + creature_memory + plot_memory + initial_memory)

    print(f"INITIAL MEMORY USAGE: {initial_memory:.2f} MB")
    print(f"MAP MEMORY USAGE: {map_memory:.2f} MB")
    print(f"CREATURE MEMORY USAGE: {creature_memory:.2f} MB")
    print(f"PLOT MEMORY USAGE: {plot_memory:.2f} MB")
    print(f"RANDOM MEMORY USAGE: {other_memory:.2f} MB")

if time_tracking:

    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats("cumtime")
    ps.print_stats(15)  # top 15 slowest functions
    print(s.getvalue())

