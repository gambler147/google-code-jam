
def solve():
  """
  Greedy.

  Since the block size is B and we have N blocks.
  For each block, the value of the tower is sum(D^(i) for i in [0, B-1]).
  Notice that first B-2 digits in each block contribute very little to the total sum
  So only the B-1 and Bth digits count. For any given digit d,
  if d == 9, we place it at the highest tower (less than B),
  if d >= 7, we place it at the highest tower (less than B-1)
  if d <= 6, we place it at any random tower whose height is less than (B-2)

  Time complexity: O(N^2 * B)
  """
  heights=[0 for _ in range(N)]
  numbers = ["" for _ in range(N)]
  for _ in range(N * B):
    d = int(input())
    idx = -1
    if (d == 9):
      for i in range(N):
        if heights[i] == B-1:
          idx = i
          break
    
    if d >= 7:
      if idx == -1:
        for i in range(N):
          if heights[i] == B-2:
            idx = i
            break
    
    # put to tower with height less than B-2
    if idx == -1:
      for i in range(N):
        if heights[i] < B-2:
          idx = i
          break

    # d <= 5 but all heights >= B-2, has to put to the lowest tower
    if idx == -1:
      for i in range(N):
        if (idx == -1 or heights[idx] > heights[i]):
          idx = i

    # update
    heights[idx] += 1
    numbers[idx] = str(d) + numbers[idx]
    
    # print result
    print(idx + 1)
  S = sum(map(int, numbers))
  return S
        
      
if __name__ == '__main__':
  try:
    T, N, B, P = list(map(int, input().split()))
    S = 0
    for i in range(1, T+1):
      S += solve()
    # assert(S >= P)
    assert(S >= P)
  except Exception as e:
    print(e)
