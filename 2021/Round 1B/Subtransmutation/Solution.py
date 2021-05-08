
def solve():
  """
  1 <= N <= 20
  1 <= Ui <= 20
  
  Starting from a metal m, lets define two counters cur and target, where in a given state, cur[i]
  is the number of metal i we have and target[i] is number of metal i we need. So target starts 
  with target[i] = Ui, and if at any point target is emtpy (target[i] == 0 for all i), then 
  we can produce all required metals from starting metal m. If at any point cur is empty while 
  target is not, then we fail to produce.

  We update our counters and target in a greedy way,
    pick the largest metal j from cur, check if j is also in target, if so, let c = target[j]
    and set cur[j] = cur[j] - target[j], if cur[j] < 0, then return False

  Notice that given A, B, a metal m will turn to m-A, m-B, therefore, all subsquent metals produced
  by metal m will have the same modulo of m%(A,B). Let d = (A,B), it can be proven that if all
  required metals i that i = m (mod d), then it is always possible to produce these metals.
  The upper bound of the metal in our case will be 402
  
  Time complexity O(400*400)
  """
  N, A, B = list(map(int, input().split()))
  U = list(map(int, input().split()))
  # get gcd of A,B
  d = gcd(A, B)
  
  mod = set()
  for i, u in enumerate(U):
    if u > 0:
      mod.add((i+1)%d)
  # if not all units share the same module, return IMPOSSIBLE
  if len(mod) > 1:
    return "IMPOSSIBLE"

  mod = mod.pop()
  # iterate all possible starting metal from N to 402
  for m in range(N, 403):
    if m%d != mod:
      continue
    
    # construct cur and target
    cur = {}
    cur[m] = 1
    target = {}
    for i, u in enumerate(U):
      if u > 0:
        target[i+1] = u

    if check_status(cur, target, A, B):
      return m
  
  return "IMPOSSIBLE"

def check_status(cur, target, A, B):
  """
  inplace update of cur and target. 
  cur is a SortedDict instance. target can be a dict or a SortedDict
  return true if it is possible to make target empty
  """
  if len(target) == 0:
    return True

  if len(cur) == 0:
    return False

  # get largest element from cur 
  k = max(cur.keys())
  v = cur.pop(k)
  if k in target:
    tv = target.pop(k)
    v -= tv
    if v < 0:
      return False

  # update k and k-A, k-B
  if k - A > 0:
    cur[k-A] = cur.get(k-A, 0) + v
  if k - B > 0:
    cur[k-B] = cur.get(k-B, 0) + v
  return check_status(cur, target, A, B)
    
    
def gcd(A, B):
  if A == 0:
    return B

  if B == 0:
    return A

  A,B = max(A, B), min(A,B)
  while B > 0:
    q, r = divmod(A, B)
    A, B = B, r
  return A
    
if __name__ == '__main__':
  try:
    T = int(input())
    for i in range(1, T+1):
      res = solve()
      print("Case #{}: {}".format(i, res))
  except Exception as e:
    print(e)
  