class Solution:
  @staticmethod
  def solve():
    """
    test set 3 constraint:
    1 <= N <= 3, 1 <= Q <= 120

    for N = 1, we can simply return S/1, where S is the score of the student's answer, because we know nothing beyond this
    for N = 2, we can group question into 2 cases: 2 students have the same answer or they have different answer.
      Let T1, T2 be number of question for each case, so T1 + T2 = Q.
      Let k1, k2 be correct answer of first student in each group of questions, k1 <= T1 and k2 <= T2.
      So we have the relationship k1 + k2 = Q1 and k1 + (T2 - k2) = Q2. Which means we can solve analytically:
      k1 = (Q1 + Q2 - T2) / 2, k2 = (Q1 - Q2 + T2) / 2
      therefore:
        if k1 >= T1-k1, we completely follow student 1's answer, other wise we take student 1's (or student 2's) opposite answer
        similarly if k2 >= T2 - k2, we completely follow student 1's answer, otherwise we take student 2's answer
      Expected scores will be max(k1, T1-k1)/T1 + max(k2, T2-k2)/T2

    for N = 3, we can group questions into 4 cases: 
      1. three students share the same answer, total questions T1
      2. student 1 and 2 share the same answer, total question T2
      3. student 1 and 3 share the same answer, total questions T3
      4. student 2 and 3 share the same answer, total question T4
    T1 + T2 + T3 + T4 = Q
    Let k1, k2, k3, k4 be questions student 1 answered correctly in each of these 4 cases, then we have the relationship:
      k1 + k2 + k3 + k4 = Q1
      k1 + k2 + (T3 - k3) + (T4 - k4) = Q2
      k1 + (T2 - k2) + k3 + (T4 - k4) = Q3
    This system of equation is not uniquely solved, but we can iterate all possible cases for k1, given k1, we can solve
      k2 = (Q1 + Q2 - T3 - T4)/2 - k1
      k3 = (Q3 - Q2 - T2- + T3)/2 + k2
      k4 = Q1 - k1 - k2 - k3
    We verify these values meet the condition then we know the we can make our choice on each group of questions based on the relationship
    of ki versus Ti/2, if ki >= Ti/2, we following student 1's answer, otherwise, we take the opposite answer.

    For each solution k1, k2, k3, k4, total number of combinations of correct answers will be
    S = comb(T1, k1) * comb(T2, k2) * comb(T3, k3) * comb(T4, k4)
    so the probability of given distribution of k1, k2, k3, k4 is S/sum(S).

    notice we have 2**4 options for choosing our final result, because in each group
    we can either complete follow student 1's answer or the opposite. We simply check
    which option makes our expected score maximum

    Time complexity: O(Q)?
    """

    from fractions import Fraction
    # from math import comb  # Python 3.7 does not provide comb function
    def opposite(s):
      res = []
      for c in s:
        res.append('F' if c == 'T' else 'T')
      return ''.join(res)

    def comb(n, k):
      result = 1
      for i in range(1, k+1):
        result = result * (n-i+1) // i
      return result

    # read number of students and questions
    N, Q = list(map(int, input().split()))
    # read student answers and scores
    answers = []
    scores = []
    for _ in range(N):
      s = input().split()
      answers.append(s[0])
      scores.append(int(s[1]))

    # N takes 3 cases
    if N == 1:
      if scores[0] >= Q - scores[0]:
        return "{} {}/{}".format(answers[0], scores[0], 1)
      else:
        return "{} {}/{}".format(opposite(answers[0]), Q - scores[0], 1)

    if N == 2:
      # find T1 and T2
      T1 = 0
      T2 = 0
      Q1, Q2 = scores
      for q in range(Q):
        if answers[0][q] == answers[1][q]:
          T1 += 1
        else:
          T2 += 1
      k1 = (Q1 + Q2 - T2) // 2
      k2 = (Q1 - Q2 + T2) // 2
      ans = []
      for q in range(Q):
        a1, a2 = answers[0][q], answers[1][q]
        if a1 == a2:
          if k1 >= T1 - k1:
            ans.append(a1)
          else:
            ans.append(opposite(a1))
        else:
          # answers[0][q] != answers[1][q]
          if k2 >= T2 - k2:
            ans.append(a1)
          else:
            ans.append(a2) # or opposite(a1)
      ans = ''.join(ans)
      scr = max(k1, T1 - k1) + max(k2, T2 - k2)
      return "{} {}/{}".format(ans, scr, 1)

    if N == 3:
      T = [0] * 4
      S = scores
      # get Ti
      for q in range(Q):
        if answers[0][q] == answers[1][q] == answers[2][q]:
          T[0] += 1
        elif answers[0][q] == answers[1][q]:
          T[1] += 1
        elif answers[0][q] == answers[2][q]:
          T[2] += 1
        else:
          T[3] += 1
      
      # iterate all possible values of k1, k2, k3, k4
      ks = []
      for k1 in range(T[0]+1):
        k2 = (S[0] + S[1] - T[2] - T[3])//2 - k1
        k3 = (S[2] - S[1] - T[1] + T[2])//2 + k2
        k4 = S[0] - k1 - k2 - k3
        if 0 <= k2 <= T[1] and 0 <= k3 <= T[2] and 0 <= k4 <= T[3]:
          ks.append((k1, k2, k3, k4))

      # compute probability of each group value (k1, k2, k3, k4)
      total_comb = 0
      combination = []
      for k in ks:
        cur = comb(T[0], k[0])*comb(T[1], k[1])*comb(T[2], k[2])*comb(T[3],k[3])
        combination.append(cur)
        total_comb += cur

      # establish a flag list of 4 x 4
      op = []
      for i in range(16):
        op.append( list(map(int, format(i, '04b'))) )

      # calculate max_expected score
      max_exp_scr = 0
      max_l = None
      for l in op:
        exp_scr = 0 # expected score
        for k, c in zip(ks, combination):
          # find score of each group
          scr = 0
          for i in range(4):
            scr += l[i] * k[i] + (1-l[i]) * (T[i] - k[i])
          exp_scr += Fraction(c, total_comb) * scr
        if exp_scr >= max_exp_scr:
          max_l = l
          max_exp_scr = exp_scr

      # return the final answer string
      ans = []
      for q in range(Q):
        a1, a2, a3 = answers[0][q], answers[1][q], answers[2][q]
        if a1 == a2 == a3:
          ans.append(a1 if max_l[0] else opposite(a1))
        elif a1 == a2:
          ans.append(a1 if max_l[1] else opposite(a1))
        elif a1 == a3:
          ans.append(a1 if max_l[2] else opposite(a1))
        else:
          ans.append(a1 if max_l[3] else opposite(a1))

      ans = ''.join(ans)
      return "{} {}/{}".format(ans, max_exp_scr.numerator, max_exp_scr.denominator)
      
      
if __name__ == '__main__':
  T = int(input())
  for i in range(1, T+1):
    res = Solution.solve()
    print("Case #{}: {}".format(i, res))

  