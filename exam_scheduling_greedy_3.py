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

print('Greedy algorithm 2')
startTime = process_time()

conflicts = {} #conflicts[i] = list of exams that cannot be administered in the same period as exam i+1
for pair in p:
    conflicts.setdefault(pair[0], []).append(pair[1])
    conflicts.setdefault(pair[1], []).append(pair[0])

print('\nExam schedule sorted by period')

sortedExams = sorted([(d[i], i) for i in range(N)], reverse=True) #sort exams in ascending order of expected turnout

scheduleByPeriod = [] #scheduleByPeriod[i, k] + 1 = exam administered in period i + 1 and hall k + 1
scheduleByExam = {} #scheduleByExam[i] = (period - 1, hall - 1) allocated for exam i + 1
period = 0

while sortedExams: #sequentially fill each period with as many exams as possible until all exams have been scheduled
    if period % 4 == 0:
        print(f'Day {period // 4 + 1}:')
    print(f'\tPeriod {period + 1}:')
    scheduleByPeriod.append([None] * M)
    for hall in range(M):
        for exam in sortedExams: #consider more popular exams first
            if exam[0] <= c[hall]: #if expected turnout of this exam <= capacity of this hall
                #check if any exam already scheduled in this period has common candidates with this one
                noConflict = True
                if exam[1] in conflicts:
                    for scheduledExam in scheduleByPeriod[period]:
                        if scheduledExam in conflicts[exam[1]]:
                            noConflict = False
                            break
                if noConflict: #schedule exam in period and hall, then remove from list of exams to schedule
                    scheduleByPeriod[period][hall] = exam[1]
                    scheduleByExam[exam[1]] = (period, hall)
                    print(f'\t\tHall {hall + 1} (capacity = {c[hall]}): ', end='')
                    print(f'Exam {exam[1] + 1} (turnout = {exam[0]}, exams with common candidates = {[e + 1 for e in conflicts.get(exam[1], [])]}')
                    sortedExams.remove(exam)
                    break
    period += 1


#PRINT RESULT

print(f'\nSolution found in {(process_time() - startTime) * 1000} milliseconds')
numberOfDays = ceil(period / 4)
print(f'The number of days to administer all exams is {numberOfDays}.')

if input('\nWould you like to see the exam schedule sorted by exam? Enter "y" or "n". ').lower() in ('y', 'yes'):
    print('Exam', 'Period', 'Hall', sep='\t')
    for exam in sorted(scheduleByExam.items()):
        print(exam[0] + 1, exam[1][0] + 1, exam[1][1] + 1, sep='\t')