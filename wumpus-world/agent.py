import random

class Agent:
  def get_action(self):
    actions = ['MOVE_UP', 'MOVE_DOWN', 'MOVE_LEFT', 'MOVE_RIGHT']
    extras = ['SHOOT_UP', 'SHOOT_DOWN', 'SHOOT_LEFT', 'SHOOT_RIGHT']
    if random.random() > 0.07:
      return random.choice(actions)
    return random.choice(extras)
    

  def give_senses(self, location, breeze, stench):
    pass

  def killed_wumpus(self):
    pass


