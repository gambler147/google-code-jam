from sys import stdout

class Solution:
  @staticmethod
  def solve(N, Q):
    """
    ask at most Q questions and finally print the array.

    N is the number of elements in the array. Q is the limit number of queries.

    We can use binary search to determine the position of each new element. Total
    time complexity is O(NlogN).

    At step i,
    let l,r = 1, i-1 and ask l, r, i to get the median of these 3, 
      1. if i is the median then we let m = (l+r) >> 1 and continue ask l, m, i and m, r, i
        to determine the interval the array lies in
      2. if l is the median, we put i at the beginning of the current list

    Total time complexity is O(N**2) (list insertion in each loop)
    """
    def query(i,j,k):
      print(i, j, k)
      stdout.flush()
      return input()

    # initialization
    arr = [1,2]
    # loop through 3 to N
    for v in range(3, N+1):
      # determine position for v
      n = len(arr)
      l, r = 0, n-1
      while l + 1 <= r:
        m = (l+r+1)//2
        ans = int(query(arr[l], arr[m], v))
        # 3 cases
        if ans == arr[l]:
          r = l-1
        elif ans == arr[m]:
          l = m
        else:
          r = m-1
      # insert
      arr.insert(r+1, v)
    
    # print result
    print(' '.join(map(str, arr)))
    stdout.flush()
    ans = input().strip()
    if ans != "1":
      exit()
        
if __name__ == '__main__':
  T, N, Q = input().split()
  T, N, Q = int(T), int(N), int(Q)
  for i in range(1, T+1):
    Solution.solve(N, Q)

  