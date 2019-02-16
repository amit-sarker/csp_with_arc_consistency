from collections import deque

import copy

from revise import revise_v2, all_arcs


def arc_consistency_2(domains, constraints, number_of_nodes):
    val_queue1 = deque()
    val_queue2 = deque()
    for i in range(0, number_of_nodes):
        arcs = all_arcs(constraints)
        for j in range(0, i):
            if (i, j) in arcs:
                val_queue1.append((i, j))
                val_queue2.append((j, i))
        while not val_queue1.__len__() == 0:
            while not val_queue1.__len__() == 0:
                k, m = val_queue1.popleft()
                if revise_v2(domains, (k, m), constraints):
                    if len(domains[str(k)]) == 0:
                        return False
                    for p in range(0, i + 1):
                        if ((p, k) in arcs) and m != p:
                            val_queue2.append((p, k))
            val_queue1 = copy.deepcopy(val_queue2)
            val_queue2.clear()
    return True
