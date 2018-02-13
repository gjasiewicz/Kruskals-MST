class FindUnion:
    def __init__(self, number_of_vertices):
        """initializing so that each vertex is his own boss
        (boss[i] = i)
        Vertices are represented by indices.
        type number_of_vertices: integer
        type boss: list"""
        self.boss = range(number_of_vertices)

    def find_boss(self, v):
        """
        type v: integer
        rtype: integer
        """
        boss = self.boss
        while boss[v] != v:
            v = boss[v]
        return v

    def union_boss(self, v1, v2):
        """Updating 'boss' list.
        Setting a boss for two vertices.
        type v1, v2: integer
        """
        boss = self.boss
        find_boss = self.find_boss
        boss_v1, boss_v2 = find_boss(v1), find_boss(v2)
        super_boss = min(boss_v1, boss_v2)
        boss[boss_v1] = boss[boss_v2] = super_boss
        boss[v1] = boss[v2] = super_boss

    


