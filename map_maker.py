import random

def make_map_terrain(area_map):
    scattered_map = []

    for col in area_map:
        for cell in col:
            scattered_map.append(cell)

    random.shuffle(scattered_map)

    for cell in scattered_map:
        marshes = 2
        plains = 5
        forests = 4
        mountains = 3
        savanna = 2
        desert = 2

        for count1, row in enumerate(range(cell.row_col[0] - 3, cell.row_col[0] + 4)):
            for count2, cell1 in enumerate(range(cell.row_col[1] - 3, cell.row_col[1] + 4)):
                try:
                    if area_map[row][cell1].terrain == "marshes":
                        marshes += 100 - ((count1+count2) * 10)
                    elif area_map[row][cell1].terrain == "plains":
                        plains += 100 - ((count1+count2) * 10)
                    elif area_map[row][cell1].terrain == "forests":
                        forests += 100 - ((count1+count2) * 10)
                    elif area_map[row][cell1].terrain == "mountains":
                        mountains += 100 - ((count1+count2) * 10)
                    elif area_map[row][cell1].terrain == "savanna":
                        savanna += 100 - ((count1+count2) * 10)
                    elif area_map[row][cell1].terrain == "desert":
                        desert += 100 - ((count1+count2) * 10)
                except IndexError:
                    pass



                average = (marshes + plains + forests + mountains + savanna + desert)
                ran = random.randint(0, average)
                if ran < marshes:
                    cell.change_terrain("marshes", 0)
                elif ran < plains + marshes:
                    cell.change_terrain("plains", 1)
                elif ran < forests + plains + marshes:
                    cell.change_terrain("forests", 2)
                elif ran < mountains + forests + plains + marshes:
                    cell.change_terrain("mountains", 3)
                elif ran < savanna + mountains + forests + plains + marshes:
                    cell.change_terrain("savanna", 4)
                elif ran < desert + savanna + mountains + forests + plains + marshes:
                    cell.change_terrain("desert", 5)