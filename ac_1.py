from revise import revise_v2, all_arcs


def arc_consistency_1(domains, constraints):
    arcs = list(all_arcs(constraints))
    pending_arcs = set(arcs)
    isChanged = False
    while True:
        for arc in pending_arcs:
            x = arc[0]
            y = arc[1]
            isChanged = revise_v2(domains, (x, y), constraints)
            if len(domains[str(x)]) == 0:
                return False
        if not isChanged:
            break
    return True
