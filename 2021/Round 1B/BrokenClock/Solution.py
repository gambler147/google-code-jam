class Solution:
  @staticmethod
  def solve():
    """
    the consistent value in the problem is total time of three hands.
    Define 
      TICKS_PER_SECOND = 10**9
      TOTAL_TICKS = TICKER_PER_SECOND * 12 * 60 * 60
    Lets assume h, m, s are tick values from 12 o'clock. Then we know that
    Let t be total ticks of the hour hand and clearly 0 <= t < TOTAL_TICKS, 
    then we have the following modulo equations
      t%TOTAL_TICKS = (h + K)%TOTAL_TICKS
      12*t%TOTAL_TICKS = (m + K)%TOTAL_TICKS
      720*t%TOTAL_TICKS = (s + K)%TOTAL_TICKS
    where K is some integer ticks.
    The following equations are equal to above
      11*t%TOTAL_TICKS = (m-h)%TOTAL_TICKS
      708*t%TOTAL_TICKS = (s-m)%TOTAL_TICKS

    so solve for t. Finally, to transform the ticks to hour, minute, second and nanosecond,

    """
    from itertools import permutations
    TICKS_PER_SECOND = 10**9 # this is in terms of hour hand
    TOTAL_TICKS = TICKS_PER_SECOND * 60 * 60 * 12 # 12 hours
    INV_11 = linear_congruence(11, 1, TOTAL_TICKS)
    
    def format_ticks(t):
      s, n = divmod(t, TICKS_PER_SECOND)
      m, s = divmod(s, 60)
      h, m = divmod(m, 60)
      return "%s %s %s %s" % (h, m, s, n)

    A,B,C = list(map(int, input().split()))

    for (h,m,s) in permutations([A,B,C]):
        t = INV_11*(m-h)%TOTAL_TICKS
        if 708*t%TOTAL_TICKS == (s-m)%TOTAL_TICKS:
          break
    return format_ticks(t)


    
def linear_congruence(a, b, m):
  """
  this function solves ax = b (mod m). The solution exists if and only if 
  (a,m) | b

  Using Euler's algorithm
  """
  if b == 0:
    return 0
  b %= m
  a %= m
  return (m * linear_congruence(m, -b, a) + b) // a
  
    
if __name__ == '__main__':
  T = int(input())
  for i in range(1, T+1):
    res = Solution.solve()
    print("Case #{}: {}".format(i, res))

  