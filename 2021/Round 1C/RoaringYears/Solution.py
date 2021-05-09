import traceback
def solve():
  """
  Notice that we can always find a roaring year whose digits is at most D+1, where D is the number of digits of given year N.

  So we can first search for solution whose digits is exactly D. We need to pick the starting number, we iterate d from 1 to (D+1)//2.
  d is the number of digits of starting number.
  if D%d == 0:
    the starting number can only be N's first d digits or plus 1
  else:
    the starting number can only be 10**d - D//d, we can simply iterate from 10**d - D//d to 10**d - 1 to check if any reaches minimum

  Then we check solution with D+1 digits. If D+1 is even, we can simply let d = (D+1)//2, and start from 10**d. If D+1 is odd, then we iterate
  all d from 1 to (D+1)//2, if (D+1) % d == 0, then it might be possible and starting number must be 10**d.

  Time complexity: O(log10(N)**2)
  """

  N = input()
  D = len(N)

  # first find solutions with d digits
  res = float('inf')
  for d in range(1, (D+1)//2+1):
    year = find_min_year_with_same_digits(d, N)
    if year != -1:
      res = min(res, year)

  if res != float('inf'):
    return res

  # find solutions with D+1 digits
  res = find_min_year_with_plus_one_digits(N)

  return str(res)



def find_min_year_with_plus_one_digits(N):
  D = len(N)
  if (D+1)%2 == 0:
    d = (D+1)//2
    start = 10**(d-1)
    ans = str(start) + str(start+1)
    return ans

  # (D+1) is odd, we have to check all d from 1 to D//2
  ans = float('inf')
  for d in range(1, D//2+1):
    cur = ""
    if (D+1)%d == 0:
      s = 10**(d-1)
      while cur == "" or int(cur) <= int(N):
        cur += str(s)
        s += 1
      if int(cur) < ans:
        ans = int(cur)
  return ans
  
    
def find_min_year_with_same_digits(d, N):
  """
  find min year with starting number with d digits, d <= D//2
  """
  D = len(N)
  if d > D//2:
    return float('inf')

  res = float('inf')
  if D%d == 0:
    init = int(N[:d])
    if d == 1:
      # d == 1 is special, because 1 divides every integer so we need to check all possible starting numbers (1 - 9)
      starting_options = list(range(init, 10))
    else:
      starting_options = [init, init+1]
    for s in starting_options:
      ans = ""
      while ans == "" or int(ans) <= int(N):
        ans += str(s)
        s += 1
      if len(ans) == D:
        res = min(res, int(ans))
    
  else:
    # start number can only be 10**d - D//d to 10**d - 1, less than 10 numbers
    for s in range(10**d - D//d, 10**d):
      if s <= 0: continue
      ans = ""
      while ans == '' or int(ans) <= int(N):
        ans += str(s)
        s += 1
      if len(ans) == D:
        res = min(res, int(ans))

  return res
  


if __name__ == '__main__':
  try:
    T = int(input())
    for i in range(1, T+1):
      res = solve()
      print("Case #{}: {}".format(i, res))
  except Exception as e:
    print(traceback.format_exc())
