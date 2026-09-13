import random
from collections import deque


def make_map_terrain(area_map):
    terrain_list = ["marshes", "plains", "forests", "mountains", "savanna", "desert"]
    terrain_values = {"marshes": 0, "plains": 1, "forests": 2, "mountains": 3, "savanna": 4, "desert": 5}

    # Set weights: higher means more likely to appear
    terrain_weights = {
        "marshes": 10,
        "plains": 20,
        "forests": 15,
        "mountains": 10,
        "savanna": 8,
        "desert": 7
    }

    rows = len(area_map)
    cols = len(area_map[0])

    assigned = [[False for _ in range(cols)] for _ in range(rows)]

    def weighted_choice(weight_dict):
        """Return a terrain based on weights"""
        total = sum(weight_dict.values())
        rand_val = random.randint(1, total)
        cumulative = 0
        for terrain, weight in weight_dict.items():
            cumulative += weight
            if rand_val <= cumulative:
                return terrain

    def grow_terrain(r, c, terrain, max_growth):
        queue = deque()
        queue.append((r, c))
        assigned[r][c] = True
        area_map[r][c].change_terrain(terrain, terrain_values[terrain])
        growth_count = 0

        while queue and growth_count < max_growth:
            cr, cc = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols and not assigned[nr][nc]:
                    if random.random() < 0.7:  # chance to expand
                        assigned[nr][nc] = True
                        area_map[nr][nc].change_terrain(terrain, terrain_values[terrain])
                        queue.append((nr, nc))
                        growth_count += 1

    # Fill map
    all_cells = [(r, c) for r in range(rows) for c in range(cols)]
    random.shuffle(all_cells)

    for r, c in all_cells:
        if not assigned[r][c]:
            terrain = weighted_choice(terrain_weights)
            max_growth = random.randint(5, 50)  # variable cluster size
            grow_terrain(r, c, terrain, max_growth)
