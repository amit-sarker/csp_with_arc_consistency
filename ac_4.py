from collections import deque

from revise import all_arcs, all_arcs_v2


def init_all(domains, constraints):
    s = {}
    for key, val in domains.items():
        for i in range(len(val)):
            pair = (key, val[i])
            s.update({pair: []})

    c = {}
    arcs = list(all_arcs(constraints))
    print(arcs)
    for an_arc in arcs:
        x, y = an_arc
        x = str(x)
        y = str(y)
        dom_list = domains.get(x, None)
        for value in dom_list:
            counter_pair = (x, value, y)
            c.update({counter_pair: 0})
    return s, c


def remove_domain(domains, vi, ai):
    if ai in domains[str(vi)]:
        domains[str(vi)].remove(int(ai))
    return domains


def arc_consistency_4(domains, constraints):
    val_queue = deque()
    support, counter = init_all(domains, constraints)
    arcs, temp = list(all_arcs_v2(constraints))
    for an_arc in arcs:
        x, y = an_arc
        arc_const = temp.get(an_arc, None)
        x = str(x)
        y = str(y)
        p = []
        q = []
        for x_va in domains[x]:
            p.append(x_va)
        for y_va in domains[y]:
            q.append(y_va)
        for x_value in p:
            support_list = []
            for y_value in q:
                if arc_const([], [x_value, y_value]):
                    cnt = counter.get((x, x_value, y), None)
                    cnt += 1
                    counter.update({(x, x_value, y): cnt})
                    support_list.append((y, y_value))
            support.update({(x, x_value): support_list})
            chk_val = counter.get((x, x_value, y), None)
            if chk_val == 0:
                val_queue.append((x, x_value))
                remove_domain(domains, x, x_value)
                if len(domains[x]) == 0:
                    return False

    while not val_queue.__len__() == 0:
        vj, aj = val_queue.popleft()
        sup_list = support.get((vj, aj), None)
        for val in sup_list:
            vi, ai = val
            if ai in domains[str(vi)]:
                cnt = counter.get((vi, ai, vj), None)
                cnt -= 1
                counter.update({(vi, ai, vj): cnt})
                if counter.get((vi, ai, vj), None) == 0:
                    val_queue.append((vi, ai))
                    remove_domain(domains, vi, ai)
                    if len(domains[str(vi)]) == 0:
                        return False

    return True
