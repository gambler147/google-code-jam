import traceback
def solve():
  """
  Group E and S by consecutive zeros and ones. The binary string can be then converted to a list of numbers
  S = [a0, a1, ...] where a[i] is the number of bits in ith group, notice that the first group is always ones.
  Lets assume converting S to E needs X NOT operations in total, and notice that each NOT operation removes the first
  element in the group list and will not change the value in each group. It is obvious that X should not be exceeding
  len(S) + 1. 

  Also, a double operation will append a new group or update last group's bit count.

  So we loop X from 0 to len(S)+1, then S will be converted to a new string S', if S' prime is prefix of E, then will need
  to check how many additional groups in E's suffix, because adding an additional group requires 1 NOT operation and total 
  number of additional groups should not exceed X, otherwise it is impossble.

  reference: https://github.com/kamyu104/GoogleCodeJam-2021/blob/main/Round%201C/double_or_noting.py
  """

def flip(s):
    return "".join(["01"[c == '0'] for c in s]).lstrip('0') or "0"

def not_count(s):
    s += '0'  # if s ends with '1', it requires one more "not" operation
    ans = 0
    for i in range(len(s)-1):
      ans += s[i+1] != s[i]
    return ans

def solve():
    S, E = input().strip().split()
    # loop through all possible number of flips
    result = float('inf')
    X = 0 # number of flips
    S_ = S # make a copy
    while S_ != '0':
      if S_ == E[:len(S_)] and X >= not_count(E[len(S_):]):
        return X + (len(E) - len(S_))
      S_ = flip(S_)
      X += 1
    # if unable to find a E's prefix before turning S to '0'
    # S -> '0' -> E
    if X >= not_count(E):
      return X + len(E) - (E[0] == '0') # if E is '0', not additional ops needed


    M = not_count(E[1:])
    if M == 0:
        # E is in form 10000...0 
        return X+1+(len(E)-1)
    if M == 1:
        # E is in form 11111..1 or 1111..00000..
        return X+1+len(E)+1

    return "IMPOSSIBLE"


if __name__ == '__main__':
  try:
    T = int(input())
    for i in range(1, T+1):
      res = solve()
      print("Case #{}: {}".format(i, res))
  except Exception as e:
    print(traceback.format_exc())
