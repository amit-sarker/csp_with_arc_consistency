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
        vi, vj = an_arc
        arc_const = temp.get(an_arc, None)
        vi = str(vi)
        vj = str(vj)
        di = []
        dj = []
        for x_va in domains[vi]:
            di.append(x_va)
        for y_va in domains[vj]:
            dj.append(y_va)
        for ai in di:
            for aj in dj:
                if arc_const([], [ai, aj]):
                    cnt = counter.get((vi, ai, vj), None)
                    cnt += 1
                    counter.update({(vi, ai, vj): cnt})
                    support_list = support.get((vj, aj), None)
                    support_list.append((vi, ai))
                    support.update({(vj, aj): support_list})
            chk_val = counter.get((vi, ai, vj), None)
            if chk_val == 0:
                val_queue.append((vi, ai))
                remove_domain(domains, vi, ai)
                if len(domains[vi]) == 0:
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
