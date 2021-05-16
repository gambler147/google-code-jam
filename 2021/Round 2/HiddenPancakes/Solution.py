import traceback
f, f_inv = None, None

def solve(): 
  """
  We can form a tree based on the size of pancakes, an edge from a parent to
  a child represents the parent's size is greater than the child's size. we
  use a decreasing stack to record the size of nodes, when a new pancake i comes,
  we pop out all elements until Vi pancakes remaining. 

  After we construct the tree of N pancakes, we start from the root, and imagine there
  are k branches with each branch nk pancakes in each subtree, there are dp(i, nk) ways to
  arrange these nk pancakes, so in total there are dp(root, N) = prod(dp(i, nk) for all k) ways 
  that satisfy given visible condition. If at any step i, Vi > len(stack) or Vi == 0, 
  it is impossible.
  
  """
  from collections import defaultdict
  global f, f_inv

  N = int(input())
  V = list(map(int, input().split()))
  stack = []
  f, f_inv = get_f_and_inv(N)
  children = defaultdict(list)

  for i in range(N):
    # read Vi
    v = V[i]
    if v > len(stack)+1:
      return 0
    # otherwise pop the stack until v-1 elements remaining
    # and build tree
    cur = None
    while len(stack) > v-1:
      if stack and cur is not None:
        children[stack[-1]].append(cur)
      cur = stack.pop()
    stack.append(i)
    if cur is not None:
      children[stack[-1]].append(cur)
      
  # handle the final stack, and the last element remained is the biggest pancake in the tree
  while len(stack) > 1:
    cur = stack.pop()
    children[stack[-1]].append(cur)
  root = stack.pop()
  
  # then use dfs to get depth of each node
  child_cnts = get_child_cnt_list(N, root, children)

  # get mod combination
  res = get_mod_comb(root, children, child_cnts)

  return res


def get_child_cnt_list(N, root, children):
  """return child count list of all nodes"""
  cnts = [1] * N
  stack = [(-1, root, iter(children[root]))]
  while stack:
    p, c, it = stack[-1]
    nxt = next(it, None)
    if nxt is None:
      # this node is exhausted. Pop from stack and add its value to its parent
      stack.pop()
      if p != -1:
        cnts[p] += cnts[c]
    else:
      stack.append([c, nxt, iter(children[nxt])])
  return cnts
  

def get_mod_comb(root, children, child_cnts):
  """find total arrangements of a subtree (mod 10**9+7)"""
  N = child_cnts[root]
  comb = [f[child_cnts[i]-1] for i in range(N)] # combination value for each node
  # use a stack
  stack = [(-1, root, iter(children[root]))]
  while stack:
    p, c, it = stack[-1]
    nxt = next(it, None)
    if nxt is None:
      stack.pop()
      if p!=-1:
        y = child_cnts[c]
        comb[p] = comb[p] * f_inv[y] % MOD * comb[c] % MOD
    else:
      stack.append([c, nxt, iter(children[nxt])])
  # total comb is a multinomial distribution (n-1)! / k1!k2!...kr!, k1+k2+...+kr = n-1
  # ans = f[n-1]
  # for c in children[node]:
  #   ans = (ans * f_inv[child_cnts[c]] * get_mod_comb(c, children, child_cnts)) % MOD
  return comb[root]

def get_f_and_inv(N):
  """return list of factorial mod MOD"""
  f = [1, 1]
  f_inv = [1, 1]
  inv = [0, 1]
  for i in range(2, N+1):
    f.append(f[-1] * i % MOD)
    inv.append(MOD - (MOD//i) * inv[MOD%i] % MOD)
    f_inv.append(inv[-1] * f_inv[-1] % MOD)
  return f, f_inv

MOD = 10**9+7

if __name__ == '__main__':

  try:
    T = int(input())
    for i in range(1, T+1):
      res = solve()
      print("Case #{}: {}".format(i, res))
  except Exception as e:
    print(traceback.format_exc())
