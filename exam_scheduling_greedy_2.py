from math import ceil
from time import process_time

#READ INPUT

def readData(filename):
    with open(filename) as f:
        content = [[int(j) for j in i.split()] for i in f.read().splitlines()]
    N, d, M, c, K = content[0][0], content[1], content[2][0], content[3], content[4][0]
    p = [[content[5 + i][0] - 1, content[5 + i][1] - 1] for i in range(K)]
    print(f'N = {N}', f'd = {d}', f'M = {M}', f'c = {c}', f'K = {K}', f'p = {p}', sep = '\n')
    print('------------------')
    return N, d, M, c, K, p
filename = 'data.txt'
N, d, M, c, K, p = readData(filename)


#GREEDY ALGORITHM
print('Greedy algorithm 1.2')

startTime = process_time()

conflicts = {} #conflicts[i] = list of exams that cannot be administered in the same period as exam i+1
for pair in p:
    conflicts.setdefault(pair[0], []).append(pair[1])
    conflicts.setdefault(pair[1], []).append(pair[0])

sortedHalls = sorted([(c[i], i) for i in range(M)]) #sort halls in ascending order of capacity
result = [[None] * M] #result[i, k] = exam administered in period i+1 and hall k+1
print('\nExam', 'Period', 'Hall', sep='\t')
for exam in range(N): #sequentially assign a period and a hall to each exam
    nextExam = False
    for period in range(len(result) + 1): #consider existing periods first
        if period == len(result):
            #if this exam cannot be held in any existing period, set up a new period
            result.append([None] * M)
        notThisPeriod = False
        if exam in conflicts:
            for otherExam in result[period]:
                if otherExam in conflicts[exam]:
                    notThisPeriod = True
                    break
            if notThisPeriod:
                continue 
        for hall in range(M): #consider smaller halls first to save bigger ones for other exams
            capacity = sortedHalls[hall][0]
            hallIndex = sortedHalls[hall][1]
            if result[period][hallIndex] == None and capacity >= d[exam]:
                result[period][hallIndex] = exam
                print(exam + 1, period + 1, hall + 1, sep='\t') #print schedule by exam
                nextExam = True
                break
        if nextExam:
            break


#PRINT RESULT

print(f'\nSolution found in {(process_time() - startTime) * 1000} milliseconds')

numberOfDays = ceil(len(result) / 4)
print(f'\nThe number of days to administer all exams is {numberOfDays}.')

if input('\nWould you like to see the exam schedule sorted by day with additional details? Enter "y" or "n". ').lower() in ("y", "yes"):
    for period in range(len(result)): #print schedule by period
        if period % 4 == 0:
            print(f'Day {period // 4 + 1}:')
        print(f'\tPeriod {period + 1}:')
        for hall in range(M):
            exam = result[period][hall]
            conflictsOfThisExam = [e + 1 for e in conflicts.get(exam, [])]
            if exam != None:
                print(f'\t\tHall {hall + 1} (capacity = {c[hall]}): Exam {exam + 1} (expected turnout = {d[exam]}, exams with common candidates = {conflictsOfThisExam})')