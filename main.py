
import random
from location_tiles import Location
from creature_def import Creature
from name_gen import name_make
from id_getter import gen_id
from time import sleep as s
import numpy as np
import matplotlib.pyplot as plt
from plottin import plot_data
from map_maker import make_map_terrain
import tracemalloc
import psutil
import os






#control panel

map_width = 30
map_height = 30
initial_pop = 10
run_time = 100001
display_per_year = 100

area_map = []

for i in range(0,map_width):
	area_map.append([])
	for i2 in range(0,map_height):
		area_map[i].append(Location(area_map, [i,i2]))

map = area_map[random.randint(0,map_width-1)][random.randint(0,map_height-1)]
#map = area_map[5][5]

scattered_map = []

#TODO
make_map_terrain(area_map)


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



for i in range(0,initial_pop):
    id = gen_id()
    map = area_map[random.randint(0, map_width - 1)][random.randint(0, map_height - 1)]
    creature = Creature(id, life, first_species_name, species, map, "base_strain", None, False)
    #def __init__(self, id, parent_list, species_name, species, location, subspecies_name, parent=None, speciate=True):
    life[id] = creature
    creature.id_for_subspecies = len(species[first_species_name][1]["base_strain"][1])
    species[first_species_name][2][id] = creature
    species[first_species_name][1]["base_strain"][1][id] = creature
    species[first_species_name][1]["base_strain"][0] += 1
#life = {joe_suaruas: [overall_pop_val=int, subspecies={joe_suaruas_with_horns: [over_all_pop=int, members=[guy2]]}, members=[guy1,guy2,guy3]]}



while life != {}:
    try:
        for i in range(0,run_time):
            tracemalloc.start()
            range = len(life)
            keys = list(life.keys())
            keys.sort(key=lambda c: life[c].list_priority+random.randint(-2,2), reverse=True)
            do_big_break = False
            for id in keys:
                try:
                    life[id].cycle()
                except KeyError:
                    pass
            for col in area_map:
                for cell in col:
                    cell.grow()

            print(f"\n{i}\namount of pop {len(life)}\n",end ='')

            current, peak = tracemalloc.get_traced_memory()
            print(f"Current memory usage: {current / 1e6:.2f} MB; Peak: {peak / 1e6:.2f} MB")

            process = psutil.Process(os.getpid())
            # inside your loop
            print(f"Memory used: {process.memory_info().rss / 1e6:.2f} MB")

            if i  % display_per_year == 0:
                s(sleep)
                #data = np.array([[cell.plants for cell in row] for row in area_map])
                #plot_data(data, "amount of plants")
                data1 = np.array([[cell.terrain_value for cell in row] for row in area_map])
                data2 = np.array([[len(cell.inhabitants) for cell in row] for row in area_map])

                time.append(i)
                for i2 in species.keys():
                    if i2 in plots:
                        if species[i2][0] <= max_value_y:
                            plots[i2].append(species[i2][0])
                        else:
                            plots[i2].append(max_value_y)
                    else:
                        plots[i2] = []
                        zeros = [0] * (len(time)-1)
                        plots[i2].extend(zeros)
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

            tracemalloc.stop()

        break
    except KeyboardInterrupt:
        break


print(f"\nbroke\n")


for i in species.keys():
    print(i, end = " ")
    print(species[i][0])
    print(f"id: {species[i][2][list(species[i][2])[0]].id}")
    print(f"diet: {species[i][2][list(species[i][2])[0]].traits.diet}")
    print(f"diet scale: {species[i][2][list(species[i][2])[0]].traits.diet_scale}")
    print(f"diet range: {species[i][2][list(species[i][2])[0]].traits.diet_range}")
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

process = psutil.Process(os.getpid())
# inside your loop
print(f"Memory used: {process.memory_info().rss / 1e6:.2f} MB")
