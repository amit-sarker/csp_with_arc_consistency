class CspProblem(object):
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

        # variable-based constraints dict
        self.var_contraints = dict([(v, [constraint
                                         for constraint in constraints
                                         if v in constraint[0]])
                                    for v in variables])

        # calculate degree of each variable
        self.var_degrees = dict([(v, len(self.var_contraints[v]))
                                 for v in variables])