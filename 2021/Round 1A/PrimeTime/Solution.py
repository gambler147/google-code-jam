class Solution:
  @staticmethod
  def solve():
    """
    We know that we have at most M = 95 distinct prime numbers in given range [2, 499], and
    notice that sum of all numbers will not exceed 499 * 10**15, which is less than 2**59.
    Therefore, we know that the second group should have no more than 59 elements and thus the sum
    of the elements in second group should be smaller or equal than 59 * 499 = 29441 and thus the 
    range of sum of first group should be between [S - 29941, S] where S is the total sum of all element.
    Then we can iterate all number between this range and factorize the number to check if given factorization
    matches the input condition, this step will take (95 + 59) operations at most. If so, we can update our result.

    Total time complexity ~ O(MAX_P*log(S) * (M + log(S))), where S is total sum of all prime numbers.
    Space complexity ~ O(M) (only need to use a counter to record all distinct prime numbers and their numbers)
    """
    from math import log2, ceil
    M = int(input().strip())  # number of distinct prime numbers
    prime_cnt = []
    S = 0 # total sum of prime numbers
    MAX_P = -1
    # read primes
    for _ in range(M):
      P, N = list(map(int, input().split()))
      prime_cnt.append([P, N])
      S += P*N
      MAX_P = max(P, MAX_P)

    # find ceil of sum of second group
    sum_ceil = MAX_P * int(ceil(log2(S)))
    
    # iterate all possible number
    for v in range(S - 1, S - sum_ceil-1, -1):
      if v <= 1:
        # second group must have an element greater or equal than 2
        continue

      # factorize v, for each prime in prime_cnt, divide v by p all the way
      sum_second = 0
      n = v
      for p, k in prime_cnt:
        if n < p:
          break
        while n%p == 0:
          # we cannot proceed because we do not have enough primes
          if k <= 0:
            break
          sum_second += p
          n //= p
          k-=1
          if n == 1:
            break
        if n%p == 0 or n == 1:
          break

      # if n == 1, we have already factorized v, so we check if it is a valid answer
      if n == 1 and S - sum_second == v:
        return v
      
    return 0
      
      
if __name__ == '__main__':
  T = int(input())
  for i in range(1, T+1):
    res = Solution.solve()
    print("Case #{}: {}".format(i, res))

  