# ****************************************************************
# This code will solve an mdp object by returning a policy vector
# The policy vector will have utility value for all the given states
# The utility function computes the utility value of the states
# The agent will move from state to state based on the utility function
# Reference: http://aima.cs.berkeley.edu/python/mdp.html
# ****************************************************************
import random

# Returns an element with lowest fn(seq[i]) score; tie goes to first one.
def argmin(seq, fn):
	best = seq[0]; best_score = fn(best)
	for x in seq:
		x_score = fn(x)
		if x_score < best_score:
			best, best_score = x, x_score
	return best


# Return an element with highest fn(seq[i]) score; tie goes to first one.
def argmax(seq, fn):
	return argmin(seq, lambda x: -fn(x))

# given an MDP, state s and action a, return list of (state, probability) pairs
def transitions(mdp, s, a):
	ret = []
	for u in mdp.S():
		ret.append((u, mdp.P(s, a, u)))
	return ret

# calculate expected policy
def calcPolicy(mdp, a, s, U):
	return sum([p * U[s1] for (s1, p) in transitions(mdp, s, a)])

class Solver:
	def __init__(self, mdp, epsilon=0.001):
		# initializing mdp object
		self.mdp = mdp
		self.epsilon = epsilon

	def solve(self):
		# Value Iteration algorithm for MDP
		mdp = self.mdp
		epsilon = self.epsilon

		U1 = dict([(s, 0) for s in mdp.S()])
		U = None
		A = dict([(s, random.choice(mdp.A())) for s in mdp.S()])
		R, gamma = mdp.R, mdp.gamma()

		# Run the value iteration algorithm until false
		while True:
			U = U1.copy()
			delta = 0
			for s in mdp.S():
				U1[s] = R(s) + gamma * max([sum([p * U[s1] for (s1, p) in transitions(mdp, s, a)])
											for a in mdp.A()])
				delta = max(delta, abs(U1[s] - U[s]))
			if delta < epsilon * (1 - gamma) / gamma:
				 break
		for s in mdp.S():
			A[s] = argmax(mdp.A(), lambda a: calcPolicy(mdp, a,s,U))
		return A
