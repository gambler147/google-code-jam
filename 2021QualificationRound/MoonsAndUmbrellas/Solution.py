class Solution:
  @staticmethod
  def solve(X,Y,S):
    """
    return minimum cost of Cody-Jamal's copyrights payment
    
    count number of '?'s for each group, for X > 0 and Y > 0 cases, it's trivial:
    we only need to count number of changes from S to J and J to S

    if X + Y < 0, its always optimal to alternate S and J
    """
    n = len(S)
    prev = None
    cost = [X, Y] # cost of transitioning from C to J and J to C respectively
    res = 0
    z = 0 # counter for '?'s
    for i in range(n):
      if S[i] in ['C', 'J']:
        cur = 0 if S[i] == 'C' else 1
        # switch cases
        if X + Y >= 0:
          # not optimal to alternate, keep all ?s same in the group
          # but if prev is None and cost[1-cur] < 0, we can make profit in prefix
          if prev is None and cost[1-cur] < 0 and z > 0:
            res += cost[1-cur]
          elif prev is not None and prev != cur:
            res += cost[prev]
        else: 
          # X + Y < 0:
          # it is always optimal to alternate
          # but be careful when ? exisits in prefix
          if prev is not None:
            res += cost[prev] * ((z+(prev!=cur)+1)//2) + cost[1-prev] * ((z+(prev==cur))//2)
          else:
            res += cost[cur] * (z//2) + cost[1-cur] * ((1+z)//2)
            if cost[cur] > 0 and z > 0 and z%2 == 0:
              # if prev is none and cost[cur] > 0 and we have even number of ?s
              # we subtract one cost[cur]
              res -= cost[cur]
            elif cost[1-cur] > 0 and z%2 == 1:
              res -= cost[1-cur] 
        z = 0
        prev = cur
      else:
        z += 1

    # handle suffix ? case
    if z > 0:
      if prev is None:
        # the whole string consists of ?
        if X + Y >= 0:
          if X < 0 and z > 1:
            res = X
          elif Y < 0 and z > 1:
            res = Y
          else:
            res = 0
        else:
          # X + Y < 0
          X, Y = min(X,Y), max(X,Y)
          res = X * (z//2) + Y * ((z-1)//2)
          if Y > 0 and z%2 == 0:
            res -= Y
      else:
        # prev is not None
        if X+Y >= 0:
          # check if cost[prev] < 0
          if cost[prev] < 0:
            res += cost[prev]
        else:
          # X+Y < 0
          res += cost[prev] * ((z+1)//2) + cost[1-prev] * (z//2)
          if cost[prev] > 0:
            res -= cost[prev]
          elif cost[1-prev] > 0 and z%2 == 0:
            res -= cost[1-prev]
    
    return res

if __name__ == '__main__':
  t = int(input())
  for i in range(1, t+1):
    X,Y,S = input().split()
    X, Y = int(X), int(Y)
    res = Solution.solve(X,Y,S)
    print("Case #{}: {}".format(i, res))

  