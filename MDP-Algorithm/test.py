import solver
class ChainMDP:

  # Probability
  def P(self, s, a, u):
    if a == 'left' and u == s-1:
      return 0.7
    if a == 'left' and u == s+1:
      return 0.3
    if a == 'left' and s == 0 and u == 0:
      return 0.7
    if a == 'right' and u == s+1:
      return 0.7
    if a == 'right' and u == s-1:
      return 0.3
    if a == 'right' and u == s and u == 10:
      return 0.7
    return 0.0

  # Discount Factor
  def gamma(self):
    return 0.9

  # Rewards
  def R(self, s):
    if s == 0 or s == 10:
      return 1.0
    return 0.0

  # Actions
  def A(self):
    return ['left', 'right']

  # States
  def S(self):
    return [0,1,2,3,4,5,6,7,8,9,10]

  # Initial State
  def initial_state(self):
    return 5


mdp = ChainMDP()
s = solver.Solver(mdp)
policy = s.solve()

for i in range(0, 5):
  assert(policy[i] == 'left')

for i in range(6,11):
  assert(policy[i] == 'right')



