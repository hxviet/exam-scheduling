import time

# Data Reader
filename = 'data.txt'
def readData(filename):
  with open(filename) as f:
    content = [[int(j) for j in i.split()] for i in f.read().splitlines()]
  N, d, M, c, K = content[0][0], content[1], content[2][0], content[3], content[4][0]
  p = [[content[5 + i][0] - 1, content[5 + i][1] - 1] for i in range(K)]
  # print(f'N = {N}', f'd = {d}', f'M = {M}', f'c = {c}', f'K = {K}', f'p = {p}', sep = '\n')
  return N, d, M, c, K, p
N, d, M, c, K, p = readData(filename)

# ans
ans = 99999999

# clash
clash = [[] for _ in range(N)]
for k in p:
  u, v = k[0], k[1]
  clash[u].append(v)
  clash[v].append(u)

# assign time slot
time_slot = [-1] * N

# room
room = []
for _ in range(N):
  room.append([-1] * M)

# checker: (1) assigned a time_slot, (2) not clashing
def isPlaceable(u, slot):
  if time_slot[u] >= 0:
    return False
  for v in clash[u]:
    if time_slot[v] == slot:
      return False
  return True

def dfs(u, slot):
  global ans
  if u == N:
    ans = min(ans, slot)
    return
  if slot > ans:
    return
  for j in range(M):
    if room[slot][j] == -1:
      for i in range(N):
        if isPlaceable(i, slot) and d[i] <= c[j]:
          time_slot[i], room[slot][j] = slot, i
          dfs(u + 1, slot)
          time_slot[i], room[slot][j] = -1, -1
  dfs(u, slot + 1)
  return

# Solve
start_time = time.process_time()
dfs(0, 0)
end_time = time.process_time()

# Solution
if ans != 99999999:
  print(f'Objective value: {ans + 1}')
else:
  print('No solution.')
print('------------------')

# Advanced usage
print('Advanced usage:')
print(f'Elapsed time: {1000*(end_time - start_time)} milliseconds')