
def solve():
  """
  We can sort list of already purchased tickets. Then we only need to look at 
  the length of intervals of consecutive tickets, lets say d. 
  1. Then we can get maximum of d//2 tickets within this interval if we purchase one in this interval.
  2. We can get maximum of d-1 tickets if we purchase 2 tickets in same interval.
  """

  N, K = list(map(int, input().split()))

  purchased = list(map(int, input().split()))
  purchased = set(purchased)
  purchased = sorted(purchased)
  purchased = [-purchased[0]+1] + purchased + [2*K - purchased[-1]]

  # find 2 longest intervals
  gaps = [purchased[i+1] - purchased[i] for i in range(len(purchased)-1)]
  gaps = sorted(enumerate(gaps), key=lambda x: -x[1])
  # 2 options, puchase two tickets from gaps[0] if not first or last interval or purchase gaps[0] and gaps[1]
  res = gaps[0][1]//2 + gaps[1][1]//2
  if gaps[0][0] not in [0, len(gaps)-1]:
    res = max(res, gaps[0][1]-1)
  return res / K


if __name__ == '__main__':
  try:
    T = int(input())
    for i in range(1, T+1):
      res = solve()
      print("Case #{}: {}".format(i, res))
  except Exception as e:
    print(e)
