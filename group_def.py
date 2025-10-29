

class Group():
    def __init__(self, creature, group=None):

        if group is None:
            self.grup_leader = True
            self.group = {creature: creature}
        else:
            self.grup_leader = False
            group[creature] = creature

        self.collective_nutritinal_need = 0
        self.collective_speed = 0