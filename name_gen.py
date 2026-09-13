

increment = 1
def name_make():
    global increment
    return_val=("Creature"+str(increment))
    increment += 1
    return return_val
