import traceback

def solve(): 
  """
  notice p(i+1) has to be a factor of pi. So p1 contains least prime factors and then p2 all the
  way up to pk. So each time we factorize N = p*N0, and the polygon we construct will be p1, p1p2,...
  p1p2...pk, notice that sum of these value is contraint less than 10**6, so k is less or equal than
  12. Checking the prime factors of N will takes O(N^(1/2)) using naive method.

  Use dynamic programming to solve this problem. dp(N) = max(1, max(1 + dp(N-k), 1+dp(k)))  for k|N
  """
  from math import sqrt
  from functools import lru_cache
  N = int(input())
  
  @lru_cache(None)
  def dp(N, start=2):
    # if N <= 1: return 
    res = 1
    # loop all divisors
    for i in range(start, int(sqrt(N)) + 1):
      if N%i == 0 and N-i > i:
        # print(i)
        res = max(res, 1+dp(N//i - 1), 1+dp(i-1))
    return res
  return dp(N, start=3)
    

if __name__ == '__main__':
  try:
    T = int(input())
    for i in range(1, T+1):
      res = solve()
      print("Case #{}: {}".format(i, res))
  except Exception as e:
    print(traceback.format_exc())
