import traceback
from scipy.optimize import linear_sum_assignment

def solve(): 
  """
  This can be solved using perfect matching algorithm, Hungarian Algorithm.
  The goal is to convert all Ms from the source grid to positions in the target
  grid. 
  There are two options for converting M in the source:
    1. swap to some target position
    2. flip to G
  There are also two options for getting each M in the target:
    1. swap from some source position
    2. flip from G
  We can construct a cost matrix with size (n1 + n2) * (n1 + n2). The row representing
  the source node and column representing a target node. The first n1 rows represents
  locations of M in the source, the first n2 cols represents locations of M in the target.
  for i < n1 while j >= n2, representing turning M to G, and i >= n1 while j < n2, representing
  converting G to M in target grid. So each pair of i,j represents an assignment for Ms from
  the source to target. Each M in both source and target can be matched with exactly one
  from the other group. Then the problem becomes a perfect matching algorithm.
  """
  R,C,F,S = list(map(int, input().split()))
  # read src and target
  src = [input() for _ in range(R)]
  tgt = [input() for _ in range(R)]
  # find locations where src or tgt is 'M'
  sloc = [(i,j) for i in range(R) for j in range(C) if src[i][j] == 'M']
  tloc = [(i,j) for i in range(R) for j in range(C) if tgt[i][j] == 'M']
  ns = len(sloc)
  nt = len(tloc)
  if ns == 0 and nt == 0:
    return 0
  # construct adjacency cost matrix
  cost = [[0 for _ in range(ns+nt)] for _ in range(ns+nt)]
  # for i < ns and j < nt, cost[i][j] means transferring M from sloc[i] to tloc[j]
  # for i < ns or j < nt, we can do a flip
  for i in range(ns+nt):
    for j in range(ns+nt):
      if i < ns and j < nt:
        cost[i][j] = S * (abs(sloc[i][0] - tloc[j][0]) + abs(sloc[i][1] - tloc[j][1]))
      elif i < ns or j < nt:
        cost[i][j] = F
  # print(cost)
  row_ind, col_ind = linear_sum_assignment(cost) # TODO: implementation of this algo
  res = 0
  for r, c in zip(row_ind, col_ind):
    res += cost[r][c]
  return res


if __name__ == '__main__':
  try:
    T = int(input())
    for i in range(1, T+1):
      res = solve()
      print("Case #{}: {}".format(i, res))
  except Exception as e:
    print(traceback.format_exc())
