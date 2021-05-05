from sys import stdout

class Solution:
  @staticmethod
  def solve():

    def inc(x):
      """increase string by 1 in value"""
      l = list(map(int, x))
      carry = 1
      for i in range(len(l)-1,-1,-1):
        l[i], carry = (l[i] + carry)%10, (l[i]+carry)//10
      s = ''.join(list(map(str, l)))
      return s

    N = int(input().strip())
    X = input().split() # we use string here

    res = 0
    for i in range(1, N):
      p_len = len(X[i-1]) # length of previous string
      c_len = len(X[i]) # length of current string
      if p_len < c_len:
        continue

      if X[i-1][:c_len] > X[i] or (X[i-1][:c_len] == X[i] and X[i-1][c_len:] == '9' * (p_len-c_len)):
        X[i] += '0' * (p_len-c_len+1)
        res += p_len-c_len+1

      elif X[i-1][:c_len] == X[i]:
        X[i] += inc(X[i-1][c_len:])
        res += p_len-c_len
        
      else:
        X[i] += '0' * (p_len-c_len)
        res += p_len-c_len

    return res


        
if __name__ == '__main__':
  T = int(input())
  for i in range(1, T+1):
    res = Solution.solve()
    print("Case #{}: {}".format(i, res))

  