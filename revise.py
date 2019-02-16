def check_constraint(values, a_con):
    return a_con([], values)


def all_arcs_v2(constraints):
    arcs = set()
    temp = {}
    for neighbors, constraint in constraints:
        if len(neighbors) == 2:
            x, y = neighbors
            temp.update({(x, y): constraint})
            list(map(arcs.add, ((x, y), (y, x))))
    return arcs, temp


def all_arcs_ac2(constraints):
    arcs1 = []
    arcs2 = []
    for neighbors, constraint in constraints:
        if len(neighbors) == 2:
            x, y = neighbors
            if int(x) > int(y):
                arcs1.append((x, y))
            else:
                arcs2.append((x, y))
    return arcs1, arcs2


def all_arcs(constraints):
    arcs = set()
    for neighbors, constraint in constraints:
        if len(neighbors) == 2:
            x, y = neighbors
            list(map(arcs.add, ((x, y), (y, x))))
    return arcs


def revise_v2(domains, edge, constraints):
    x, y = edge
    p = []
    q = []
    for con in constraints:
        arc, a_con = con
        if edge == arc:
            break
    modified = False
    res = False
    for x_value in domains[str(x)]:
        p.append(x_value)
    for y_value in domains[str(y)]:
        q.append(y_value)
    for x_val in p:
        for y_val in q:
            res = check_constraint([x_val, y_val], a_con)
            if res:
                break
        if not res:
            domains[str(x)].remove(x_val)
            modified = True
    return modified
