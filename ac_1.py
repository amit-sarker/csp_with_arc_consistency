from revise import revise_v2, all_arcs


def arc_consistency_1(domains, constraints):
    arcs = list(all_arcs(constraints))
    while True:
        sec_flag = False
        for arc in arcs:
            x = arc[0]
            y = arc[1]
            is_changed = revise_v2(domains, (x, y), constraints)
            if is_changed:
                sec_flag = True
            if len(domains[str(x)]) == 0:
                return False
        if not sec_flag:
            break
    return True
