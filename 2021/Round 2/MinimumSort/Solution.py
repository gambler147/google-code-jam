import traceback

def solve(N): 
  # do N-1 swaps
  for i in range(1, N):
    # ask for min from i to N
    print("M {} {}".format(i, N))
    idx = int(input())
    # swap index for idx and i if idx != i
    if idx != i:
      print("S {} {}".format(i, idx))
      respond = int(input())
  # done with the sorting
  print("D") 
  respond = int(input())
  return 


if __name__ == '__main__':
  try:
    T, N = list(map(int, input().split()))
    for i in range(1, T+1):
      res = solve(N)
      # print("Case #{}: {}".format(i, res))
  except Exception as e:
    print(traceback.format_exc())
