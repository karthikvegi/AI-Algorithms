# ****************************************************************
# This code will solve an mdp object by returning a policy vector
# The policy vector will have utility value for all the given states
# The utility function computes the utility value of the states
# The agent will move from state to state based on the utility function
# Reference: http://aima.cs.berkeley.edu/python/mdp.html
# ****************************************************************

class Solver:
    def __init__(self, mdp):
        # initializing mdp object
        self.mdp=mdp

        # Policy vector
        self.policy=[]

        # Utility vector to store utility values
        self.utility=[]

    def solve(self):
        # Getting the length of the states in the MDP object
        state_length=len(self.mdp.S())

        # Building a policy vector for all the states
        for state in range(state_length):
            self.policy.append(state)

        # Building a utility vector for all the states
        for state in range(state_length):
            self.utility.append(state)

        # Value Iteration algorithm for MDP
        # Reference: http://aima.cs.berkeley.edu/python/mdp.html
        flag = True;

        # Run the value iteration algorithm until false
        while flag:
            flag = False
            # Compute utilities
            for state in self.mdp.S():
                # For every state, compute the utility value from the probability, reward and utility function
                utility=[self.mdp.P(state, self.policy[state], new_state)
                                           * (self.mdp.R(state) + self.mdp.gamma()
                                              * self.utility[new_state]) for new_state in self.mdp.S()]

                # Summation of utility
                self.utility[state] = sum(utility)
                
                # print(self.utility[state])

            for state in self.mdp.S():
                best_value = self.utility[state]

                for action in self.mdp.A():
                    # Compute the value
                    computed_value= [self.mdp.P(state, action, new_state)
                                 * (self.mdp.R(state) + self.mdp.gamma()
                                    * self.utility[new_state]) for new_state in self.mdp.S()]

                    # print(comp_value)

                    # Sum of computed value
                    computed_sum = sum(computed_value)

                    # print(comp_sum)

                    # Compare the computed value with best value
                    if computed_sum > best_value:
                        self.policy[state] = action

                        # update the policy vector
                        best_value = computed_sum

                        flag = True

        # Return the final policy
        return self.policy