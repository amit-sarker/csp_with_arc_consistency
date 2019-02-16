from revise import revise_v2, all_arcs


def arc_consistency_3(domains, constraints):
    arcs = list(all_arcs(constraints))
    pending_arcs = set(arcs)
    while pending_arcs:
        x, y = pending_arcs.pop()
        if revise_v2(domains, (x, y), constraints):
            if len(domains[str(x)]) == 0:
                return False
            pending_arcs = pending_arcs.union((x2, y2) for x2, y2 in arcs if y2 == x)
    return True
