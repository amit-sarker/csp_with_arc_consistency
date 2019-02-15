import queue

y_val = []


def _call_constraint(assignment, neighbors, constraint):
    variables, values = zip(*[(n, assignment[n])
                              for n in neighbors])
    if constraint(variables, values):
        y_val.append(values[1])
    return constraint(variables, values), y_val


def calculate_support(pair, domains, constraints):
    arc = []
    supported_list = []

    pair = list(pair)
    for const in constraints:
        x, y = const[0]
        if x == int(pair[0]) or y == int(pair[0]):
            arc.append(const[0])

    for a in arc:
        x, y = a
        related_constraints = [(neighbors, constraint)
                               for neighbors, constraint in constraints
                               if set(a) == set(neighbors)]

        for neighbors, constraint in related_constraints:
            for y_value in domains[str(y)]:
                tup = []
                val = [pair[1], y_value]
                if constraint([], val):
                    tup.append(str(y))
                    tup.append(val[1])
                    tup = tuple(tup)
                    supported_list.append(tup)
    return supported_list


def update_counter(variables, domains, counter, constraints, s):
    temp = []
    support_tuple = []
    arc = []
    cnt = 0
    for key, val in domains.items():
        for const in constraints:
            x, y = const[0]
            if x == int(key):
                arc.append(y)
            if y == int(key):
                arc.append(x)
        for i in val:
            for j in arc:
                temp.append(key)
                support_tuple.append(key)
                temp.append(i)
                support_tuple.append(i)
                temp.append(j)
                temp = tuple(temp)
                support_tuple = tuple(support_tuple)
                support_list = s.get(support_tuple, None)

                if support_list:
                    for elem in support_list:
                        x1, y1 = elem
                        if int(x1) == int(j):
                            cnt += 1
                else:
                    cnt = 0
                counter.update({temp: cnt})
                cnt = 0
                temp = []
                support_tuple = []
    return counter


def remove_domain(domains, vi, ai):
    print("llll    ", ai)
    if ai in domains[str(vi)]:
        domains[str(vi)].remove(int(ai))
        print("dddd   ", domains)
    return domains


def arc_consistency_4(variables, domains, constraints):
    q = queue.Queue(500)
    s = {}
    pair = []
    counter = {}
    M = []
    for key, val in domains.items():
        for i in range(len(val)):
            pair.append(key)
            pair.append(val[i])
            pair = tuple(pair)
            supported_list = calculate_support(pair, domains, constraints)
            s.update({pair: supported_list})
            counter = update_counter(variables, domains, counter, constraints, s)
            pair = []

        for k, v in counter.items():
            if v == 0:
                vi,ai,vj = k
                l = [vi,ai]
                l = tuple(l)
                #print(l)
                q.put(l)
                #domains = remove_domain(domains, vi, ai)


    while not q.empty():
        var = q.get()
        M.append(var)
        # for k1,v1 in s.items():

    print("Support List  ", s)
    print("Counter   ", counter)
    print("domains   ", domains)
