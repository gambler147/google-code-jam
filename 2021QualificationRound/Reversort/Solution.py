class Solution:
  @staticmethod
  def solve(nums, n):
    """return total cost for reversort"""
    res = 0
    for i in range(n-1):
      min_j = nums.index(min(nums[i:])) + 1
      nums[i:min_j] = nums[i:min_j][::-1]
      res += min_j - i
    return res

if __name__ == '__main__':
  t = int(input())
  for i in range(1, t+1):
    n = int(input())
    L = list(map(int, input().split()))
    res = Solution.solve(L, n)
    print("Case #{}: {}".format(i, res))

  