digital = [1, 2, 3]
alpha = ['one', 'two', 'three']
upper = ['ONE', 'TWO', 'THREE']
decimal = [10, 20, 30]
animal = ['1ion', '2ebra', '3lephant']

outcome = zip(digital, alpha, upper, decimal, animal)  # zipping indexes together

outcome_set = set(outcome)  # converting to set
print(outcome_set)