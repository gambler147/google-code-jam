import traceback
f, f_inv = None, None

def solve(): 
  global f, f_inv

  N = int(input())
  V = list(map(int, input().split()))
  V.append(1)
  stack = []
  f, f_inv = get_f_and_inv(N)
  res = 1
  for i in range(N+1):
    # read Vi
    v = V[i]
    if v > len(stack)+1:
      return 0
    cnt = 0
    while len(stack) > v-1:
      res = res * f[cnt+stack[-1]-1] % MOD * f_inv[stack[-1]-1] % MOD * f_inv[cnt] % MOD
      cnt += stack.pop()
    stack.append(cnt+1)
  return res


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
