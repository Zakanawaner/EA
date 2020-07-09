# Finding the maximum of the function
# y = -x * (x-2) * (x-5)
# between 0 and 5 using evolutionary algorithms

import random

GENERATIONS = 1000
INDIVIDUALS = 8
BEST_SELECTION = INDIVIDUALS // 2
MUTATION = INDIVIDUALS - BEST_SELECTION


def equation(x):
    return -x * (x - 5) * (x - 1)


def reproduction(x1, x2):
    return (x1 + x2) / 2


values = [random.random() * (INDIVIDUALS - 1) for i in range(INDIVIDUALS)]
results = [equation(value) for value in values]
for g in range(GENERATIONS):

    zipped_lists = zip(results, values)
    sorted_pairs = sorted(zipped_lists, reverse=True)
    tuples = zip(*sorted_pairs)
    _, values = [list(tup) for tup in tuples]
    best = values[:BEST_SELECTION]
    offspring = [reproduction(best[i], best[i+1]) for i in range(0, BEST_SELECTION - 1, 2)]
    offspring_2 = [reproduction(best[i], best[i+2]) for i in range(0, BEST_SELECTION - 2)]
    [offspring.append(son) for son in offspring_2]
    [offspring.append(random.random() * (INDIVIDUALS - 1)) for i in range(MUTATION)]
    values = offspring
    results = [equation(value) for value in values]

zipped_lists = zip(results, values)
sorted_pairs = sorted(zipped_lists, reverse=True)
tuples = zip(*sorted_pairs)
results, values = [list(tup) for tup in tuples]
print('Best result: {} with value {}'.format(values[0], equation(values[0])))



