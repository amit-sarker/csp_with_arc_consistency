import time

from ac_1 import arc_consistency_1
from ac_2 import arc_consistency_2
from ac_3 import arc_consistency_3
from ac_4 import arc_consistency_4


def get_result(domain_ac1, domain_ac2, domain_ac3, domain_ac4, constraints, total_nodes):

    start_ac1 = time.time()
    print('\n')
    print("Before AC1   ", domain_ac1)
    is_consistent_ac1 = arc_consistency_1(domain_ac1, constraints)
    print("After AC1   ", domain_ac1)
    print("Status:   ", is_consistent_ac1)
    end_ac1 = time.time()
    elapsed_ac1 = (end_ac1 - start_ac1)
    print("Elapsed time:   ", elapsed_ac1)

    start_ac2 = time.time()
    print('\n')

    print("Before AC2   ", domain_ac2)
    is_consistent_ac2 = arc_consistency_2(domain_ac2, constraints, total_nodes)
    print("After AC2   ", domain_ac2)
    print("Status:   ", is_consistent_ac2)
    end_ac2 = time.time()
    elapsed_ac2 = (end_ac2 - start_ac2)
    print("Elapsed time:   ", elapsed_ac2)

    start_ac3 = time.time()
    print('\n')
    print("Before AC3   ", domain_ac3)
    is_consistent_ac3 = arc_consistency_3(domain_ac3, constraints)
    print("After AC3   ", domain_ac3)
    print("Status:   ", is_consistent_ac3)
    end_ac3 = time.time()
    elapsed_ac3 = (end_ac3 - start_ac3)
    print("Elapsed time:   ", elapsed_ac3)

    print('\n')
    start_ac4 = time.time()

    print("Before AC4   ", domain_ac4)
    is_consistent_ac4 = arc_consistency_4(domain_ac4, constraints)
    print("After AC4   ", domain_ac4)
    print("Status:   ", is_consistent_ac4)
    end_ac4 = time.time()
    elapsed_ac4 = (end_ac4 - start_ac4)
    print("Elapsed time:   ", elapsed_ac4)
    is_same = False

    consistent = False

    if domain_ac3 == domain_ac1 == domain_ac2 == domain_ac4:
        is_same = True
    if is_consistent_ac1 and is_consistent_ac2 and is_consistent_ac3 and is_consistent_ac4:
        consistent = True

    return elapsed_ac1, elapsed_ac2, elapsed_ac3, elapsed_ac4, is_same, consistent
