# Integer Linear Programming
from ortools.linear_solver import pywraplp
# Timer
import time

# Data Reader Implementation
filename = 'data.txt'
def readData(filename):
  with open(filename) as f:
    content = [[int(j) for j in i.split()] for i in f.read().splitlines()]
  N, d, M, c, K = content[0][0], content[1], content[2][0], content[3], content[4][0]
  p = [[content[5 + i][0] - 1, content[5 + i][1] - 1] for i in range(K)]
  print(f'N = {N}', f'd = {d}', f'M = {M}', f'c = {c}', f'K = {K}', f'p = {p}', sep = '\n')
  print('------------------')
  return N, d, M, c, K, p
N, d, M, c, K, p = readData(filename)

# Integer Linear Programming
print('Integer Linear Programming')
print('------------------')

#start timing
start_time = time.process_time()
# Instantiate a SCIP solver
solver = pywraplp.Solver.CreateSolver('SCIP')
INF = solver.infinity()

# Define variables

# Variable x[i][j][k]
x = [[[solver.IntVar(0, 1, f'x[{i}][{j}][{k}]') for i in range(N)] for j in range(M)] for k in range(N)]

# Variable y
y = solver.IntVar(0, N - 1, 'y')

# Define constraints

# Constraint 1: Pairs of conflicting courses may not be put in the same time slot
for i in range(K):
  u, v = p[i][0], p[i][1]
  for k in range(N):
    constraint = solver.Constraint(0, 1)
    for j1 in range(M):
      for j2 in range(M):
        if j1 != j2:
          constraint.SetCoefficient(x[u][j1][k], 1)
          constraint.SetCoefficient(x[v][j2][k], 1)

# Constraint 2: A course may be conducted at most one time in an exam hall
for i in range(N):
  constraint = solver.Constraint(1, 1)
  for j in range(M):
    for k in range(N):
      constraint.SetCoefficient(x[i][j][k], 1)

# Constraint 3: An exam hall may be assigned at most one course in a time slot
for j in range(M):
  for k in range(N):
    constraint = solver.Constraint(0, 1)
    for i in range(N):
      constraint.SetCoefficient(x[i][j][k], 1)

# Constraint 4: A course n_i must be put into a hall m_j with capacity c(j)
for i in range(N):
  for j in range(M):
    constraint = solver.Constraint(0, c[j])
    for k in range(N):
      constraint.SetCoefficient(x[i][j][k], d[i])

# Constraint 5: The number of time slots (x[i,j,k] - y <= 0)
for i in range(N):
  for j in range(M):
    for k in range(N):
      constraint = solver.Constraint(-INF, 0)
      constraint.SetCoefficient(y, -1)
      constraint.SetCoefficient(x[i][j][k], k)

# Define objective
obj = solver.Objective()
obj.SetCoefficient(y, 1)
obj.SetMinimization()

# Solve and count elapsed time
status = solver.Solve()
end_time = time.process_time()

# Check that the problem has an optimal solution.
if status == solver.OPTIMAL or status == solver.FEASIBLE:
  print(f'Optimal objective value: {obj.Value() + 1}') # Objective value
  print('------------------')
  # Allocation of examination hall and time slot
  for k in range(N):
    for j in range(M):
      for i in range(N):
        if x[i][j][k].solution_value() == 1:
          print(f'Time slot {k + 1}: Hall {j + 1}: Course {i + 1}')
          break
else:
  print('The solver could not solve the problem.')
print('------------------')

#Advanced usage
print('Advanced usage:')
print(f'Problem solved in {end_time - start_time} milliseconds')