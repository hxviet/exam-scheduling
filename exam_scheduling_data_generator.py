import random as rd
from itertools import combinations
from math import comb

def genData(N, M, turnoutRange, capacityRange, K):
    ''' Assume N, M, *turnoutRange, and *capacityRange are positive integers.
    Assume turnoutRange and capacityRange are 2-element lists or tuples.
    Assume turnoutRange[0] <= turnoutRange[1] <= capacityRange[1] and capacityRange[0] <= capacityRange[1].
    Assume K is a natural number at most N choose 2.
    
    Randomly generate N courses, M exam halls, and K conflicts for exam scheduling algorithms 
    such that the number of candidates attending any exam is between turnoutRange[0] and turnoutRange[1]
    while the capacity of any exam hall is between capacityRange[0] and capacityRange[1].
    
    Write data into a text file.'''
    
    assert False not in [arg > 0 for arg in (N, M, *turnoutRange, *capacityRange)], 'N, M, *turnoutRange, and *capacityRange should be positive integers.'
    assert K >= 0 and K <= comb(N, 2), 'K should be a natural number at most N choose 2.'

    turnouts = [str(rd.randint(turnoutRange[0], turnoutRange[1])) for i in range(N)]
    #generate a number of large halls which can occupy all candidates of any exam and a number of smaller halls which cannot
    numLargeHalls = rd.randint(1, M)
    smallHalls = [str(rd.randint(capacityRange[0], max(turnoutRange[1], capacityRange[0]))) for i in range(M - numLargeHalls)]
    largeHalls = [str(rd.randint(turnoutRange[1], capacityRange[1])) for i in range(numLargeHalls)]
    capacities = smallHalls + largeHalls
    rd.shuffle(capacities)
    #generate all possible pairs of exams with common candidates and pick K random pairs
    conflicts = rd.sample(tuple(combinations(range(1, N + 1), 2)), K)
    rd.shuffle(conflicts)
    conflicts = [[str(i), str(j)] for i, j in conflicts]
    for pair in conflicts:
        rd.shuffle(pair)
    
    filename = f'data-N{N}-M{M}-d{turnoutRange[0]},{turnoutRange[1]}-c{capacityRange[0]},{capacityRange[1]}-K{K}.txt'
    with open(filename, 'w') as file:
        #line 1: N 
        file.write(str(N))
        #line 2: d1, d2, ..., dN
        file.write('\n' + ' '.join(turnouts))
        #line 3: M
        file.write('\n' + str(M))
        #line 4: c1, c2, ..., cM'''
        file.write('\n' + ' '.join(capacities))
        #line 5: K
        file.write('\n' + str(K))
        #lines from 6 to 5 + K: pairs of exams with common candidates
        for pair in conflicts:
            file.write('\n' + ' '.join(pair))
    return filename

if __name__ == '__main__':
    n = int(input('Enter number of exams: N = '))
    m = int(input('Enter number of examination halls: M = '))
    d = [int(i) for i in input('Enter min and max number of candidates for any exam, seperated by whitespace: ').split()]
    c = [int(i) for i in input('Enter min and max capacity of any exam hall, seperated by whitespace: ').split()]
    k = int(input('Enter number of pairs of exams with common candidates: K = '))
    print('Check out ' + genData(n, m, d, c, k) + '.')