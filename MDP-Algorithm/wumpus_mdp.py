
class WumpusMDP:
	# wall_locations is a list of (x,y) pairs
	# pit_locations is a list of (x,y) pairs
	# wumnpus_location is an (x,y) pair
	# gold_location is an (x,y) pair
	# start_location is an (x,y) pair representing the start location of the agent

	def __init__(self, wall_locations, pit_locations, wumpus_location, gold_location, start_location):
		self.walls = wall_locations
		self.pits = pit_locations
		self.wumpus = wumpus_location
		self.gold = gold_location
		self.start = start_location

	def A(self):
		return ["do nothing", "left", "right", "up", "down", "shoot left", "shoot right", "shoot up", "shoot down"]

	def S(self):
		return [(0,0), (0,1), (0,2), (0,3), (1,0), (1,1), (1,2), (1,3), (2,0), (2,1), (2,2), (2,3), (3,0), (3,1), (3,2), (3,3)]

	def P(self, s, a, u):
		move_action = ["left", "right", "up", "down"]
		if a == "do nothing": return 1.0
		elif a in move_action:
			for w in self.walls:
				if w[0]==u[0] and w[1] == u[1]: return 0
			if s[0] == u[0] and s[1] == u[1]+1 and a == "right": return 0.9
			elif s[0] == u[0] and s[1] == u[1]-1 and a == "left": return 0.9
			elif s[0] == u[0]+1 and s[1] == u[1] and a == "down": return 0.9
			elif s[0] == u[0]-1 and s[1] == u[1] and a == "up": return 0.9
			else: return 0.1
		else:
			if a == "shoot left":
				for i in range(s[1], s[1]-4, -1):
					if i < 0 == 0: return 0.0
					if self.wumpus[0]==s[0] and self.wumpus[1] == i: return 1.0
			elif a == "shoot right":
				for i in range(s[1], s[1]+4):
					if i > 4: return 0.0
					if self.wumpus[0]==s[0] and self.wumpus[1] == i: return 1.0
			elif a == "shoot down":
				for i in range(s[0], s[0]+4):
					if i > 4: return 0.0
					if self.wumpus[0]==i and self.wumpus[1] == s[1]: return 1.0
			elif a == "shoot up":
				for i in range(s[0], s[0]-4, -1):
					if i < 0: return 0.0
					if self.wumpus[0]==i and self.wumpus[1] == s[1]: return 1.0

	def R(self, s):
		if self.gold[0]==s[0] and self.gold[1] == s[1]: return 100
		for w in self.walls + self.pits + [self.wumpus]:
			if w[0]==s[0] and w[1] == s[1]: return -100
		return 0

	def initial_state(self):
		return self.start

	def gamma(self):
		return 0.99

# EXAMPLE USAGE:
# mdp = WumpusMDP([(0,0),(1,0),(2,0),(3,0),(3,1),(3,2),(3,3),(2,3),(1,3),(0,3),(0,2),(0,1)], [(1,2)], (2,1), (2,2), (1,1))
