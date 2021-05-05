class Solution:
  @staticmethod
  def solve(N, C):
    """
    return the permutation with total cost of C of integers from 1 to N if possible
    otherwise print IMPOSSIBLE.

    If N-1 <= C <= N(N+1)/2 - 1, then it is always possible.
    We iteratively get index i <= x <= N (i from 1 to N-1) and make sure 
    N-i-1 <= C:= C-x  <= (N-i)(N+1-i)/2 - 1
    """
    if C < N-1 or C > N*(N+1)/2 - 1:
      return "IMPOSSIBLE"
    
    # we now iterate and find indices of each value satisfying total cost is C
    cost = []
    for i in range(1,N):
      x = max(1, C - (N-i)*(N-i+1)//2 + 1) # cost for ith step
      cost.append(x)
      C -= x
    
    # reconstruct array
    array = [0] * (N-1) + [N]
    # start from the end of indices
    for i in range(N-2, -1, -1):
      idx = cost[i]
      # reverse array[i:i+idx]
      array[i:i+idx] = array[i:i+idx][::-1]
      array[i+idx-1] = 1+i
    
    return ' '.join(map(str,array))

   

if __name__ == '__main__':
  t = int(input())
  for i in range(1, t+1):
    N, C = input().split()
    N, C = int(N), int(C)
    res = Solution.solve(N, C)
    print("Case #{}: {}".format(i, res))

  