def _call_constraint(assignment, neighbors, constraint):
    variables, values = zip(*[(n, assignment[n])
                              for n in neighbors])
    return constraint(variables, values)


def revise(domains, arc, constraints):
    x, y = arc
    related_constraints = [(neighbors, constraint)
                           for neighbors, constraint in constraints
                           if set(arc) == set(neighbors)]
    modified = False

    for neighbors, constraint in related_constraints:
        for x_value in domains[str(x)]:
            constraint_results = (_call_constraint({x: x_value, y: y_value},
                                                   neighbors, constraint)
                                  for y_value in domains[str(y)])

            if not any(constraint_results):
                domains[str(x)].remove(x_value)
                modified = True
    return modified


def all_arcs(constraints):
    arcs = set()

    for neighbors, constraint in constraints:
        if len(neighbors) == 2:
            x, y = neighbors
            list(map(arcs.add, ((x, y), (y, x))))

    return arcs


def arc_consistency_3(domains, constraints):
    arcs = list(all_arcs(constraints))
    x = arcs[2][0]
    #print("pp   ", x)
    #print("qq   ", arcs[2][1])
    print(arcs)
    pending_arcs = set(arcs)
    #print(pending_arcs)

    while pending_arcs:
        x, y = pending_arcs.pop()
        if revise(domains, (x, y), constraints):
            if len(domains[str(x)]) == 0:
                return False
            pending_arcs = pending_arcs.union((x2, y2) for x2, y2 in arcs if y2 == x)
    return True


def arc_consistency_1(domains, constraints):
    arcs = list(all_arcs(constraints))
    print(arcs)
    isChanged = False
    while True:
        for arc in arcs:
            x = arc[0]
            y = arc[1]
            #print("x  ", x, "  y  ", y)
            isChanged = revise(domains, (x, y), constraints)
            if len(domains[str(x)]) == 0:
                return False
        if not isChanged:
            break
    return True


