from sys import stdout

class Solution:
  @staticmethod
  def solve():
    """
    N = 100 players
    Q = 10000 questions
    We know Q question difficulties are drawing from uniform distribution in [-3.0, 3.0]. 
    Then since Q is large enough, the average number of questions the player answered correctly can
    be an estimate of E(f(s - q)) according to LLN. Given assumed distribution of q we can calculate the expecation, 
    and we can derive s = -log((exp(a) - exp(-a)) / (exp(2az) -1) - exp(-a)), where [-a, a] is the range of q and 
    z is the average value of player's correct answer. 

    Then, to determine which player is most likely to be the cheating player, we calculate the likelyhood
    of each player based on his estimated skill level and his answer in easiest and hardest questions. This
    is because for any player not cheating, it is more likely to answer much more easy questions than hard questions.
    The likelyhood of player p is prod( ans[j] * f(s[p] - q[j]) + (1-ans[j]) * f(s[p] - q[j]) for all j ). For precision
    matter, we take the log likelyhood. We find the player with smallest log likelyhood.
    
    Time: O(N * Q + QlogQ)
    Space: O(N * Q)
    """
    from math import exp, log

    Q = 10000 # number of questions
    N = 100 # number of players
    A = 3  # skill and difficulty levels are between [-A, A]

    def f(x):
      # sigmoid function
      return 1.0 / (1 + exp(-x))

    def skill_est(z):
      # estimate player's skill level given average correct answer
      return -log((exp(A) - exp(-A)) / ((exp(2*A*z) - 1) - exp(-A)))

    dinc = 2*A/Q # increment of skill level and difficulty level
    # read answers
    answer = []
    p_cnt = [0] * Q # count of players who answer each question correctly
    q_cnt = [0] * N # count of questions each player answered correctly
    s = [0] * N # estimated value of players' skill level
    for i in range(N):
      ans = list(map(int, input().strip()))
      answer.append(ans)
      for j, v in enumerate(ans):
        # update p_cnt and q_cnt
        p_cnt[j] += int(v)
        q_cnt[i] += int(v)
      s[i] = skill_est(q_cnt[i] / Q)
    # we sort the questions and get the score of each player in easiest and hardest questions
    questions = sorted(range(Q), key=lambda x: -p_cnt[x])
    # then we iterate players to get loss of each player
    min_likelyhood = float('inf')
    res = -1
    # to reduce the time complexity, we only consider the easiest 10% and hardest 10% questions
    for p in range(N):
      log_lhood = 0 # log likelyhood 
      # easiest questions
      for j in range(len(questions) // 10):
        q = questions[j]
        dl = -A + dinc * j
        log_lhood += log(answer[p][q] * f(s[p] - dl) + (1-answer[p][q]) * (1 - f(s[p] - dl)))
      # hardest questions
      for j in range(len(questions) - len(questions) // 10, len(questions)):
        q = questions[j]
        dl = -A + dinc * j
        log_lhood += log(answer[p][q] * f(s[p] - dl) + (1-answer[p][q]) * (1 - f(s[p] - dl)))
      # update if loss is greater than max_loss
      if log_lhood < min_likelyhood:
        min_likelyhood = log_lhood
        res = p
    
    return res+1


        
if __name__ == '__main__':
  T = int(input())
  P = int(input())
  for i in range(1, T+1):
    res = Solution.solve()
    print("Case #{}: {}".format(i, res))

  